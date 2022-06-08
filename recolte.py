import requests
from bs4 import BeautifulSoup
import webbrowser
import warnings


warnings.filterwarnings("ignore")

liste = []
alpha = "abcdefghijklmnopqrstuvwxyz"
files = open("data.txt", "w+")
for lettre in alpha:
    inte = 0
    print(lettre)
    erreur = True
    while erreur == True:
            inte+=1
            url ="https://motsavec.fr/"+lettre+"*/ordre-alphabetique/"+str(inte)
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
                            motWeb = str(mot.string.strip())
                            motWeb = motWeb.lower()
                            motWeb = motWeb.replace("'","")
                            motWeb = motWeb.replace("-","")
                            motWeb = motWeb.replace("œ","oe")
                            motWeb = motWeb.replace("æ","ae")
                            print(motWeb)
                            files.write(motWeb+"\n")
                    except:
                        lol = ""
files.close()