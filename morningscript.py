import os
import random
import time
import webbrowser
import requests
from colorama import init, Fore, Back, Style
import keyboard
import sys
import pygame
import Toolbox
import math
userdata = ["", "", ""]
apikey = "e91d81d114cb8742d01f3f74cda18d27"
class Main():
    def __init__(self):
        print("Starting...")
        self.bgm = pygame.mixer.Sound(Toolbox.PythonTools.loadfile("clairdelune.mp3"))
        self.running = True
        self.choice = ""
        print("Started")
        functions.clearscreen()
        self.main()
    def main(self):
        self.bgm.play(-1)
        while self.running:
            if self.choice == "" or self.choice == False:
                timeh = int(time.strftime("%#H")) if os.name == "nt" else int(time.strftime("%-H"))
                if timeh >= 4 and timeh < 11:
                    welcometext = "Good morning "
                elif timeh >= 11 and timeh < 18:
                    welcometext = "Good afternoon "
                elif timeh >= 18 and timeh < 24 or timeh >= 0 and timeh < 4:
                    welcometext = "Hello "
                print(welcometext + str(userdata[0].decode("utf-8", "strict"))[:len(str(userdata[0].decode("utf-8", "strict")))-1] + "!")
                functions.printoptions()
                self.choice = input("What would you like to do?\n")
                functions.clearscreen()
                if self.choice.isnumeric() or self.choice == "secondthoughts2" or self.choice == "Sky" or self.choice == "sky" or self.choice == "Field" or self.choice == "field" or self.choice == "Ocean" or self.choice == "ocean":
                    continue
                else:
                    self.choice = ""
            elif self.choice == "1":
                timeold = ""
                while not keyboard.is_pressed("esc"):
                    curtime = Toolbox.PythonTools.gettime()
                    if not timeold == curtime:
                        timeold = curtime
                        functions.clearscreen()
                        print("The time is " + timeold + "\nPress 'esc' to exit")
            elif self.choice == "2":
                dateold = ""
                while not keyboard.is_pressed("esc"):
                    curdate = Toolbox.PythonTools.getdate()
                    if not dateold == curdate:
                        dateold = curdate
                        functions.clearscreen()
                        print("The date is " + dateold + "\nPress 'esc' to exit")
            elif self.choice == "3":
                newwetloc = input("What would you like to set it to?\nExtra Options: Autofill\n") + "\n"
                if newwetloc == "autofill" or newwetloc == "Autofill":
                    ip = Toolbox.PythonTools.getip()
                    newwetloc = Toolbox.PythonTools.getcity(ip) + "\n"
                newwetlocutf8 = newwetloc.encode("utf-8", "strict")
                userdata[1] = newwetlocutf8
                with open("info/userdata.arry", "wb") as udf:
                    udf.writelines(userdata)
                    udf.close()
            elif self.choice == "4":
                curwetloc = str(userdata[1].decode("utf-8", "strict"))[:len(str(userdata[1].decode("utf-8", "strict")))-1]
                wetold = ""
                while not keyboard.is_pressed("esc"):
                    curwet = Toolbox.PythonTools.getweather(curwetloc, apikey)
                    if not wetold == curwet:
                        wetold = curwet
                        functions.clearscreen()
                        for text in curwet:
                            print(text)
                        print("Press 'esc' to exit")
            elif self.choice == "5":
                newname = input("What would you like to change it to?\n") + "\n"
                newnameutf8 = newname.encode("utf-8", "strict")
                userdata[0] = newnameutf8
                with open("info/userdata.arry", "wb") as udf:
                    udf.writelines(userdata)
                    udf.close()
            elif self.choice == "6":
                print("This program was last run " + str(userdata[2].decode("utf-8", "strict"))[:len(str(userdata[2].decode("utf-8", "strict")))-1] + "\nPress 'esc' to exit")
                while not keyboard.is_pressed("esc"):
                    continue
            elif self.choice == "7":
                search = input("What page would you like to visit?\n")
                search = search.replace(" ", "_")
                search = search.capitalize()
                url = "https://en.wikipedia.org/wiki/" + search
                response = requests.get(url)
                response = response.content.decode()
                data = response[response.rfind("headline"):response.rfind("headline")+(len(response)-response.rfind("headline"))]
                data = data[11:data.find("</script>")-2]
                if not data == False and not data == "":
                    data = "'" + data.capitalize() + "'"
                    print(data)
                else:
                    print("We couldn't find anything to show you. If you think this is a bug, consider reporting it.\ngithub.com/Techpotato1/Python-Morning-Script")
                openpage = input("Do you want to open the wikipedia page in your browser?\n")
                if openpage == "yes" or openpage == "Yes":
                    webbrowser.open(url)
                else:
                    pass
            elif self.choice == "8":
                url = input("What url do you want to open?\n")
                webbrowser.open(url)
            elif self.choice == "9":
                lower = input("What is the minimum?")
                upper = input("What is the maximum?")
                try:
                    if lower.isnumeric and upper.isnumeric:
                        lower = int(lower)
                        upper = int(upper)
                        if lower < upper:
                            rint = random.randint(lower, upper)
                        elif upper > lower:
                            rint = random.randint(upper, lower)
                        elif lower == upper:
                            rint = lower
                        else:
                            rint = "There was an error"
                    else:
                        rint = "Couldn't find a number. Please input the numbers in numeric form"
                except:
                    rint = "There was an error"
                print(str(rint) + "\nPress 'esc' to exit")
                while not keyboard.is_pressed("esc"):
                    continue
            elif self.choice == "10":
                print(str(math.pi) + "\nPress 'esc' to exit")
                while not keyboard.is_pressed("esc"):
                    continue
            elif self.choice == "11":
                exitc = input("Are you sure?\nType 'exit' to exit.\nType anything else to continue\n")
                if exitc == "Exit" or exitc == "exit":
                    print("Goodbye")
                    self.running = False
                    sys.exit()
            elif self.choice == "12":
                consent = input("Are you sure?\n")
                if consent == "yes" or consent == "Yes":
                    print(Toolbox.PythonTools.getip() + "\nPress 'esc' to exit")
                    while not keyboard.is_pressed("esc"):
                        continue
            elif self.choice == "13":
                confirm = input("Are you sure?\n")
                if confirm == "yes" or confirm == "Yes":
                    try:
                        print("Deleting all saved info...")
                        os.remove(os.getcwd() + "/info")
                        print("Done")
                    except:
                        print("Error")
            self.choice = ""
            functions.clearscreen()
