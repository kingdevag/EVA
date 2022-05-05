#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import
import json
import os
import random
import openai
import sys
import pyautogui
import pyttsx3
import pyjokes
import wikipedia
import configparser
try:
    import pywhatkit
except:
    pass

#From-Import
from tkinter import *
from googletrans import Translator
from datetime import datetime
from pynput.keyboard import Key, Controller
from openAW import openApp
from database import db

pathdirEVA = f"C:\\Users\\{os.getlogin()}\\Documents\\Eva"

config = configparser.ConfigParser()
config.read('config.ini')

IA_Name = config['DEFAULT']['IA-NAME']
name = config['DEFAULT']['NAME']
version = config['DEFAULT']['VERSION']

i = 1
h = 1

os.system("title EVA - Commands")

def getKey(key):
    collection = db['keys']
    KEY = collection.find_one()["KEYs"][key]
    return KEY

engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('volume',1.0)
openai.api_key = str(getKey("OpenAI"))
translator = Translator()
keyboard = Controller()
root = os.path.abspath(os.getcwd()).replace('\\', '/')

def getmail():
    with open(pathdirEVA + "\\account.json", "r") as fileM:
        text = json.load(fileM)
        mail = text['mail']
        return mail
        

def scr():
    
    if os.path.isdir(f"C:\\Users\\{str(os.getlogin())}\\Documents\\Eva"):
        pass
    else:
        os.mkdir(f"C:\\Users\\{str(os.getlogin())}\\Documents\\Eva")
        
    tad = getAnswer("Captura de pantalla")
    talk(tad)
    talk("en 3, 2, 1")
    screenshot = pyautogui.screenshot()
    screenshot.save(f"C:\\Users\\{str(os.getlogin())}\\Documents\\Eva\\screenshot.png")
    return("Captura de pantalla tomada.")

#====================================FUNCTIONS====================================


def getAnswer(tag:str):
    with open(pathdirEVA + '\\config\\lang.json', 'r') as LFile:
        lang = json.load(LFile)
    lang = lang['select']['Lang']
    lang = str(lang).upper()
    with open(os.getcwd() + '\\config\\answers.json', 'r') as AnswerFile:
        answer = json.load(AnswerFile)
        answer = answer['ES'][tag]
        answer = random.choice(answer)
        return str(answer)


def log(status:str, title:str):
    if os.path.isfile(pathdirEVA + "\\log\\logs.log"):
        file = open(pathdirEVA + "\\log\\logs.log", 'r+')
        text = file.read()
        file.close()
        file = open(pathdirEVA + "\\log\\logs.log", 'w+')
        time = str(datetime.today().strftime('%Y-%m-%d') + " - " + datetime.now().strftime("%H:%M:%S"))
        file.write(str(text + "\n" + "\n" + "#" + "TIME: " + time + "   #" + "EVENT: " + title.lower() + "\n" + "STATUS: " + status.lower()))
        file.close()
    if os.path.isfile(pathdirEVA + "\\log\\logs.log") == False:
        file = open(pathdirEVA + "\\log\\logs.log", 'w')
        time = str(datetime.today().strftime('%Y-%m-%d') + " - " + datetime.now().strftime("%H:%M:%S"))
        file.write(str("\n" + "#" + "TIME: " + time + "   #" + "EVENT: " + title.lower() + "\n" + "STATUS: " + status.lower()))
        file.close()

def talk(responce):
    x=pyttsx3.init()
        #print(responce)
    li = []
                    
    x.setProperty('rate',160)
    x.setProperty('volume',100)
    x.say(responce)
    x.runAndWait()


def close():
    print("\n")
    print("Saliendo")
    engine.stop()
    i = 0
    h = 0
    sys.exit()


def mute():
    for i in range(50):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)

def full():
    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)


#====================================CHAT-BOT====================================


