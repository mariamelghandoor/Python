This repository contains a Python script for a simple voice assistant. This assistant can listen to your voice commands and respond based on predefined commands.
Features
Listens to user voice commands through microphone.
Converts speech to text using Google Speech Recognition.
Responds to predefined commands with text-to-speech functionality.
Currently supports commands like "hello", "play music", "open website", and "what is the weather like today?".
Usage
Clone the repository:
git clone https://github.com/your-username/voice-assistant.git
Install dependencies:
pip install playsound speech_recognition gTTS
Run the script:
python voice_assistant.py
Speak your commands: The program will listen for your voice commands and respond accordingly.
Additional Notes
This is a basic example and can be extended to support more complex functionalities.
You can modify the commands dictionary to add new commands and responses.
Consider adding error handling and improving the accuracy of speech recognition.
