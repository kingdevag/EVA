#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import
import os
import random
import threading
import json
import openai
import subprocess
import sys
import pyautogui
import colorama
import pyttsx3
import time
import speech_recognition as sr
import pyjokes
import wikipedia
import pywhatkit
import webbrowser
import sqlite3 as sql
import modules.whatsapp as whapp

#From-Import
from tkinter import *
from config import config
from googletrans import Translator
from datetime import datetime
from pynput.keyboard import Key, Controller

IA_Name = "E.V.A".upper()
name = "eva".lower()
version = "1.0.0"
i = 1
h = 1

engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('volume',1.0)
openai.api_key = config.openaikey
translator = Translator()
keyboard = Controller()
root = os.path.abspath(os.getcwd()).replace('\\', '/')

def default_mode():
    text_mode()

#====================================FUNCTIONS====================================


def getroot():
    return str(os.getcwd())

def debug():
    if os.path.isfile(getroot() + "\\start.config"):
        file = open(getroot() + '\\start.config', 'r+')
        text = file.read()
        if text[1] == 'mode=debug':
            debg = "True"
        else:
            debg = "False"
    else:
        debg = "False"
    return debg

def log(status:str, title:str):
    if os.path.isfile(getroot() + "\\log\\logs.log"):
        file = open(getroot() + "\\log\\logs.log", 'r+')
        text = file.read()
        file.close()
        file = open(getroot() + "\\log\\logs.log", 'w+')
        time = str(datetime.today().strftime('%Y-%m-%d') + " - " + datetime.now().strftime("%H:%M:%S"))
        file.write(str(text + "\n" + "\n" + "#" + "TIME: " + time + "   #" + "EVENT: " + title.lower() + "\n" + "STATUS: " + status.lower()))
        file.close()
    if os.path.isfile(getroot() + "\\log\\logs.log") == False:
        file = open(getroot() + "\\log\\logs.log", 'w')
        time = str(datetime.today().strftime('%Y-%m-%d') + " - " + datetime.now().strftime("%H:%M:%S"))
        file.write(str("\n" + "#" + "TIME: " + time + "   #" + "EVENT: " + title.lower() + "\n" + "STATUS: " + status.lower()))
        file.close()


def talk(text:str):
    print(text)
    text = text.replace('"', '')
    text = text.lower()
    if text.startswith(name):
        text = text.replace(name, '')
    engine.say(text)
    engine.runAndWait()


def close():
    print("\n")
    print(colorama.Fore.RED + "Saliendo" + colorama.Style.RESET_ALL)
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


#====================================DATABASE====================================
    

def add_db():
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    conn.commit()
    conn.close()

