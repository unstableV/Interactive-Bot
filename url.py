# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:07:23 2019

@author: HP
"""
import re
import webbrowser
url=[ 'https://www.youtube.com/','https://www.netflix.com/r/','https://www.facebook.com/',
'https://www.instagram.com/r/',
'https://www.instagram.com/r/','whatsappmessenger://','https://www.swiggy.com/','telegram://']
app=['youtube','netflix','facebook','instagram','insta','whatsapp','swiggy','telegram']
text= "hey user.. open netflix for me"
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
            print(app[i])
            
            if(app[i]=="whatsapp" or app[i]=="telegram"):
                print("just click on the first image or icon..")
            webbrowser.open(url[i])