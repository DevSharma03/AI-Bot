import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "98cd9f73ae7c4eafb420bdacdc262d33"  # Api key for news from News Api

# Set the speech rate (words per minute)
rate = engine.getProperty('rate') 
# Get the current speech rate
engine.setProperty('rate', rate - 200)
# Decrease the rate (default is usually around 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if response.status_code == 200:
            # Parse the JSON responce
            data = response.json()
            # Extract the article
            articles = data.get('articles', [])
            # Print the headlines
            for article in articales:
                speak(article['title'])
    else:
        pass
    
if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        #listen for the wake word 'Jarvis'
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")
                #Listen for commond
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        
        except Exception as e:
            print("error; {0}".format(e))
            
