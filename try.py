import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS



commands = {
    "hello": "Hi there",
    "play music": "Playing your favorite music...",
    "open website": "Opening website...",
    "what is the weather like today?": "Let me check the weather...",
}


#speaks the string i enter
def speak(text):
    #transfer the the text to audio with english language
    tts = gTTS(text=text,lang="en")
    #save the audio file and then play it
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

#takes the audio and turn it to text
def get_audio_from_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("say anything : ")
        audio = r.listen(source)
        #figuring out what is said
        said = ""

        try:
            said = recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))
    return said


word = get_audio_from_user() 
print(word)


def handle_command(command):
    if command in commands:
        speak(commands[command])
    else:
        speak("I don't understand what you mean")

word = get_audio_from_user()
handle_command(word)