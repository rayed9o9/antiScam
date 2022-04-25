
#Microphone with name "Speakers (Realtek(R) Audio)" found for `Microphone(device_index=2)`
import sys

import speech_recognition as sr
import pyautogui
#from plyer.utils import platform
from plyer import notification
from tkinter import *
from tkinter import ttk
from threading import *
import os

theapp = None
thecounter = None
root = Tk()
running = True


def speech_rec():
    r = sr.Recognizer()
    sound = sr.Microphone(device_index=2)
    with sound as source:
        audio = r.listen(source)
    return (r.recognize_google(audio))


flaged_phrazes = ["give me your password","tell me your password","give me your credit card number"]

import time

def flag():
    while (True):
        if( not running):
            print(running)
            break
        try:
            text = speech_rec()
            print(text)
            for i in flaged_phrazes:
                if (i in text):
                    return True
        except:
            print("error")

def mute_discord():
    pyautogui.hotkey('ctrl','`')

def mute_zoom():
    pyautogui.hotkey('alt', 'q')
    time.sleep(0.3)
    pyautogui.press('enter')

def app():
    print(f"the app{theapp.get()} and counter= {thecounter.get()}")

    if (flag()):
        # os.system("netsh interface set interface \"Wi-Fi 3\" disable")
        if(theapp.get()==0 and thecounter.get()==1):
            mute_zoom()
        if(theapp.get()==1 and thecounter.get()==1):
            print("dis mute")
            mute_discord()
        if(thecounter.get()==0):
            os.system("netsh interface set interface \"Wi-Fi 3\" disable")
        notification.notify(
            title='SCAM Alert',
            message='Do not share your information with this call',
            app_name='Anti-scam App'
            # app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
        )
def threading():
    running = True
    t1 = Thread(target=app)
    t1.start()

def stopRunning():
    running = False
    root.destroy()

if __name__ == '__main__':


    root.geometry("500x200")
    frm = ttk.Frame(root, padding=20)
    frm.grid(row=1,column=1)
    ttk.Label(frm, text="Make your choses and press \"Start\" ").grid(column=0, row=0)
    ttk.Button(frm, text="Start", command=threading).grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=stopRunning).grid(column=0, row=2)

    theapp= IntVar()
    thecounter = IntVar()
    ttk.Radiobutton(frm,text="zoom", variable=theapp, value=0).grid(column=2,row=1)
    ttk.Radiobutton(frm, text="Discord", variable=theapp, value=1).grid(column=3, row=1)


    ttk.Radiobutton(frm, text="Disable wireless", variable=thecounter, value=0).grid(column=2, row=2)
    ttk.Radiobutton(frm, text="End call", variable=thecounter, value=1).grid(column=3, row=2)

    root.mainloop()
    ##############





