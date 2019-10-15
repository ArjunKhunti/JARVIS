import datetime
import os
import smtplib
import webbrowser

from pygame import mixer
import pyaudio
import subprocess

import pyttsx3
import speech_recognition as sr
import wikipedia
import win32serviceutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 14:
        speak("Good noon!")

    elif 14 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    mixer.init()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('arjunvkhunti@gmail.com', 'Rudr@nsh007')
    server.sendmail('arjunvkhunti@gmail.com', to, content)
    server.close()

abcd = 3

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'close youtube' in query:
            webbrowser.BackgroundBrowser()

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
          #  abcd = os.startfile(os.path.join(music_dir, songs[0]))
            mixer.music.load(os.path.join(music_dir, songs[0]))
            mixer.music.play()

        elif 'stop music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            mixer.music.stop()

        elif 'open photos' in query:
            photos_dir = 'C:\\Users\\khunt\\OneDrive\\Pictures\\Saved Pictures'
            photo = os.listdir(photos_dir)
            print(photo)
            os.startfile(os.path.join(photos_dir, photo[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play video' in query:
            video_dir = 'D:\\Videos'
            video = os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir, video[0]))

        elif 'email to myself' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "arjunkhunti@yahoo.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Bro! I am not able to send this email")
