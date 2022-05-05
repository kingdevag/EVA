import time
import tkinter as tk
import tkinter.messagebox as msgbox
from PIL import ImageTk, Image
import os
import threading
import json
import requests

pathdirEVA = f"C:\\Users\\{os.getlogin()}\\Documents\\Eva"


def Window():
    root = tk.Tk()
    a = ImageTk.PhotoImage(Image.open(os.getcwd() + "\\resources\\logoShadow.png").resize((200, 200), Image.ANTIALIAS))
    label = tk.Label( root, image=a, bg='black')
            
    marco = True
    iconGui = os.getcwd() + '\\resources\\icon.ico'
    root.geometry('400x400')
    root.title("Loading...")

    root.attributes('-alpha',1.0)

    root.overrideredirect(marco)
    root.lift()
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "black")

    pantall_ancho = root.winfo_screenwidth()
    pantall_largo = root.winfo_screenheight()


    label.place(x=0,y=0,relwidth=1, relheight=1)
    x = int((pantall_ancho/2) - (400/2))
    y = int((pantall_largo/2) - (400/2))
    root.geometry(f"{400}x{400}+{x}+{y}")
    root.iconbitmap(iconGui)


    def OcultarVentana():
        root.withdraw()
        if os.path.isfile(pathdirEVA + "\\complete.eva"):
            os.remove(pathdirEVA + "\\complete.eva")
            try:
                root.destroy()
            except:
                pass
        else:
            root.destroy()
            time.sleep(1)
            if t1.is_alive():
                time.sleep(1)
                try:
                    root.destroy()
                except:
                    pass
            else:
                try:
                    root.destroy()
                except:
                    pass
            
        


    root.after(1350, OcultarVentana)
    root.mainloop()
    
    
def loadInterF():
    if os.path.isdir(pathdirEVA):
        pass
    else:
        os.mkdir(pathdirEVA)
    if os.path.isdir(pathdirEVA + "\\config"):
        pass
    else:
        os.mkdir(pathdirEVA + "\\config")
    if os.path.isfile(pathdirEVA + "\\config\\lang.json"):
        pass
    else:
        with open(pathdirEVA + "\\config\\lang.json", "w")as JXDF:
            xdd = """{
    "select": {
        "Lang": "es"
    }
}"""
            JXDF.write(xdd)
    if os.path.isdir(pathdirEVA + "\\log"):
        pass
    else:
        os.mkdir(pathdirEVA + "\\log")
        
    if os.path.isfile(pathdirEVA + "\\prompt.txt"):
        pass
    else:
        f = open(pathdirEVA + "\\prompt.txt", mode="w", encoding="utf-8")
        f.write("The following is a conversation with an Eva assistant. The assistant is helpful, creative, clever, and very friendly. \n \n Human: Hello, who are you? \n Eva: I am an AI created by OpenAI and KingAG. How can I help you today? \n Human: Hello \n Eva: Hello! \n Human: ")
        f.close()
    if os.path.isdir(f"C:\\Users\\{os.getlogin()}\\Documents\\Eva"):
        pass
    else:
        os.mkdir(f"C:\\Users\\{os.getlogin()}\\Documents\\Eva")
    if os.path.isfile(f"C:\\Users\\{os.getlogin()}\\Documents\\Eva\\path.eva"):
        pass
    else:
        with open(f"C:\\Users\\{os.getlogin()}\\Documents\\Eva\\path.eva", mode="w", encoding="utf-8") as fP:
            fP.write("{}".format(os.getcwd()))
    try:
        request = requests.get("https://www.google.com", timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        red = False
    else:
        red = True
    if red == True:
        pass
    else:
        with open(pathdirEVA + '\\config\\lang.json', 'r') as LFile:
            lang = json.load(LFile)
            lang = lang['select']['Lang']
            lang = str(lang)
        if lang.lower() == 'es':
            msgbox.showwarning(title="Warning!", message="Sin conexion a internet! :( \n Puede que algunas funciones de EVA no funcionen \n correctamente sin conexion a internet.")
        else:
            msgbox.showwarning(title="Warning!", message="No internet connection! :( \n Some features of EVA may not work properly \n without internet connection.")
    



t0 = threading.Thread(name="WindowLoading", target=Window , args=())
t1 = threading.Thread(name="FunctionsLoading", target=loadInterF , args=())
    
    
def load():
    t1.start()
    t0.run()
    t1.join()
    
if __name__ == '__main__':
    load()