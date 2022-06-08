import requests
from bs4 import BeautifulSoup
import random
import webbrowser
import csv
from art import *
import os
import platform
from urllib.request import urlopen
import warnings


warnings.filterwarnings("ignore")

class Color:
    no_colored = "\033[0m"
    white_bold = "\033[1;37m"
    blue_bold = "\033[34m"
    cyan_bold = "\033[1;96m"
    green_bold = "\033[1;92m"
    red_bold = "\033[1;91m"
    yellow_bold = "\033[1;33m"
    orange_bold = "\033[33m"
    purple_bold = "\033[35m"
    pink_bold="\033[95m"
    grey_bold="\033[90m"
    internet = False

# verification de la connextion
def is_internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        Color.internet = True
    except:
        Color.internet = False

def Clear():
    if platform.system() == "Linux":
        os.system("clear") 
    elif platform.system() == "Window":
        os.system("cls")

def Banner():
    Clear()
    print(Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""╭━━━╮"""+Color.purple_bold+"""╱╱╱╱╱╱╱"""+Color.yellow_bold+"""╭╮"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""╭╮
"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""┃╭━╮┃"""+Color.purple_bold+"""╱╱╱╱╱╱╱"""+Color.yellow_bold+"""┃┃"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""┃┃
"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""┃┃"""+Color.purple_bold+"""╱"""+Color.yellow_bold+"""╰╋━┳━━┳━━┫┃╭┳━━┳╮╭┳━╮┃┃"""+Color.purple_bold+"""╱╱"""+Color.yellow_bold+"""╭╮╭┳━━┳┳━╮
"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""┃┃"""+Color.purple_bold+"""╱"""+Color.yellow_bold+"""╭┫╭┫╭╮┃╭━┫╰╯┫┃━┫┃┃┃╭╯┃┃"""+Color.purple_bold+"""╱"""+Color.yellow_bold+"""╭┫┃┃┃╭╮┣┫╭╮╮
"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""┃╰━╯┃┃┃╭╮┃╰━┫╭╮┫┃━┫╰╯┃┃"""+Color.purple_bold+"""╱"""+Color.yellow_bold+"""┃╰━╯┃╰╯┃╰╯┃┃┃┃┃
"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""╰━━━┻╯╰╯╰┻━━┻╯╰┻━━┻━━┻╯"""+Color.purple_bold+"""╱"""+Color.yellow_bold+"""╰━━━┻━━┫╭━┻┻╯╰╯
"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""┃┃
"""+Color.purple_bold+"""╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱"""+Color.yellow_bold+"""╰╯
    """)


def start():
    cores = []
    res=[]
    print(Color.grey_bold+" Exemple : <Salut les gens> ==> <_a_u_ _e_ _e__>")
    phrase = input(Color.white_bold+" ["+Color.cyan_bold+"?"+Color.white_bold+"] Phrase à décode. "+Color.blue_bold)

    # verification de la connexion
    is_internet()
    phraseCode = phrase.split(" ")
    print(Color.white_bold+" ["+Color.green_bold+"*"+Color.white_bold+"] Colection des mots pouvant matcher ...")
    for mot in phraseCode:
        # On test les caractères entré
        testMot = True
        for lettre in mot:
            voyelle = ["a","e","u","o","i","y"]
            testLettre = False
            for voy in voyelle:
                if (voy == lettre) or (lettre == "_"):
                    testLettre = True
            if testLettre == False:
                testMot = False
        if testMot:
            if Color.internet:
                cores.append(Recolte_Web(mot))
            else:
                cores.append(recolte(mot))
        else:
            print(Color.white_bold+" ["+Color.red_bold+"!"+Color.white_bold+"] Carractère incorecte")
            fin = input("")
            return False
        print(Color.white_bold+" ["+Color.green_bold+"*"+Color.white_bold+"] Construction du tableau de possibilité ...")
        #Ici on écrit d'abord les mot de la phrase coder
        c= csv.writer(open("resultat.csv", "w+"))
        c.writerow(phraseCode)
        # On cherche la suite la plus longue
        Num = 0
        for Liste in cores:
            if len(Liste) > Num:
                Num = len(Liste)
        
        for i in range(Num):
            Ligne = []
            for élément in cores:
                élément = élément.split(",")
                try:
                    Ligne.append(élément[i])
                except:
                    Ligne.append("")
            c.writerow(Ligne)
        
        print(Color.white_bold+" ["+Color.red_bold+"+"+Color.white_bold+"] "+Color.green_bold+"Résultats écrit dans resultat.csv")

def recolte(mots):
    inte = 0
    liste = ""
    erreur = True
    data = open("data.txt","r",encoding="utf-8")
    FData = data.read()
    FData = FData.split("\n")

    for MotData in FData:
        MotData = MotData.lower()
        MotData = MotData.replace("'","")
        MotData = MotData.replace("-","")
        MotData = MotData.replace("œ","oe")
        MotData = MotData.replace("æ","ae")
        #On prends que les mots de même longeur que celui à tester
        if len(MotData) == len(mots):
            #On teste si les voyelle du motData est en correspondance avec le mot à teste
            i=-1
            Voyelle = ["a","e","u","o","i","y","é","ê","è","à","â","ä","ë","ù","û","ô","ö","ü","î","ï"]
            TestAddMot = True
            for LetData in MotData:
                i+=1
                if (mots[i] == "_" and LetData not in Voyelle) or (mots[i] in Voyelle and LetData == mots[i]):
                    pass
                else:
                    TestAddMot = False
            if TestAddMot:
                liste += str(MotData)+","
    return liste[0:-1]        

def Recolte_Web(mots):

    inte = 0
    liste = ""
    erreur = True
    while erreur == True:
        inte+=1
        url ="https://www.motsavec.fr/"+mots+"/"+str(inte)
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text)
            divs = soup.findAll('li')
            if len(divs) <= 6:
                erreur = False
                break
            i = 0
            for div in divs:
                i+=1
                mot = div.find('a')
                try:
                    caracBan = ["«","»","1","2","3","4","5","6","7","8","9","10","…","12","13","14","15","16","17","18","19"]
                    stop = True
                    for cara in caracBan:
                        if mot.string.strip() in cara or cara in mot.string.strip():
                            stop = False
                    
                    if stop:

                        # On prends que les mots qui n'ont pas d'autre voyelle
                        motWeb = str(mot.string.strip())
                        motWeb = motWeb.lower()
                        motWeb = motWeb.replace("'","")
                        motWeb = motWeb.replace("-","")
                        motWeb = motWeb.replace("œ","oe")
                        motWeb = motWeb.replace("æ","ae")
                        add = True
                        for i in range(len(motWeb)):
                            if mots[i] == "_":
                                ListeVoyelle = ["a","e","u","o","i","y","é","ê","è","à","â","ä","ë","ù","û","ô","ö","ü","î","ï"]
                                for voyelle in ListeVoyelle:
                                    if voyelle == motWeb[i]:
                                        add = False
                        if add:        
                            liste = liste + str(mot.string.strip()) +","

                except:
                   lol = "lol"
    return liste[0:-1]

Banner()
start()