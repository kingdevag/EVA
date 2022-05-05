#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import sys

from colorama import init, Style, Fore

try:
    init()

    title = """

    █▀▀ ░ █░█ ░ ▄▀█   ▄▄   █▀█ █▀▀ █▀▄▀█ █▀█ ▀█▀ █▀▀   █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄
    ██▄ ▄ ▀▄▀ ▄ █▀█   ░░   █▀▄ ██▄ █░▀░█ █▄█ ░█░ ██▄   █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀
    """


    def name():
        os.system("cls")
        print(Fore.LIGHTCYAN_EX + title + Style.RESET_ALL)

    name()

    print(Fore.RED + "EMPEZANDO DESCARGA EN..." + "5")
    time.sleep(1)
    name()
    print(Fore.RED + "EMPEZANDO DESCARGA EN..." + "4")
    time.sleep(1)
    name()
    print(Fore.RED + "EMPEZANDO DESCARGA EN..." + "3")
    time.sleep(1)
    name()
    print(Fore.RED + "EMPEZANDO DESCARGA EN..." + "2")
    time.sleep(1)
    name()
    print(Fore.RED + "EMPEZANDO DESCARGA EN..." + "1")
    time.sleep(1)
    name()

    print(Fore.GREEN + "DESCARGANDO..." + Style.RESET_ALL)
    time.sleep(1)
    def gitdownload():
        c = os.system("git --version")
        if c == 1:
            print(Fore.RED + "Se nesesita instalar Git para la instalacion." + Style.RESET_ALL)
        else:
            os.system("cd " + os.getcwd())
            os.system("git clone https://github.com/kingdevag/Eva_V.A.git")
    gitdownload()

    def downloadF():
        os.system("cls")
        downloadTITLE = """

        █▀▄ █▀▀ █▀ █▀▀ ▄▀█ █▀█ █▀▀ ▄▀█
        █▄▀ ██▄ ▄█ █▄▄ █▀█ █▀▄ █▄█ █▀█

        █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ ▄▀█
        █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ █▀█
        """

        print(Fore.GREEN + downloadTITLE + Style.RESET_ALL)

    downloadF()

    print(Fore.RED + "Saliendo en..." + "10")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "9")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "8")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "7")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "6")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "5")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "4")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "3")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "2")
    time.sleep(1)
    downloadF()
    print(Fore.RED + "Saliendo en..." + "1")
    time.sleep(1)
    downloadF()
    time.sleep(1)
    sys.exit

except KeyboardInterrupt:
    print(Fore.RED + "Saliendo" + Style.RESET_ALL)
    time.sleep(1)
    sys.exit()
except Exception as e:
    print(type(e).__name__)
    
