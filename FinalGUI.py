#Importing libraries tkinter as a whole, messagebox from tkinter and the fonts for font styling
from tkinter import *
from tkinter import messagebox
import tkinter.font as style

import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

led = LED(15)

#Limit of the input
MAX_LIMIT = 12

#Setting up the GUI Layout
master = Tk()
master.minsize(275, 150)
myFont = style.Font(family = "monospace", size=10)
master.eval('tk::PlaceWindow . center')
master.title("User Input GUI")

#A variable to store the input provided by the user
var = StringVar()

#For converting each letter to morse code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#When the submit is pressed, output is shown at the output screen
#Also restricts the submitted input to MAX_LIMIT characters
#Uses the MORSE_CODE_DICT so as to convert, store and return the new converted morse code
def blink(chars):
    led.off()
    i = 0
    while len(chars) > i:
        if chars[i] == '.':
           led.on()
           sleep(1)
           led.off()
           
        elif chars[i] == '-':
           led.on()
           sleep(3)
           led.off()
           
        elif chars[i] == ' ':
           led.off()
           sleep(2)
        sleep(0.5)
        i += 1

def submit():
    name = var.get().upper()
    if len(name) <= MAX_LIMIT and len(name) > 0:
        print(name)
        #name = var.get().upper()
        arr = list(name)
        cipher = ''
        for letter in arr:
            if letter != ' ':
                # Looks up the dictionary and adds the
                # corresponding morse code
                # along with a space to separate
                # morse codes for different characters
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                cipher += ' '
        print(cipher)
        blink(cipher)
        
    elif len(name) > MAX_LIMIT or len(name) == 0:
        messagebox.showerror("Error", "Name cannot exceed " + str(MAX_LIMIT) + " characters or cannot be null")
        var.set("")

#For enabling the QUIT button
def close():
    GPIO.cleanup()
    master.destroy()

#MAIN
Label(master, text="FIRST NAME: ", font = myFont).grid(column=0, row=0)
Entry(master, width = 18, textvariable=var).grid(column=1, row=0, sticky='nesw')
Label(master, text=" ").grid(column=1, row=1)
Button(master, text = "SUBMIT", command = submit, height=1, width = 13, bg = "bisque2", bd = 3).grid(column=1, row = 2, sticky='nesw')
Button(master, command = close, text = "QUIT", width = 9, height = 1, bg = "red", bd = 3).grid(column=1, row=3)
master.protocol("WM_DELETE_MASTER", close)

#Iterating the main instructions
master.mainloop()