import subprocess
import os
pathdirEVA = f"C:\\Users\\{os.getlogin()}\\Documents\\Eva"
def openVoiceApp():
     subprocess.Popen(str(os.getcwd() + "\\E.V.A - Voice.exe"))
    
def update():
    if os.path.isfile(str(os.getcwd() + "\\updater.exe")):
        subprocess.Popen(str(os.getcwd() + "\\updater.exe"))
    else:
        subprocess.Popen(str(os.getcwd() + "\\tools\\download\\Eva_Download_Remote.exe"))

def getConfig():
    subprocess.Popen(str(os.getcwd() + "\\E.V.A - Configure.exe"))

def lang(lang:str):
    JStringLang = '''{
    "select": {
        "Lang": "''' + lang + '''"
    }
}'''
    with open(pathdirEVA + "\\config\\lang.json", "w") as File:
        File.write("")
        File.write(JStringLang)
        