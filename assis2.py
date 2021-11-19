[0:19 pm, 19/11/2021] Satish @lpu: # in terminal install these
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


def welcom…