def chat_bot(data):
    with open(pathdirEVA + '\\config\\lang.json', 'r') as LFile:
        lang = json.load(LFile)
    lang = lang['select']['Lang']
    lang = str(lang).upper()
    
    result = translator.detect(data)
    langD=result.lang
    confidence=result.confidence
        
    if confidence == 1:
        lang = langD

    with open(pathdirEVA + "\\prompt.txt", "r") as file:
        conversacion = file.read()

    start_sequence = "\Eva:"
    restart_sequence = "\nHuman: "
                
    text = translator.translate(data)

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt= conversacion + "Human: " + data,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", f" {name}:"]
    )
    answer = translator.translate(response['choices'][0]['text'], dest=lang.lower())
    answer = answer.text
    return str(answer)
    

#====================================TEXT====================================


def text_mode(text):
    try:
        with open(pathdirEVA + '\\config\\lang.json', 'r') as LFile:
            lang = json.load(LFile)
        lang = lang['select']['Lang']
        lang = str(lang).upper()
        data = str(text)
        data = data.lower().replace(name, '')
        
        if data == "":
            pass

        elif data.replace('?', '') == "como te llamas":
            return getAnswer("nombre") + name
        
        elif "chiste" in data:
            langs = ['IA', 'en']
            langG = str(random.choice(langs))
            if lang == 'IA':
                chat_bot(data)
            else:
                joke = pyjokes.pyjokes.get_joke(lang, 'all')
                if langG == 'en':
                    joke = translator.translate(joke, dest=lang.lower)
                    return joke.text

        elif "reproduce" in data:
            video = data
            video = video.lower().replace("reproduce", '')
            pywhatkit.playonyt(video)
            return getAnswer("Reproduce") + video
        
        elif "captura de pantalla" in data:
            return scr()
        
        elif "screenshot" in data:
            return scr()

        elif "busca" in data:
            if "wikipedia" in data:
                order = data.replace('busca', '').replace('en wikipedia' '').replace('in wikipedia' '')
                order = str(order).replace('wikipedia', '')
                wikipedia.set_lang(str(lang.lower))
                info = wikipedia.summary(order, 1)
                return info
            else:
                search = str(data.replace('busca', ''))
                pywhatkit.search(search)
                return getAnswer("Busca") + search
        elif 'hora' in data:
            hora = datetime.datetime.now().strftime('%I:%M %p')
            return "Horaa" + str(hora)

        elif 'abre' in data:
            app = data.replace('abre', '')
            r = openApp(app)
            if r == "NOT APP":
                chat_bot(data)
            else:
                return getAnswer("Abre") + r
        elif "sube" in data:
            if "volumen" in data:
                if 'todo' in data: 
                    full()
                    return getAnswer("SVolumen") + " al Maximo"
                else:
                    for i in range(5):
                        keyboard.press(Key.media_volume_up)
                        keyboard.release(Key.media_volume_up)
                    return getAnswer("SVolumen")
            else:
                chat_bot(data)
        elif "baja" in data:
            if "volumen" in data:
                if 'minimo' in data: 
                    mute()
                    return getAnswer("BVolumen") + " al Minimo"
                else:
                    for i in range(5):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                    return getAnswer("BVolumen")
                    
            else:
                return chat_bot(data)

        elif data == "salir":
            talk(getAnswer("Salir"))
            close()


        else:
            return chat_bot(data)
        
    except KeyboardInterrupt:
        log("GOD", "CLOSE")
        close()
    except Exception as e:
        log("BAD", "ERROR: " + type(e).__name__)
        print("A ocurrido el siguiente error: " + type(e).__name__)



def FilterT(textD:str):
    with open(pathdirEVA + '\\config\\lang.json', 'r') as LFile:
        lang = json.load(LFile)
    lang = lang['select']['Lang']
    lang = str(lang).lower()
    
    data = text_mode(textD)
    if lang == 'ES':
        return data
    else:
        return translator.translate(data, dest=lang).text
        
    

#====================================RUN====================================



if __name__ == '__main__':
    data = input("-> ")
    text_mode(data)
    