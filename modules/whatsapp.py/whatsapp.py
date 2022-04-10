import pyautogui
import webbrowser
import time

def send(contact, message):
    webbrowser.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}")
    time.sleep(24)
    pyautogui.press('enter')
