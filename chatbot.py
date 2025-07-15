import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import nltk
from nltk.chat.util import Chat, reflections
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime
import random
import speech_recognition as sr

# -------------------- TTS Engine -------------------- #
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def tell_joke():
    try:
        import requests
        res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        return res.json()["joke"]
    except:
        return "Oops! Couldn't fetch a joke right now."

def play_rps():
    global game_active, bot_choice
    game_active = True
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)
    return f"Let's play Rock-Paper-Scissors! I choose {bot_choice}. What do you choose?"

def check_rps_winner(user_choice):
    global game_active, bot_choice
    if user_choice not in ["rock", "paper", "scissors"]:
        return "Please choose rock, paper, or scissors."
    game_active = False
    if user_choice == bot_choice:
        return f"You chose {user_choice}. I chose {bot_choice}. It's a draw!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        return f"You chose {user_choice}. I chose {bot_choice}. You win! 🎉"
    else:
        return f"You chose {user_choice}. I chose {bot_choice}. I win! 😎"

def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.5:
        return "You sound happy 😊"
    elif score['compound'] <= -0.5:
        return "I sense you're feeling down. I'm here for you 💛"
    return None

def save_user_name(name):
    with open("username.txt", "w") as file:
        file.write(name)

def load_user_name():
    try:
        with open("username.txt", "r") as file:
            return file.read().strip()
    except:
        return ""

def reward_points():
    rewards = ['🌟', '🎉', '✨', '💎', '🏆']
    return f"You've earned a reward: {random.choice(rewards)}"

# --------------------Pattern-------------------- #
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you\??', ['I am fine, thank you!', 'Doing well, thanks for asking.']),
    (r'my name is (.*)', ['Nice to meet you %1!']),
    (r'i am (.*)', ['Hello %1, how can I help you?']),
    (r'your favorite movie', ['I love sci-fi movies!']),
    (r'your favorite color', ['Blue is my favorite color!']),
    (r'your favorite food', ['I enjoy pizza!']),
    (r'who (created|made) you', ['I was created by Saloni Swami 💻']),
    (r'.*joke.*', ['__tell_joke__']),
    (r'.*\b(play|game|rock|paper|scissors)\b.*', ['__play_game__']),
    (r'i am (sad|unhappy)', ['I am here for you 😊', 'Let me cheer you up 🌟']),
    (r'what can you do', ['I can tell jokes, play Rock-Paper-Scissors, greet you, chat with you, and much more!']),
    (r'who am i', ["You're my favorite person 😄"]),
    (r'who are you', ["I'm Saloni's custom chatbot!"]),
    (r'are you okay|how\'s it going', ["I'm great! Thanks for asking.", "Feeling awesome!"]),
    (r'.*your name.*', ["I'm ChatBot, Saloni's friendly assistant!"]),
    (r'.*(help|support).*', ['I am here to assist! What do you need help with?']),
    (r'tell me about (.*)', ["I'm still learning, but I can try to explain %1."]),
    (r'what is (.*)', ["I'm still learning, but I can try to explain %1."]),
    (r'thank you|thanks', ['You\'re welcome!', 'Anytime 😊']),
    (r'bye|quit|exit', ['Bye! Take care 💖', 'Goodbye! See you soon!']),
    (r'(.*)', ['Sorry, I didn’t understand that 😅. Can you rephrase?'])
]

chatbot = Chat(patterns, reflections)
sia = SentimentIntensityAnalyzer()
user_name = load_user_name()
game_active = False
bot_choice = ""

# -------------------- GUI -------------------- #
window = tk.Tk()
window.title("Saloni's Chatbot")
window.geometry("500x650")
window.resizable(False, False)

chat_log = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled')
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(window)
entry_frame.pack(pady=10)

entry_box = tk.Entry(entry_frame, width=40)
entry_box.pack(side=tk.LEFT, padx=5)

def send_message():
    global user_name, game_active
    user_input = entry_box.get().strip().lower()
    if not user_input:
        return

    chat_log.configure(state='normal')
    chat_log.insert(tk.END, f"You: {user_input}\n")

    if "my name is" in user_input:
        user_name = user_input.split("is")[-1].strip().capitalize()
        save_user_name(user_name)
        response = f"Nice to meet you, {user_name}!"
    elif game_active:
        response = check_rps_winner(user_input)
    else:
        response = chatbot.respond(user_input)
        if response == '__tell_joke__':
            response = tell_joke()
        elif response == '__play_game__':
            response = play_rps()
        elif user_name and '%1' in response:
            response = response.replace('%1', user_name)

    mood_reply = analyze_sentiment(user_input)
    if mood_reply:
        chat_log.insert(tk.END, f"Bot: {mood_reply}\n")
        speak(mood_reply)

    if random.randint(1, 10) > 8:
        reward = reward_points()
        chat_log.insert(tk.END, f"Bot: {reward}\n")
        speak(reward)

    chat_log.insert(tk.END, f"Bot: {response}\n")
    chat_log.configure(state='disabled')
    chat_log.see(tk.END)
    speak(response)
    entry_box.delete(0, tk.END)

    if user_input in ['bye', 'quit', 'exit']:
        window.after(1500, window.destroy)

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            entry_box.delete(0, tk.END)
            entry_box.insert(0, user_input)
            send_message()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Try again.")
        except sr.RequestError:
            speak("Network error. Try again later.")

send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

voice_button = tk.Button(entry_frame, text="\U0001F3A4 Speak", command=voice_input)
voice_button.pack(side=tk.LEFT, padx=5)

intro = f"{get_time_greeting()} {'Welcome back, ' + user_name + '!' if user_name else 'I am your chatbot. Type \"quit\" to exit.'}"
chat_log.configure(state='normal')
chat_log.insert(tk.END, f"Bot: {intro}\n")
chat_log.configure(state='disabled')
speak("Hi ")
speak(intro)

window.mainloop()
