# in terminal install these
# pip install pyttsx3
# pip install SpeechRecognition
# pip install wikipedia
# pip install jokes
# pip install wheel
# pip install pippin
# pippin install PyAudio
# pip install C:\Assis\PyAudio-0.2.11-cp310-cp310-win_amd64.whl

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

my_assis = Tk()
my_assis.geometry('400x480')
#my_assis.configure(bg='pink')
my_assis.title('Assis - Dummy Assistant')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def welcome():
    t_hour = int(datetime.datetime.now().hour)

    if 0 <= t_hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= t_hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    speak("I am Assis. How can I help you?")


def input_command():
    r = sr.Recognizer()

    lb11 = Label(my_assis, text='Listening...')
    lb12 = Label(my_assis, text='Recognising....')

    def lb11show():
        lb11.place(x=25, y=220)

    def lb11hide():
        lb11.place_forget()

    def lb12show():
        lb12.place(x=25, y=250)

    def lb12hide():
        lb12.place_forget()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
        lb11show()

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"command received: {query}\n")
        lb12show()

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.\n")

        def err_voice():
            messagebox.showwarning('Notice', 'Command not received.')

        return err_voice()

    return query


def myf1():
    clear = lambda: os.system('cls')

    clear()

    welcome()
    if _name_ == "_main_":

        clear = lambda: os.system('cls')

        clear()

        i = 0

        while i < 2:
            query = input_command().lower()

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

                str_time = datetime.datetime.now().strftime("%H:%M:S")
                speak(f"Sir,the time is {str_time}")
                print({str_time})

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'tell me a joke' in query:
                speak(pyjokes.get_joke())

            elif 'search' or 'play' or 'open' or 'go to' or 'open website' in query:
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
                speak("fFinding")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location)

            elif 'I am done' or 'stop' or 'exit' in query:
                speak('Thanks for giving me your time')
                exit()

        i += 1


def myf2():
    exit()


lb1 = Label(my_assis, text='Welcome....! ')
lb1.place(x=15, y=15)

lb2 = Label(my_assis, text='I am Assis, your virtual assistant.')
lb2.place(x=15, y=55)

btn1 = Button(my_assis, text='start !', command=myf1)
btn1.place(x=160, y=140)

btn2 = Button(my_assis, text='Stop !', command=myf2)
btn2.place(x=120, y=300)


def myf3():
    exit()


btn3 = Button(my_assis, text='Exit Program !', command=myf3)
btn3.place(x=220, y=300)

lb3 = Label(my_assis, text='Click on Start to execute program.')
lb3.place(x=15, y=400)

lb4 = Label(my_assis, text='Click Stop or Exit to terminate program.')
lb4.place(x=15, y=430)

mainloop()
