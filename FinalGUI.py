# Importing Libraries required for code
from tkinter import*
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM) 
import time

## hardware
Led = LED (14)

MAX_LIMIT = 12

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler") # GUI title 
myFont = tkinter.font. Font(family = 'Helvetica', size = 12, weight = "bold") # Defining Font 

# A List that stores morse symbol for each alphabet, number and many symbols
translate_dict = { 'A':'.-', 'B':'-...',
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

#Defining variable of String type
ledinput = str()

### EVENT FUNCTIONS ###
def dash(): # Blink Led correspoding to dash in Morse code
    Led.on()
    time.sleep(0.6)
    Led.off()
    time.sleep(0.3)
def dot(): # Blink Led correspoding to dot in Morse code
    Led.on()
    time.sleep(0.2)
    Led.off()
    time.sleep(0.1)

# Converts String input into Morse code and blinks Led accordingly   
def Morse_code(ledinput): 
    ledinput = code.get().upper()
    if ledinput <= MAX_LIMIT and ledinput > 0:
        ledinput = " ".join(translate_dict[c] for c in ledinput.upper())
        print(ledinput)
        for c in ledinput:
            if c == ".":
                dot()
            elif c == "-":
                dash()
            elif c == "/" or c == " ":
                time.sleep(0.5)
            else:
                print("Enter a valid Character")
    else:
        print("Error!", "Input cannot exceed " + str(MAX_LIMIT) + " characters or cannot be null")
        ledinput.set("")


#Destroy the GUI and clean the code
def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
#Button to call the funtion Morse_code to blink input
ledButton = Button (win, text = 'Blink Name', font = myFont, command = lambda: Morse_code(ledinput), bg = 'aqua', height = 1)
ledButton.grid (row=0, column=2)

# Entry widget to get input from the User
code = Entry(win, font=myFont, width=15)
code.grid(row=0, column=1)

# Exit the GUI and cleans the code
exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'aqua', height = 1, width = 6)
exitButton.grid (row=2, column=1)

# To destroy GUI on pressing the cross button in the corner 
win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop() # Loop forever

