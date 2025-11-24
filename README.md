# 🤖 JARVIS Voice Assistant

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**A Python-based voice-activated virtual assistant inspired by JARVIS from Iron Man**

</div>

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🌟 Overview

JARVIS Assistant is an intelligent voice-activated assistant built with Python that can perform various tasks through voice commands. The project leverages speech recognition, text-to-speech conversion, and API integrations to provide a seamless user experience.

---

## ✨ Features

### 🎤 Voice Interaction
- **Speech Recognition**: Converts voice commands to text using Google Speech Recognition
- **Text-to-Speech**: Responds with natural-sounding voice using pyttsx3
- **Wake Word Detection**: Activates on "Jarvis" command

### 🌐 Web Automation
- **Browser Control**: Opens popular websites (Google, Facebook, LinkedIn, YouTube)
- **Smart Navigation**: Quick access to frequently used platforms

### 🎵 Music Integration
- **Music Playback**: Play songs from a predefined library
- **YouTube Integration**: Seamless music streaming
- **Custom Playlist Support**: Add your favorite tracks

### 📰 News Updates
- **Real-time News**: Fetches top headlines using NewsAPI
- **Voice Narration**: Reads out news headlines
- **Country-specific News**: Configured for US news (customizable)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| **Python 3.8+** | Core programming language |
| **speech_recognition** | Voice command processing |
| **pyttsx3** | Text-to-speech conversion |
| **webbrowser** | Browser automation |
| **requests** | API communication |
| **NewsAPI** | News headline retrieval |
| **python-dotenv** | Environment variable management |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Microphone for voice input
- Internet connection
- NewsAPI Key (free from [newsapi.org](https://newsapi.org/))

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/surag29/JARVIS_ASSISTANT.git
   cd JARVIS_ASSISTANT
   ```

2. **Install Dependencies**
   ```bash
   pip install speechrecognition
   pip install pyttsx3
   pip install requests
   pip install python-dotenv
   pip install pyaudio  # For microphone access
   ```

3. **Configure Environment Variables**
   
   Create a `.env` file in the project root:
   ```env
   NEWS_API=your_newsapi_key_here
   ```
   
   Get your free API key from [NewsAPI.org](https://newsapi.org/)

4. **Update Music Library** (Optional)
   
   Edit `musiclibrary.py` to add your favorite songs:
   ```python
   music = {
       "song_name": "youtube_url",
       # Add more songs...
   }
   ```

---

## 🚀 Usage

### Starting the Assistant

```bash
python main.py
```

### Voice Commands

| Command | Action |
|---------|--------|
| "Open Google" | Opens Google in browser |
| "Open Facebook" | Opens Facebook |
| "Open LinkedIn" | Opens LinkedIn |
| "Open YouTube" | Opens YouTube |
| "Play [song name]" | Plays the specified song |
| "News" | Reads top 5 news headlines |

### Example Interaction

```
User: "Jarvis"
Jarvis: "Ya" (Activates)

User: "Open Google"
Jarvis: [Opens Google in browser]

User: "Play dhurandhar"
Jarvis: [Plays the song from music library]

User: "News"
Jarvis: "Here are the top five news headlines..."
```

---

## ⚙️ Configuration

### NewsAPI Settings

In `main.py`, customize news parameters:
```python
r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
```

Change `country=us` to your preferred country code (in, uk, ca, etc.)

### Voice Settings

Adjust voice properties in the `speak()` function:
```python
engine = pyttsx3.init()  # Initialize TTS engine
# Customize rate, volume, and voice here
```

---

## 📁 Project Structure

```
JARVIS_ASSISTANT/
│
├── main.py              # Main application file
├── musiclibrary.py      # Music URLs dictionary
├── .gitignore          # Git ignore file
├── .env                # Environment variables (create this)
└── README.md           # Project documentation
```

### File Descriptions

- **main.py**: Core logic including speech recognition, command processing, and API integrations
- **musiclibrary.py**: Dictionary containing song names and their YouTube URLs
- **.env**: Stores sensitive API keys (not tracked in Git)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contribution
- Add weather integration
- Implement calendar management
- Add email sending capability
- Improve natural language processing
- Add more voice commands
- Create a GUI interface

---

## 📄 License

This project is licensed under the MIT License - feel free to use, modify, and distribute.

---

## 👨‍💻 Author

**Surag**
- GitHub: [@surag29](https://github.com/surag29)
- Project Link: [https://github.com/surag29/JARVIS_ASSISTANT](https://github.com/surag29/JARVIS_ASSISTANT)

---

## 🙏 Acknowledgments

- Inspired by JARVIS from Marvel's Iron Man
- NewsAPI for providing free news API
- Python community for excellent libraries

---

<div align="center">

**If you find this project useful, please consider giving it a ⭐!**

Made with ❤️ by Surag

</div>
