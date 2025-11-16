import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import time 
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("NEWS_API")

recoginizer =  sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()



def processcommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")

     elif "open facebook" in c.lower():
          webbrowser.open("https://facebook.com")

     elif "open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")

     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")

     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]
          link = musiclibrary.music[song]
          webbrowser.open(link)
     
     elif "news" in c.lower():
          r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")

          if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            if not articles:
               speak("Sorry, I could not find any news.")
            else:
               speak("Here are the top five news headlines.")

               for i, article in enumerate(articles[:5]):
                 title = article.get("title")
                 if title:
                    speak(title)

          else:
             speak("Sorry, I could not fetch news at the moment.")
     

if __name__=="__main__":
    speak("initializing jarvis ........ ")
    # capture the auido from  mcirophone for the word 
    while True:
        
            # obtain audio from the microphone
            r = sr.Recognizer()
            
            
            

            print("recoginizing")
            # recognize speech using Sphinx
            try:
                with sr.Microphone() as source:
                   print("listening......")
                   audio = r.listen(source,timeout=5)
                word= r.recognize_google(audio)
                if(word.lower() == "jarvis"):
                     speak("ya")
                # for commands now 
                with sr.Microphone() as source:
                    print("jarvis active ....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
               

                    processcommand(command)
                
            
            except Exception as e:
                print("error; {0}".format(e))




