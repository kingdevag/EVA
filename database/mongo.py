import start
import os
from pymongo import MongoClient
import tkinter.messagebox
import json

start.loadInterF()
if os.path.isdir(f"C:\\Users\\{os.getlogin()}\\Documents\\Eva"):
    pathdirEVA = f"C:\\Users\\{os.getlogin()}\\Documents\\Eva"
else:
    pathdirEVA = os.getcwd()
with open(pathdirEVA + '\\config\\lang.json', 'r') as LFile:
    lang = json.load(LFile)
lang = lang['select']['Lang']
lang = str(lang).upper()

try:
    certpath = str(os.getcwd() + "\\cert\\X509-cert-203953579210535410.pem")
    uri = "mongodb+srv://evadb.knv6g.mongodb.net/EvaDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    client = MongoClient(uri,
                        tls=True,
                        tlsCertificateKeyFile=certpath)
    db = client['EvaDB']
except:
    if lang == "es":
        tkinter.messagebox.showerror(title="ERROR", message="No se a podido conectar con la base \n de datos, Comprueba tu conexion \n a internet o vuelve a intentarlo \n mas tarde.")
    else:
        tkinter.messagebox.showerror(title="ERROR", message="Could not connect to the database,\n please check your internet \n connection or try again later.")
        