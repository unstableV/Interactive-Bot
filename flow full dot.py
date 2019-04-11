# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:49:09 2019

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:49:46 2019

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:00:45 2019
@author: HP
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:27:11 2019
@author: HP
"""
#from googletrans import Translator
import io
import datetime
import os
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from pygame import mixer
import pyperclip
import pyttsx3
import pyaudio
import threading
import webbrowser
import nltk
import re

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize,sent_tokenize 


import wikipedia
import engineio
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from googletrans import Translator
import xlrd 
text="english"
loc = ("C:/Users/HP/Desktop/url.xlsx")   
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)   

#Tkinter app init (using custom ico in the title), using custom theme
engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    
engineio.setProperty('voice',voices[0].id)
def speak(text):
    engineio.say(text)
    engineio.runAndWait()

def talk(audio):
   for line in audio.splitlines():
       os.system(audio)
nltk.download('punkt')
 
root = Tk()                              
root.title('Voice Input')
root.iconbitmap('mic.ico')
style = ttk.Style()
style.theme_use('winnative')
# The image that is used for the speak button
photo = PhotoImage(file='microphone.png').subsample(15,15)
# Creating a guiding 'label' widget
label1 = ttk.Label(root, text="Say something", font='Courier 11 bold')     
label1.grid(row=0, column=1)
# the main part of the app. Defining what the click of the speak button does

x =  datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
a = x[9:]    
atr = a[0]+a[1]
atr1 = int(atr)
if atr1 <= 6 and atr1 >= 0:
    speak('its late night buddy..better go sleep..but how can i help you..')
elif atr1 >6 and atr1 < 12:
    speak( 'HEY!!GOOD MORNING buddy... how can i help you')
elif atr1 >= 12 and atr1 <=16:
    speak('HEY BUDDY,GOOD AFTERNOON TO YOU!!how can i help you')
elif atr1 >=16 and atr1<=20:
    speak('GOOD EVENING BUDDY!!how can i help you')
else:
    speak('its already nighT buddy....but can i help you')    
#speak("what language do you prefer to speak")
def fn1():
        # starting the recognizer, with some optional parameters that I found work well
       r = sr.Recognizer()                                         
       r.pause_threshold = 0.7                                    
       r.energy_threshold = 400
       with sr.Microphone() as source:
           try:
               audio = r.listen(source, timeout=5)
               
                    # use your own API key. get it here https://cloud.google.com/speech/ 
               global text
               #text = r.recognize_google(audio, language = 'en-IN')
    
              #      text=r.recognize_google(audio,language='hi-IN')
                    #else:
               #if(text=="english")     
                #   text=r.recognize_google(audio,language='en-IN')
               if(text=="Tamil"):
                  text=r.recognize_google(audio,language='ta-IN')
                  print(text)
                  
               elif(text=="telegu"):
                   text=r.recognize_google(audio,language='te-IN')
              
               elif(text=="malayalam"):
                   text=r.recognize_google(audio,language='ma-IN')
              
               elif(text=="hindi"):
                   text=r.recognize_google(audio,language='hi-IN')
              
               elif(text=="kanada" or text=="kanadam"):
                   text=r.recognize_google(audio,language='ka-IN')
               else:
                   text=r.recognize_google(audio,language='en-IN')
           #         print (text)
           #         talk(audio)
               destination_languages = {
                'en': 'english'
               }
               translator = Translator()
               for key,value in destination_languages.items():
                   x = translator.translate(text, dest=value).text
                   print(x)
                   speak(x)
               print("listened")
                    # playing the sound effect after recognition completed
               mixer.music.load('chime2.mp3')
               mixer.music.play()
                    # placing the recognized 'message' on the clipboard
                    #pyperclip.copy(message)
           except sr.UnknownValueError:
               print("THE AUDIO WAS NOT CLEAR..just repeat again ")
               fn1()
           except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))
           else:
               pass
           return text

def buttonClick():

        # using the pygame mixer to play sound effects, 'prompting' the user to speak
   mixer.init()
   mixer.music.load('chime1.mp3')
   mixer.music.play()
   text=fn1()
  # bool=re.search("event",text)
   #bool=re.search("events",text)
   #bool=re.search("college",text)
   #bool=re.search("club",text)
   global count
   count=0
   # using threading to prevent the app from freezing or becoming unresponsive
   if(text=="what can you do for me"):
        speak("HI.. I HAVE 3 FEATURES FOR U..I CAN HELP YOU IN TRANSLATING BASIC LANGUAGES TO ENGLISH..")
        speak("HELP TO FETCH EVENT DETAILS..HELP TO FETCH CONTENTS FROM WIKIPEDIA AND DISPLAY!!")
        speak("select what you want..")
        text="english"
        text=fn1()
        count=count+1
   if(text=="translate" or text=="translation"):
            speak("what languauge you want to speak")
            print("what languauge you want to speak")
            text=fn1()
            print(text)
            speak("speak now")
            text=fn1()
            count=count+1
 
   url=[ 'https://www.youtube.com/','https://www.netflix.com/r/','https://www.facebook.com/',
  'https://www.instagram.com/r/',
  'https://www.instagram.com/r/','whatsappmessenger://','https://www.swiggy.com/','telegram://']
   app=['youtube','Netflix','facebook','instagram','insta','whatsapp','swiggy','telegram']
   #text= "hey user.. open netflix for me"
   global b
   global b1
   b=0
   b1=0
   for j in range(len(app)):
        if(re.search(app[j],text)):
            b=1
            val=app[j]
            print(app[j])
        if(re.search("open",text)):
            b1=1
        
   if((b+b1)==2):


       for i in range(len(url)):
           if(re.search(val,url[i])):
               print("Haiyaaaaaa")
               print(app[i])            
               
               if(app[i]=="whatsapp" or app[i]=="telegram"):
                   print("just click on the first image or icon..")
               webbrowser.open(url[i])             
    
       
                           
#text="what are the events happening in next month"
   if(re.search("month",text)):
        f=re.search("next month",text)
        f1=re.search("previous month",text)
        f2=re.search("current month",text)
        f3=re.search("this month",text)
        f4=re.search("month",text)
        f5=re.search("last month",text)
        f6=re.search("day",text)
        f8=re.search("year",text)
        
        x1=0
        c1=0
        if f:    
            x1 =  datetime.datetime.now().strftime("%m")
            x1=int(x1)
            x1=x1+1
            c1=c1+1
        elif f1 and f5:
            x1 =  datetime.datetime.now().strftime("%m")
            x1=int(x1)
            x1=x1-1
            c1=c1+1
            
        elif f2 or f3:
            x1 =  datetime.datetime.now().strftime("%m")
            x1=int(x1)
            c1=c1+1
        elif f4 and c1==0 and f6 and f8:
            print("specify the month please")
        
            
        #x1=int(x1)
        print(x1)
        #x1=x1+1
        print(x1)
        x1=str(x1)
        
        print(x1)
        for j in range(sheet.nrows):
                v=sheet.cell_value(j,2)
                print(v)
                v=str(v)
                y=re.search(x1,v)
                
                if y:
                            print("matched")
                            w=sheet.cell_value(j,1)
                            webbrowser.open(w)
                            print("Done")
                            k=1
        if(k!=1):
                    speak("sorry there were no events at that time")
                        
   else:
           a=text.split(" ")
           stop_words = set(stopwords.words('english')) 
  
           word_tokens = word_tokenize(text) 
  
#filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
           filtered_sentence = [] 
  
           for w in word_tokens: 
                if w not in stop_words: 
                    filtered_sentence.append(w) 
           text=filtered_sentence
           for i in range(len(a)):
               b=a[i]
               #print(b)
               for j in range(sheet.nrows):
                   v=sheet.cell_value(j,0)
                   #print(v)
                   y=re.search(v,b)
                   if y:
                       count=count+1
   
                       print("matched")
                       w=sheet.cell_value(j,1)
                       webbrowser.open(w)
                       print("Done")

   
def thr():
    t1 = threading.Thread(target=buttonClick, daemon=True)
    t1.start()
# creating the Speak button, which calls 'thr' which invokes 'buttonClick()'
MyButton1 = Button(root, image=photo, width=150, command=thr, activebackground='#c1bfbf', bd=0)
MyButton1.grid(row=0, column=2)
# making sure the app stay on top of all windows (use this optionally)
root.wm_attributes('-topmost', 1)

# running the mainloop
root.mainloop() 
"""
if count==0:    
    a=text.split(" ");     
    #for i in a:                       
    x = wikipedia.summary(text,sentences=2) 
    print(x)
    speak(x)
"""