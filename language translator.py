# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:43:13 2022

@author: VIHAAN KATHURIA
"""

from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root=Tk()
root.geometry("1100x600")
root.configure(bg = "red")

languages = list(LANGUAGES.values())

title = Label(root,text = "Language Translator",bg = "red",font = ("Calibri",25,"bold"))
title.place(relx = 0.5,rely = 0.1,anchor = CENTER)

input_label = Label(root,text = "Enter Text",bg = "red",font = ("Calibri",15))
input_label.place(relx = 0.02,rely = 0.3,anchor = W)
input_language = ttk.Combobox(root,values = languages,width = 22,state = "readonly")
input_language.place(relx = 0.15, rely = 0.3 ,anchor = W )
input_text = Text(root,bg = "white",font =("calibri",15,"italic"),height = "7",wrap = WORD, width = "50",padx = 5,pady = 10,bd = 0)
input_text.place(relx = 0.02, rely = 0.5, anchor = W)

input_label = Label(root,text = "Output Language",bg = "red",font = ("Calibri",15))
input_label.place(relx = 0.8,rely = 0.3,anchor = E)
input_language = ttk.Combobox(root,values = languages,width = 20,state = "readonly")
input_language.place(relx = 0.98, rely = 0.3 ,anchor = E )
input_text = Text(root,bg = "white",font =("calibri",15,"italic"),height = "7",wrap = WORD, width = "50",padx = 5,pady = 10,bd = 0)
input_text.place(relx = 0.98, rely = 0.5, anchor = E)

def trans():
    translator = Translator()
    try:
        data = translator.translate(text = input_text.get(1.0,END),src = input_language.get(),dest = output_language.get())
        output_text.delete(1.0,END)
        output_text.insert(END,data.text())
    except:
        print("Try again")
    
button = Button(root,text = "Translate",command = trans)
button.place(relx = 0.5,rely = 0.75,anchor = CENTER)
root.mainloop()