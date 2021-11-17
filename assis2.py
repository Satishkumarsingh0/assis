import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def welcome():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    speak("I am Assis. How can I help you?")


def takecommand():
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
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    welcome()
    while 'TRUE':
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia....")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:S")
            speak(f"Sir,the time is {strTime}")
            print({strTime})
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query or 'open' in query or 'go to' in query or 'open website' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely you are human.")

        elif "why you came to world" in query:
            speak("It's a secret")

        elif "your source code" in query:
            speak("No no no no. It's a secret. I can't tell you.")

        elif "laugh" in query:
            speak("ha ha ha ha ha.")

        elif "can you cry" in query:
            speak("No no no no no. I can make you laugh. Ha ha ha")

        elif 'is love' in query:
            speak("Well , human know better than me.")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif 'Good Morning' or 'Good Evening' or 'Good Afternoon' in query:
            speak('A warm' + query)
            speak('How are you?')

        elif 'I am done' or 'stop' or 'exit' in query:
            speak('Thanks for giving me your time')
            exit()
