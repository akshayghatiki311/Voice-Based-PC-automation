import pyttsx3
import webbrowser
import random
import wikipedia
import datetime
import wolframalpha
import sys
import os
import speech_recognition as sr
import pygame
import pyautogui
engine=pyttsx3.init('sapi5')
client=wolframalpha.Client('ET3326-APUXP54RL5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-2].id)
def speak(audio):
    print('Computer:'+audio)
    engine.say(audio)
    engine.runAndWait()
def wishing():
    currentH=int(datetime.datetime.now().hour)
    if currentH>=0 and currentH<12:
        speak('Good Morning!,Sir')
    elif currentH>=12 and currentH<15:
        speak('Good Afternoon!,Sir')
    elif currentH>=15 and currentH<20:
        speak('Good Evening!,Sir')
    else:
        speak('Good Night!,Sir')
wishing()
speak('Hello! I am your digital assistant Simon!')
speak('How may I help you?')
def myInput():
    inp=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        inp.pause_threshold=1
        audio=inp.listen(source)
    try:
        question=inp.recognize_google(audio,language='en-in')
        print('User: '+question+'\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I did not understand.Please type your query')
        question=str(input("Question: "))
    return question
if __name__=='__main__':
    while True:
        question=myInput()
        question=question.lower()
        if 'search' in question and 'youtube' in question:
            question=question.replace('search','')
            question=question.replace('youtube','')
            webbrowser.open('https://www.youtube.com/results?search_query='+question)
        elif 'search' in question and 'google' in question:
            question=question.replace('search','')
            question=question.replace('google','')
            webbrowser.open('https://www.google.com/search?hl=en&source=hp&ei=bKQQXb7FFIzlvgTR27HACA&q='+question)
        elif 'browse' in question:
            question=question.replace('browse ','')
            webbrowser.open('www.'+question+'.com')
        elif 'windows' in question and 'shutdown' in question:
            pyautogui.moveTo(0,767,duration=2)
            pyautogui.click(22,748,duration=1)
            pyautogui.click(25,705,duration=1)
            pyautogui.moveTo(23,619,duration=1)
            pyautogui.doubleClick(23,619)
        elif 'windows' in question and 'restart' in question:
            pyautogui.moveTo(0,767,duration=2)
            pyautogui.click(22,748,duration=1)
            pyautogui.click(25,705,duration=1)
            pyautogui.moveTo(23,650,duration=1)
            pyautogui.doubleClick(23,650)
        elif 'windows' in question and 'sleep' in question:
            pyautogui.moveTo(0,767,duration=2)
            pyautogui.click(22,748,duration=1)
            pyautogui.click(25,705,duration=1)
            pyautogui.moveTo(23,588,duration=1)
            pyautogui.doubleClick(23,588)
        elif 'windows' in question:
            question=question.replace('windows','')
            pyautogui.moveTo(0,767,duration=2)
            pyautogui.click(22,748,duration=1)
            pyautogui.click(91,749,duration=1)
            pyautogui.typewrite(question,interval=0.2)
            pyautogui.click(76,260,duration=2)       
        elif 'youtube' in question:
            webbrowser.open('www.youtube.com')
        elif 'google' in question:
            webbrowser.open("www.google.com")
        elif 'facebook' in question:
            webbrowser.open('www.facebook.com')
        elif 'gmail' in question:
            webbrowser.open('www.gmail.com')
        elif 'geeks' in question:
            webbrowser.open('www.geeksforgeeks.org')
        elif 'what\'s up' in question or 'how are you' in question or 'are you' in question:
            msgs=['I am fine!','Nice','Fine,helping others']
            speak(random.choice(msgs))
        elif 'music' in question:
            song='C:\\Users\\GHATIKI\\Music\\'
            songs=['7 Years','Jana Gana Mana','Donu_Donu_Donu','Cheliya Cheliya','Mehram','Mustafa Mustafa']
            pygame.mixer.init()
            play=song+random.choice(songs)+'.mp3'
            pygame.mixer.music.load(play)
            pygame.mixer.music.play()
            speak("Enjoy your music")
        elif 'bye' in question or 'stop' in question or 'abort' in question or 'exit' in question:
            speak('Bye Sir, have a nice day')
            sys.exit()
        elif 'found you' in question or 'invented you' in question:
            speak('Akshay Ghatiki is my GURU')
        elif 'hello' in question or 'Hi' in question:
            speak('Hello Sir!')
        elif 'search' in question and 'youtube' in question:
            question.replace('search','')
            question.replace('youtube','')
            webbrowser.open('https://www.youtube.com/results?search_query='+question)
        else:
            question=question
            speak('Searching....')
            try:
                try:
                    res=client.query(question)
                    results=next(res.results).text
                    speak('WOLFRAM SAYS-')
                    speak(results)
                except:
                    results=wikipedia.summary(question,sentences=2)
                    speak('WIKI SAYS-')
                    speak(results)
            except:
                speak('Could not find your query sir.Please search in Google.')
                webbrowser.open('www.google.com')
        speak('Next Command! Sir!')