def create_table_db():
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE dates (
            name text,
            date text
        )"""
    )
    conn.commit()
    conn.close()

def insert_db(name_dates, text):
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO dates VALUES ('{name_dates}', '{text}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def read_db():
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM dates"
    cursor.execute(instruction)
    dates = cursor.fetchall()
    conn.commit()
    conn.close()
    return dates

def insert_more_db(list):
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO dates VALUES (?, ?)"
    cursor.executemany(instruction, list)
    conn.commit()
    conn.close()

def search_db(name_db):
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM dates WHERE name like '{name_db}%'"
    cursor.execute(instruction)
    dates = cursor.fetchall()
    conn.commit()
    conn.close()
    return dates

def update_db(name_db, date_db):
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    cursor = conn.cursor()
    instruction = f"UPDATE dates SET date='{date_db}' WHERE name like '{name_db}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def delete_table_db(name_db):
    conn = sql.connect(getroot() + "\\databases\\dates.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM dates WHERE name='{name_db}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


#====================================CHAT-BOT====================================


def chat_bot(data):
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "
                
    text = translator.translate(data)

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"The following is a conversation with an {name} assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\n{name}: I am an AI created by OpenAI and KingAG. How can I help you today?\nHuman: " + text.text,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", f" {name}:"]
    )
    answer = translator.translate(response['choices'][0]['text'], dest='es')
    answer = answer.text
    return str(answer)
    

#====================================TEXT====================================


def text_mode(text):
    while True:
        try:
            data = str(text)
            data = data.lower().replace(name, '')

            if data == "":
                pass

            elif data.replace('?', '') == "como te llamas":
                return random.choice(["Me llamo " + name, 'Mi nombre es ' + name, 'Soy ' + name, 'Soy ' +  name + ' Un gusto conozerte', 'Yo soy ' + name + ', Y tu?'])
            elif data.replace('?', '') == "quien eres":
                return random.choice(["Me llamo " + name, 'Mi nombre es ' + name, 'Soy ' + name, 'Soy ' +  name + ' Un gusto conozerte', 'Yo soy ' + name + ', Y tu?'])
            elif data.replace('?', '') == "cual es tu nombre":
                return random.choice(["Me llamo " + name, 'Mi nombre es ' + name, 'Soy ' + name, 'Soy ' +  name + ' Un gusto conozerte', 'Yo soy ' + name + ', Y tu?'])

            elif "chiste" in data:
                langs = ['es', 'IA', 'en']
                lang = str(random.choice(langs))
                if lang == 'IA':
                    chat_bot(data)
                else:
                    joke = pyjokes.pyjokes.get_joke(lang)
                    if lang == 'en':
                        joke = translator.translate(joke, dest='es')
                        return joke.text
                    else:
                        return joke

            elif "reproduce" in data:
                video = data.lower().replace('reproduce', '')
                pywhatkit.playonyt(video)
                return "Reproduciendo " + video
            
            elif "captura de pantalla" in data:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                return "Tomando captura de pantalla"

            elif "screenshot" in data:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                return "Tomando captura de pantalla"

            elif "busca" in data:
                if "wikipedia" in data:
                    order = data.replace('busca', '').replace('en wikipedia' '')
                    order = str(order).replace('wikipedia', '')
                    wikipedia.set_lang("es")
                    info = wikipedia.summary(order, 1)
                    return info
                else:
                    search = str(data.replace('busca', ''))
                    pywhatkit.search(search)
                    return "Buscando" + search
            elif 'hora' in data:
                hora = datetime.datetime.now().strftime('%I:%M %p')
                return "Son las " + str(hora)

            elif 'envia' in data:
                if 'mensaje' in data:
                    contact = data.lower()
                    contact = str(contact).replace('envia', '').replace('mensaje', '')
                    contact = str(contact).replace('manda', '')
                    if contact.startswith('un'):
                        contact = contact.replace('un', '')
                    if contact.startswith('a'):
                        contact = contact.replace('a', '')
                    else:
                        return f"Buscando a " + contact
                        search_contact = search_db(contact)
                        if str(search_contact).replace('[', '').replace(']', '') == '':
                            return "No encontre a " + contact + ", Quieres agreagar su numero a la base de datos?"
                            data = input(colorama.Fore.YELLOW + "-> " + colorama.Style.RESET_ALL)
                            if 'si' in data:
                                return "Escribe su numero por favor"
                                num = input(colorama.Fore.GREEN + "-> " + colorama.Style.RESET_ALL)
                                insert_db(contact.replace(' ', ''), num)
                                return "Agregando a " + num + " Como " + contact
                            if 'esta bien' in data:
                                return "Escribe su numero por favor"
                                num = input(colorama.Fore.GREEN + "-> " + colorama.Style.RESET_ALL)
                                insert_db(contact, num)
                                return "Agregando a " + num + " Como " + contact
                            else:
                                pass 
                        else:
                            num = search_contact[0][1]
                            contact = search_contact[0][0]
                            return "Que mensaje quieres enviar?"
                            msg = input(colorama.Fore.YELLOW + "-> " + colorama.Style.RESET_ALL)
                            return "mandando mensaje a " + str(contact)
                            whapp.send(num, msg)
                            return "mandando mensaje a " + str(contact)
                else:
                    return chat_bot(data)
            elif 'manda' in data:
                if 'mensaje' in data:
                    pass
                else:
                    return chat_bot(data)

            elif 'abre' in data:
                app = data.replace('abre', '')
                if app.__contains__('calculadora'):
                    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                    return "Abriendo Calculadora"
                elif app.__contains__('facebook'):
                    webbrowser.open("https://www.facebook.com")
                    return "Abriendo Faebook"
                elif app.__contains__("github"):
                    webbrowser.open("https://github.com")
                    return "Abriendo GitHub"
                elif app.__contains__("youtube"):
                    webbrowser.open("https://youtube.com")
                    return "Abriendo Youtube"
                elif app.__contains__("whatsapp"):
                    webbrowser.open("https://web.whatsapp.com")
                    return "Abriendo Whatsapp"
                elif app.__contains__("cmd"):
                    subprocess.Popen('C:\\Windows\\System32\\cmd.exe')
                    return "Abriendo simbolo del sistema"
                elif app.__contains__("word"):
                    subprocess.Popen('C:\\Windows\\System32\\write.exe')
                    return "Abriendo Word"
                elif app.__contains__("wordpad"):
                    subprocess.Popen('C:\\Windows\\System32\\write.exe')
                    return "Abriendo Word"
                elif app.__contains__("paint"):
                    subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
                    return "Abriendo Paint"

            elif "sube" in data:
                if "volumen" in data:
                    if 'todo' in data: 
                        full()
                        return "Subiendo Volumen al Maximo"
                    else:
                        for i in range(5):
                            keyboard.press(Key.media_volume_up)
                            keyboard.release(Key.media_volume_up)
                        return "Subiendo Volumen"
                else:
                    chat_bot(data)
            elif "baja" in data:
                if "volumen" in data:
                    if 'minimo' in data: 
                        mute()
                        return "Bajando volumen al Minimo"
                    else:
                        for i in range(5):
                            keyboard.press(Key.media_volume_down)
                            keyboard.release(Key.media_volume_down)
                        return "Bajando volumen"
                        
                else:
                    return chat_bot(data)

            elif data == "cierrate":
                close()
            elif data == "apagate":
                close()
            elif data == "adios":
                talk("Adios...")
                close()


            else:
                return chat_bot(data)
            break
        
        except KeyboardInterrupt:
            log("GOD", "CLOSE")
            close()
        except Exception as e:
            log("BAD", "ERROR: " + type(e).__name__)
            if debug() == "True":
                print(colorama.Fore.RED + "A ocurrido el siguiente error: " + colorama.Style.RESET_ALL + type(e).__name__)
            else:
                pass


#===================================SOUND====================================


def sound_mode():
    try:
        text = ""
    except:
        pass


#====================================CHECKFILES====================================

def checkfiles():
    if os.path.isfile(getroot() + "\\databases\\dates.db"):
        pass
    else:
        add_db()
        create_table_db()

def run():
    if os.path.isfile(getroot() + "\\start.config"):
        file = open(getroot() + '\\start.config', 'r+')
        text = file.read()
        if text[0] == "type=run":
            default_mode()
        elif text[0] == "type=sound":
            sound_mode()
        elif text[0] == "type=text":
            text_mode()
        elif text[0] == "type=thread":
            thread_mode()
        else:
            text_mode()
        file.close()
    else:
        text_mode()
#====================================RUN====================================


def thread_mode():
    t0 = threading.Thread(target=sound_mode)
    t1 = threading.Thread(target=text_mode)

    t0.start()
    t1.start()

    if h != 0:
        t0.join()
        t1.join()

if __name__ == '__main__':
    checkfiles()
    talk(f"Hola soy {name} tu Asistente Virtual con IA, En que puedo ayudarte?.")
    log("GOD", "START")
    run()