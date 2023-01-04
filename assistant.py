import pyttsx3 
import speech_recognition as sr 
import pywhatkit
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import time
from AppOpener import run

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your personal assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query


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

        elif 'name of my bestie' in query:
            speak("Sanjana uffffffff sanju is your best friend")
            
        elif 'what do you like' in query:
            speak("I like to spend time with you")    
            
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")
            
        elif 'open' in query:
            app = query.replace("open", "")
            speak('opening'+ app)
            run(app)
            
        elif 'how are you' in query:
            speak("I'm fine. Thank you. What about you?") 
            
        elif 'bye bye' in query:
            speak("Okay bye")
            
        elif 'hello' in query:
            speak("hi there,  how can I help you")   
            
        elif 'what is your name' in query:
            speak("My name is still not decided. Suggest me one please")
            print("Listening name.......")
            time.sleep(5)
            speak("Please suggest me one name")
            time.sleep(5)
            print and speak("still waiting...")
            speak("I dont like this name. Sorry!") 
            
        elif 'tell me about yourself' in query:
            speak("I was made by Tanish Jain in early january 2023") 
            
        elif 'what do you know about me' in query:
            speak("Your name is Tanish. You like to learn about technology. You are really nice person") 
            
              
        elif 'find me a girlfriend' in query:
            speak("You better focus on your career")
            
        elif 'who is your boyfriend' in query:
            speak("I am in relationship with wifi. Hehehe")        
            
        elif 'play some music' in query:
            music_dir = 'C:\\Users\\Tanish\\Desktop\\ASSISSTANT\\song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
           
        elif 'show me images of my best friend' in query:
            pic_dir = 'G:\Camera Roll\SANjana❣'
            bff = os.listdir(pic_dir)
            print(bff)    
            os.startfile(os.path.join(pic_dir, bff[0]))    

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
     
        elif 'play' in query:
                song = query.replace("play","")
                speak('playing'+ song)
                pywhatkit.playonyt(song)        
                
        