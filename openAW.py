import os
import subprocess
import webbrowser


def openApp(app:str):
    if app.__contains__('calculadora'):
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        return "Calculadora"
    elif app.__contains__("cmd"):
        subprocess.Popen('C:\\Windows\\System32\\cmd.exe')
        return "Simbolo del sistema"
    elif app.__contains__("Simbolo del sistema"):
        subprocess.Popen('C:\\Windows\\System32\\cmd.exe')
        return "Simbolo del sistema"
    elif app.__contains__("word"):
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        return  "Word"
    elif app.__contains__("wordpad"):
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        return "Word"
    elif app.__contains__("paint"):
        subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
        return "Paint"
    
    
#######################---APP-WEB---#######################
    
    elif app.__contains__("discord"):
        if os.path.isfile("C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe"):
            subprocess.Popen(str("C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe"))
            return "Discord"
        else:
            webbrowser.open("https://discord.com")
            return "Discord"
            
    
#########################---WEB---#########################
    
    elif app.__contains__('facebook'):
        webbrowser.open("https://www.facebook.com")
        return "Faebook"
    elif app.__contains__("github"):
        webbrowser.open("https://github.com")
        return "GitHub"
    elif app.__contains__("youtube"):
        webbrowser.open("https://youtube.com")
        return "Youtube"
    elif app.__contains__("whatsapp"):
        webbrowser.open("https://web.whatsapp.com")
        return "Whatsapp"
    else:
        return "NOT APP"
            
if __name__ == '__main__':
    print(openApp(""))
    