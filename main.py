import speech_recognition as sr 
import webbrowser
import pyttsx4 as pyttsx3
import musiclibrary 
import os


recognizier = sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("http://google.com")
    if "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("http://facebook.com")
    if "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        speak("playing")
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    if "open game" in c.lower():
        speak("opening game")
        os.startfile(r"C:\Program Files (x86)\Assassin's Creed - Rogue\ACC.exe")
            

       

   
if __name__=="__main__":
    speak("Hello Deepesh, I am your virtual assistant. System is ready to help you.")
    
    
    while True:

        try:
            with sr.Microphone() as source:
                print("Speak something...")
                  
                audio = recognizier.listen(source, timeout=5, phrase_time_limit=4)

            text = recognizier.recognize_google(audio) 
            print(text) 
            if "google" in text.lower():
                speak("Ya")

                with sr.Microphone() as source:
                    print("activated")
                    audio = recognizier.listen(source)
                    command= recognizier.recognize_google(audio)
                    processcommand(command)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except sr.RequestError:
            print("Could not request results, check your internet connection")       
             
       
        
     


     

             

                 






    




