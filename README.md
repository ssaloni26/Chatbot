# 🧠 Saloni's Custom Chatbot

A fun and intelligent desktop chatbot built using Python and Tkinter that can chat, greet you based on the time of day, play Rock-Paper-Scissors, tell jokes, analyze your mood using sentiment analysis, and even take voice input!



## ✨ Features

* 🗨️ Text-based chatting with natural responses using NLTK
* 🗣️ Voice input with Google Speech Recognition
* 🔊 Text-to-speech replies using `pyttsx3`
* ⏰ Time-based greetings (Good morning/afternoon/evening)
* 😄 Sentiment analysis using NLTK's VADER
* 🎮 Rock-Paper-Scissors mini-game
* 😂 Fetches live jokes from the internet
* 💾 Remembers your name across sessions
* 🏆 Rewards system to keep users engaged
* 📜 Scrollable chat history with GUI



## 🛠 Technologies Used

* Python 3.x
* Tkinter (GUI)
* NLTK (chatbot + sentiment analysis)
* pyttsx3 (text-to-speech)
* SpeechRecognition (voice input)
* requests (for jokes)
* pyaudio (for microphone support)



## 📦 Installation

### 1. Clone the repository:

bash
git clone https://github.com/ssaloni26/Chatbot.git
cd Chatbot


### 2. Install all dependencies:

bash
pip install -r requirements.txt



### 3. Download NLTK data (first-time use):

python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')


## ▶️ How to Run

Run the chatbot using Python:
python chatbot.py



## 🧩 Features in Detail

| Feature                 | Description                                       |
| ----------------------- | ------------------------------------------------- |
| **Greeting**            | Greets you based on current time                  |
| **Sentiment Analysis**  | Detects mood and replies empathetically           |
| **Name Memory**         | Saves your name in a local file (`username.txt`)  |
| **Rock-Paper-Scissors** | A mini-game with score tracking                   |
| **Joke API**            | Pulls dad jokes from `https://icanhazdadjoke.com` |
| **Voice Support**       | Converts your speech to text                      |
| **Rewards**             | Emoji-based reward system to keep you engaged     |



## 📁 File Structure
Chatbot/
├── chatbot.py          # Main chatbot script
├── .gitattributes      # Git configuration for text encoding
├── requirements.txt    # List of Python packages
└── README.md           # Project documentation



## 🙋‍♀️ Created By

**Saloni Swami**
[GitHub Profile](https://github.com/ssaloni26)



## 📜 License

This project is for educational purposes and may be modified or distributed freely with attribution.

