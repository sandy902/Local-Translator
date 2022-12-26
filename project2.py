from tkinter import *
from tkinter import ttk                                      #tkinter use for the GUI.
from gtts import gTTS                                        #gtts use for the converting text to speech.
from playsound import playsound                              #It is use for play audio files.
import speech_recognition                                    #It is use for converting the spoken words to the text
from googletrans import Translator,LANGUAGES                 #It is a python library that implemented google translate API
import time                                                  
import os

 #use for translating
  
def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text
    
#use for data displaying

def data():
    s =comb_sor.get()
    d =comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget =change(text= masg,src = s , dest = d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.resizable(0,0)
root.config(bg='SpringGreen2')

lab_txt = Label(root,text="Translator",font=("Time New Roman",30,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

#making a frame to show nicely

frame = Frame(root).pack(side=BOTTOM)

#making a Label
lab_txt = Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="black",bg="green4")
lab_txt.place(x=100,y=100,height=20,width=300)

#making a Textbox
Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text =list(LANGUAGES.values())

#making a combo box

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("english")

#making a button for translation of the input

button_change = Button(frame,text ="Translate",relief=RAISED,command=data)
button_change.place(x=150,y=300,height=40,width=150)

#making a combobox for desired output language

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

#making a label

lab_txt = Label(root,text="Dest Text",font=("Time New Roman",20,"bold"),fg="black",bg="green4")
lab_txt.place(x=100,y=360,height=20,width=300)

#making a textbox for desired output

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

#convert text to speech

def Text_to_speech():
    speech = gTTS(text = dest_txt.get(1.0, "end-1c"), slow=False)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
    os.system("DataFlair.mp3") 
   
#exit from the program

def Exit():
    root.destroy()

#give input as voice
 
def input_as_voice():
   recognizer = speech_recognition.Recognizer()
   with speech_recognition.Microphone() as source:
      voice =recognizer.listen(source)
      text = recognizer.recognize_google(voice,language="en")
      Sor_txt.insert(END,text)


Button(root, text = "listen" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=55, y=640)
Button(root, text = "Speak" , font = 'arial 15 bold', command =input_as_voice , width =4).place(x=345, y=640)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=200,y=640)

root.mainloop()










