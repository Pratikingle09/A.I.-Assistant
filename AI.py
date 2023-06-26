from cgitb import text
from email.mime import audio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("hi. please tell me how may I help you")

def takeCommand():
    #it take the voice input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    
    
    except Exception as e:
        print("sorry can you say that agin...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
#while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('please wait searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        speak('opening youtube')
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak('opening google')
        webbrowser.open("google.com")

    elif 'open google meet' in query:
        speak('opening google meet')
        webbrowser.open("google meet.com")

    elif "show me today's weather" in query:
        speak('todays whether is')
        webbrowser.open("https://www.timeanddate.com/weather/india/akot/ext") 

    elif 'mail' in query:
        speak('opening mailbox')
        webbrowser.open("gmail.com")

    elif 'play music' in query:
        music_dir = 'C:\\Users\\prati\Music\\download'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'open vlc' in query:
        path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
        os.startfile(path)

    elif 'pratik' in query:
        speak('searchig for information')
        webbrowser.open("https://www.instagram.com/pratik_ingle_09/")

    elif 'mrunal' in query:
        speak('searchig for information')
        webbrowser.open("https://www.instagram.com/mrunal.mr/")

    


    #elif 'create a file' in query:      sintax for taking audio from user and convert into text
     #   speak('please wait sir')
      #  speak('you can speak now')
       # with sr.AudioFile(audio) as source:
        #    audio_data = r.record(source)
         #   text=r.recognize_google(audio_data)
          #  print(text)

        

    


        