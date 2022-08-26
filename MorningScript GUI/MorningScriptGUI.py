print("Starting MorningScript GUI...")
import os
import time
import json
import random
import requests
import pygame
from Toolbox import PygameTools
from Toolbox import PythonTools
print("Modules loaded.")
class main():
    screenwidth = 1000
    screenheight = 700
    fontsize = 26
    fps = 24
    def __init__(self):
        print("Starting main...")
        data()
        self.screen = PygameTools.makescreen(self.screenwidth, self.screenheight, "MorningScript GUI", "data/icon.ico")
        self.clock = pygame.time.Clock()
        self.textin = False
        self.bgimageframe = 0
        self.running = True
        self.run()
    def run(self):
        choice = ""
        welcometext = ""
        gotweather = False
        weatherold = []
        gotrand = False
        gotloc = False
        locold = ""
        print("Started main.")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Goodbye")
                    pygame.quit()
                    self.running = False
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        choice = ""
                    else:
                        choice = event.key
            self.screen.fill((135, 185, 205))
            PygameTools.image(self.screen, data.bgimages[self.bgimageframe], 0, 0, self.screenwidth, self.screenheight)
            if self.bgimageframe < len(data.bgimages)-1:
                self.bgimageframe = self.bgimageframe + 1
            else:
                self.bgimageframe = 0
            timeh = int(time.strftime("%#H")) if os.name == "nt" else int(time.strftime("%-H"))
            if timeh >= 4 and timeh < 11:
                welcometext = "Good morning. "
            elif timeh >= 11 and timeh < 18:
                welcometext = "Good afternoon. "
            elif timeh >= 18 and timeh < 24 or timeh >= 0 and timeh < 4:
                welcometext = "Hello. "
            if choice == False or choice == "":
                gotrand = False
                PygameTools.text(data.font, self.screen, welcometext + "What would you like to do?", 0, 0, 255, 255, 255)
                posy = 0 + self.fontsize + 5
                for opt in data.options:
                    PygameTools.text(data.font, self.screen, opt, 0, posy, 255, 255, 255)
                    posy = posy + self.fontsize + 5
            elif choice == pygame.K_1:
                PygameTools.text(data.font, self.screen, "The time is " + PythonTools.gettime(), 0, 0, 255, 255, 255)
            elif choice == pygame.K_2:
                PygameTools.text(data.font, self.screen, "Today is " + PythonTools.getdate(), 0, 0, 255, 255, 255)
            elif choice == pygame.K_3:
                posy = 0
                if not gotweather:
                    PygameTools.text(data.font, self.screen, "Loading weather data...", 0, 0, 255, 255, 255)
                    weather = PythonTools.getweather(PythonTools.getcity(PythonTools.getip()), "e91d81d114cb8742d01f3f74cda18d27")
                    gotweather = True
                elif not weather == weatherold:
                    gotweather = False
                for wetdata in weather:
                    PygameTools.text(data.font, self.screen, wetdata, 0, posy, 255, 255, 255)
                    posy = posy + self.fontsize + 5
                weatherold = weather
            elif choice == pygame.K_4:
                if not gotrand:
                    lower = round(((random.random()+0.1) * 10) * ((random.random()+0.1) * 10))
                    upper = round((((random.random()+0.1) * 10)*lower) * (((random.random()+0.1) * 10)*lower))+lower
                    randnum = str(random.randint(lower, upper))
                    gotrand = True
                PygameTools.text(data.font, self.screen, "RNGesus: " + randnum, 0, 0, 255, 255, 255)
            elif choice == pygame.K_5:
                if not gotloc:
                    ip = PythonTools.getip()
                    response = requests.get("https://geolocation-db.com/jsonp/" + ip)
                    result = response.content.decode()
                    result  = str(json.loads(result.split("(")[1].strip(")")))
                    location = result[result.find("postal")+len("postal")+4:result.find("', 'latitude")] + ", " + result[result.find("city")+len("city")+4:result.find("', 'postal")] + ", " + result[result.find("state")+len("state")+4:result.find("'}")] + ", " + result[result.find("country_name")+len("country_name")+4:result.find("', 'city")]
                    latlong = result[result.find("latitude")+len("latitude")+3:result.find(", 'longitude")] + ", " + result[result.find("longitude")+len("longitude")+3:result.find(", 'IPv4")]
                    gotloc = True
                elif not location == locold:
                    gotloc = False
                PygameTools.text(data.font, self.screen, ip, 0, 0, 255, 255, 255)
                PygameTools.text(data.font, self.screen, location, 0, 0 + self.fontsize + 5, 255, 255, 255)
                PygameTools.text(data.font, self.screen, latlong, 0, 0 + (self.fontsize + 5) * 2, 255, 255, 255)
                locold = location
            elif choice == pygame.K_6:
                print("Goodbye")
                pygame.quit()
                self.running = False
                exit()
            pygame.display.update()
            dt = self.clock.tick(self.fps)
class data():
    print("Starting data...")
    font = PygameTools.loadfont("data/FiraCode.ttf", main.fontsize)
    bgimages = []
    for file in PythonTools.listdir("data/bg"):
        bgimages.append(PygameTools.loadimg("data/bg/" + file))
    options = ["1 - Check the time", "2 - Check the date", "3 - Check the weather", "4 - Contact RNGesus", "5 - Doxx yourself", "6 - Exit"]
    print("Started data.")
if __name__ == "__main__":
    print("Started MorningScript GUI.")
    main()