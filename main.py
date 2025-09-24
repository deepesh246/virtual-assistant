import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary 
import os
import requests

recognizier = sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    api_key = "7f41b5ed1be422dda99858d9129ba834"  
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        weather_report = f"The current temperature in {city} is {temp} degrees Celsius with {description}."
        return weather_report
    else:
        return "Sorry, I could not fetch the weather right now."

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    if "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    if "open game" in c.lower():
        speak("open game")
        os.startfile(r"C:\Program Files (x86)\Assassin's Creed - Rogue\ACC.exe")    
    elif "weather" in c:
        speak("Which city should I check?")
        with sr.Microphone() as source:
            audio = recognizier.listen(source)
            city = recognizier.recognize_google(audio)
            print(f"City: {city}")
            report = get_weather(city)
            speak(report)
        
       

   
if __name__=="__main__":
   # speak("Hello Deepesh, I am your Jarvis assistant. System is online and ready.")
    speak("initializing deaon")
    
    while True:

        try:
            with sr.Microphone() as source:
                print("Speak something...")
                  
                audio = recognizier.listen(source)
            text = recognizier.recognize_google(audio) 
            print(text) 
            if "hey siri" in text.lower():
                speak("activated")

                with sr.Microphone() as source:
                    print("activated")
                    audio = recognizier.listen(source)
                    command= recognizier.recognize_google(audio)
                    processcommand(command)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except sr.RequestError:
            print("Could not request results, check your internet connection")       
       
        
     


     

             

                 






    



