# MaitriAI - Conversational Image Chatbot

A sophisticated AI-powered chatbot that can analyze images and engage in multi-language conversations using OpenAI's GPT-4 Vision model, Google Translate API, and MongoDB for chat history persistence.

## 🎥 Demo Video

Watch the project in action:

<!-- Alternative HTML5 video player if the above doesn't work -->
<video width="800" controls>
  <source src="./2025-09-13 16-17-37.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 🌟 Features

- **🖼️ Image Analysis**: Upload and analyze images using OpenAI's GPT-4 Vision model
- **💬 Conversational AI**: Engage in natural conversations about uploaded images or general topics
- **🌍 Multi-language Support**: Translate responses to Hindi and Bengali using Google Translate API
- **📚 Chat History**: Persistent conversation history stored in MongoDB
- **🎨 Streamlit Interface**: User-friendly web interface built with Streamlit
- **🔄 Context Awareness**: Maintains conversation context for coherent interactions

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: OpenAI GPT-4 Vision (gpt-4o)
- **Translation**: Google Cloud Translate API
- **Database**: MongoDB
- **Image Processing**: PIL (Pillow)
- **Environment Management**: python-dotenv

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.7 or higher
- OpenAI API key
- Google Cloud credentials (for translation services)
- MongoDB connection string
- Required Python packages (see requirements.txt)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rajibsalui/Conversational-Image-Chatbot.git
   cd Conversational-Image-Chatbot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   MONGO_URI=your_mongodb_connection_string_here
   ```

4. **Set up Google Cloud credentials**:
   - Place your Google Cloud service account credentials file as `credentials.json` in the project root
   - Ensure the service account has access to the Google Translate API

## 💻 Usage

1. **Start the application**:
   ```bash
   streamlit run main.py
   ```

2. **Open your web browser** and navigate to the displayed local URL (typically `http://localhost:8501`)

3. **Using the chatbot**:
   - Upload an image using the sidebar file uploader
   - Type your question or prompt in the input field
   - Select your preferred language for the response
   - Click "Ask Solution" to get AI-generated responses
   - Use "Clear Chat" to reset the conversation history

## 🏗️ Project Structure

```
AI_Image_Chatbot/
│
├── main.py                    # Main Streamlit application
├── requirements.txt           # Python dependencies
├── credentials.json          # Google Cloud service account credentials
├── README.md                 # Project documentation
├── 2025-09-13 16-17-37.mp4  # Demo video
└── .env                      # Environment variables (create this)
```

## 🔧 Configuration

### MongoDB Setup
The application uses MongoDB to store chat history. Ensure your MongoDB instance is running and accessible via the connection string in your `.env` file.

### OpenAI API
The chatbot uses OpenAI's GPT-4 Vision model (`gpt-4o`) for image analysis and conversation. Make sure you have sufficient API credits and the correct API key.

### Google Translate API
Translation features require Google Cloud Translate API access. Set up a service account with appropriate permissions and download the credentials JSON file.

## 🎯 Key Features Explained

### Image Analysis
- Supports JPG, JPEG, and PNG formats
- Converts images to base64 for API processing
- Provides detailed analysis and answers questions about uploaded images

### Multi-language Support
- Automatic translation to Hindi and Bengali
- Preserves original English responses
- Uses Google Cloud Translate for accurate translations

### Chat History
- Persistent storage in MongoDB
- Displays recent conversations
- Includes both original and translated responses
- Timestamps for conversation tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/rajibsalui/Conversational-Image-Chatbot/issues) section
2. Create a new issue with detailed information about your problem
3. Include error messages, screenshots, and steps to reproduce

## 🙏 Acknowledgments

- OpenAI for the powerful GPT-4 Vision model
- Google Cloud for translation services
- Streamlit for the excellent web framework
- MongoDB for reliable data storage

## 📊 Future Enhancements

- [ ] Support for more image formats
- [ ] Additional language support
- [ ] Voice input/output capabilities
- [ ] Image generation features
- [ ] Export chat history functionality
- [ ] User authentication system

---

**Built with ❤️ by [Rajib Salui](https://github.com/rajibsalui)**
