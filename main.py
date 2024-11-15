from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()  # Load all the environment variables from .env
import base64
import streamlit as st
import os
from PIL import Image
import openai
import time
from openai import OpenAI
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credentials.json')
#print(credentials)

translate_client = translate.Client(credentials=credentials)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
mongo_uri = os.getenv("MONGO_URI")  # MongoDB URI from .env

# Initialize MongoDB client
clientmongo = MongoClient(mongo_uri)
db = clientmongo["chatbot_db"]  # Replace with your database name
collection = db["chat_history"]  # Replace with your collection name

# Function to get response from OpenAI
def get_openai_response(input_text, user_prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": input_text},
                #{"role": "user", "content": user_prompt},
                {
                    "role": "user",
                    "content": [
                        {
                        "type": "image_url",
                        "image_url": {
                            "url":  f"data:image/jpeg;base64,{base64_image}"
                        },
                        },
                    ],
                }
            ],
            
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


# Function to encode the image
def encode_image(image_data):
    return base64.b64encode(image_data).decode('utf-8')  
    
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_data = {
            "name": uploaded_file.name,
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
        return image_data
    else:
        raise FileNotFoundError("No file uploaded")

# Function to translate text
def translate_text(text, target_language):
    if text:
        translation = translate_client.translate(text, target_language=target_language)
        return translation['translatedText']
    return None

# Initialize our Streamlit app
st.set_page_config(page_title="CREWX Chatbot")

st.header("Conversational AI Image Chatbot")

# Sidebar for image upload
uploaded_file = st.sidebar.file_uploader("Choose an image ...", type=["jpg", "jpeg", "png"])

image_data = input_image_details(uploaded_file) if uploaded_file else None


# Getting the base64 string
base64_image = encode_image(image_data['data']) if image_data else None


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Uploaded Image.", use_column_width=True)



# Load previous chat history from MongoDB on app load
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = list(collection.find().sort("timestamp", -1))[:10]


# Define the input prompt for the AI
input_prompt = """
You are a conversational AI chatbot. Your task is to respond to questions related to uploaded images (if provided) or general questions. Here are your instructions:
Image Context Awareness: When an image is uploaded, respond based on the user's questions, assuming context about general image features.
Answering Questions: Respond to questions accurately and with detailed information.
Contextual Memory: Remember the context of the conversation to provide coherent and relevant answers.
User Interaction: Engage with the user in a friendly and helpful manner, ensuring that your responses are clear and informative.
"""

# Define input text at the bottom
input_text = st.text_input("Input Prompt: ", key="input")
language_option = st.selectbox("Translate response to:", ("English", "Hindi", "Bengali"))
language_codes = {"Hindi": "hi", "Bengali": "bn"}
col1, col2 = st.columns([1, 1])
with col1:
    submit = st.button("Ask Solution")
with col2:
    clear_chat = st.button("Clear Chat")
# If submit button is clicked
if submit:
    with st.spinner('Generating...'):
      st.session_state.last_interaction_time = time.time()  # Update last interaction time
      
      response = get_openai_response(input_text,input_prompt)
      if language_option != "None":
        target_language = language_codes[language_option]
        translated_response = translate_text(response, target_language)
      else:
        translated_response = response
      chat_entry = {
          "user_prompt": input_text,
          "response": response,
          "translated_response": translated_response,
          "language": language_option,
          "timestamp": time.time()
      }
      if base64_image:
          chat_entry["image"] = base64_image  # Store image if uploaded
      
      collection.insert_one(chat_entry)  # Insert the chat entry into MongoDB
      
      # Add to session state history
      st.session_state.chat_history.insert(0, chat_entry)

if clear_chat:
    st.session_state.chat_history = []  # Clear the in-app chat history
    collection.delete_many({}) 

# Display chat history
st.subheader("Chat History")
for interaction in st.session_state.chat_history:
    st.write(f"**USER:** {interaction['user_prompt']}")
    st.write(f"**AI:** {interaction['response']}")
    if interaction.get('translated_response'):
        st.write(f"**AI (Translated - {interaction['language']}):** {interaction['translated_response']}")