class functions():
    FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
    BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]
    def clearscreen():
        os.system('cls' if os.name == 'nt' else 'clear')
    def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
        print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)
    def printoptions():
        print("""
Main Options:
1. Check the time
2. Check the date
3. Change the weather location
4. Check the weather
5. Change your name
6. Check the time that the program was last run
7. Search Wikipedia
8. Open a URL
9. Generate a random number
10. Calculate PI
11. Exit

Personal Options:
12. Print your public IP address
13. Delete all saved info

Credits:
Coding - Techpotato and Iam
Music - Moura Lympany, Claude Debussy - Clair de Lune
""")
if __name__ == "__main__":
    try:
        os.mkdir("info")
    except FileExistsError:
        pass
    if os.path.exists("info/userdata.arry"):
        with open("info/userdata.arry", "rb") as udf:
            userdata = udf.readlines()
            udf.close()
        curdt = Toolbox.PythonTools.gettime() + " - " + Toolbox.PythonTools.getdate() + "\n"
        curdtutf8 = curdt.encode("utf-8", "strict")
        userdata[2] = curdtutf8
        with open("info/userdata.arry", "wb") as udf:
            udf.writelines(userdata)
            udf.close()
    else:
        name = input("What is your name?\n") + "\n"
        nameutf8 = name.encode("utf-8", "strict")
        wetloc = input("Where do you live?\nExtra Options: Autofill, Skip\n")
        if wetloc == "autofill" or wetloc == "Autofill":
            ip = Toolbox.PythonTools.getip()
            wetloc = Toolbox.PythonTools.getcity(ip) + "\n"
        if wetloc == "skip" or wetloc == "Skip":
            wetloc = "null\n"
        wetlocutf8 = wetloc.encode("utf-8", "strict")
        curdt = Toolbox.PythonTools.gettime() + " - " + Toolbox.PythonTools.getdate() + "\n"
        curdtutf8 = curdt.encode("utf-8", "strict")
        userdata[0] = nameutf8
        userdata[1] = wetlocutf8
        userdata[2] = curdtutf8
        print(userdata)
        with open("info/userdata.arry", "wb") as udf:
            udf.writelines(userdata)
            udf.close()
    init()
    pygame.mixer.init()
    Main()