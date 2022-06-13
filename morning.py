import datetime
import os
import random
import shutil
import time
import webbrowser
import requests
import json
from requests import get
import pyttsx3
from colorama import init, Fore, Back, Style

#Define a function to clear the screen
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#essential for Windows environment
init()
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

#print to the console with color
def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

#print the the options for the user to choose from
def printoptions():
    print("""What would you like to do next? \n
1. Check the time
2. Check the date
3. Change the weather location
4. Check the weather
5. Change your name
6. Exit \n
Developer Options:
7. Delete the userinfo.txt file
8. Delete the timeanddate.txt file
9. Delete the weatherlocation.txt file
10. Clear the screen
11. Delete the info folder
12. List the contents of the current directory
13. Check the time that the program was last run
14. Open a URL
15. Autofill the weather location from IP (Might be buggy)
16. Print your public IP address
17. List the contents of the info folder
18. Save text to speech to a file
19. Delete audio.mp3
20. Generate a random number
\n""")

#a function to get the weather
def getweather():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # City Name 
    CITY = weatherlocation
    # API key API_KEY = "Your API Key"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + "e91d81d114cb8742d01f3f74cda18d27"
    #HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       #convert the temperature to fahrenheit
       temperature = temperature * (9/5) - 459.67
       #round the temperature to 2 decimal places
       temperature = round(temperature, 2)
       print(f"{CITY:-^30}")
       print(f"Temperature: {temperature}")
       print(f"Humidity: {humidity}")
       print(f"Pressure: {pressure}")
       print(f"Weather Report: {report[0]['description']}")
    else:
       # showing the error message
       print_with_color("Error in the HTTP request", color=Fore.RED, brightness=Style.DIM)
       print("Try checking the city name")

#get the aproximate location of the user from their IP address
def getcity(ip_address):
    # URL to send the request to
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
# Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
# Clean the returned string so it just contains the dictionary data for the IP address
    result = result.split("(")[1].strip(")")
# Convert this data into a dictionary
    result  = json.loads(result)
#get the city name from the result
    city = result['city']
    return city

#create a folder in the same directory as the script called "info"
try:
    os.mkdir("info")
except FileExistsError:
    pass

#gets the IP address of the user
ip_address = get('https://api.ipify.org').text
name = ""
choice = ""
weatherlocation = ""
oldtimeanddate = ""
engine = pyttsx3.init()
engine.setProperty('rate', 120)

#Get the contents of the current directory
contentsofdir = os.listdir(os.getcwd())

contentsofinfodir = os.listdir("info")

#format the date nicely
date = datetime.datetime.now()
date = date.strftime("%A %B %d, %Y")

#get the time and format it nicely
def gettime():
    currenttime = datetime.datetime.now()
    currenttime = time.strftime("%I:%M %p")
    return currenttime

#setts the currenttime variable to the current time
currenttime = gettime()

#if userinfo.txt exists, open it and read the name
try:
    with open("info/userinfo.txt", "r") as f:
        name = f.read()
except FileNotFoundError:
    pass

#if weatherlocation.txt exists, open it and read the file
try:
    with open("info/weatherlocation.txt", "r") as f:
        weatherlocation = f.read()
except FileNotFoundError:
    pass

#an unused function to get the last contents of the info folder
try:
    with open("info/currentdir", "r") as f:
        olddircontents = f.read()
except FileNotFoundError:
    pass

#if timeanddate.txt exists, open it and read the file
try:
    with open("info/timeanddate.txt", "r") as f:
        oldtimeanddate = f.read()
except FileNotFoundError:
    pass

#write the time and date to a file called timeanddate.txt
with open("info/timeanddate.txt", "w") as f:
    f.write("Date last run: \n")
    f.write(date)
    f.write("\n")
    f.write(currenttime)

#CLEARS THE SCREEN
clearscreen()

#if there is nothing in name, ask for it
if name == "":
    name = input("What is your name? \n")

#create a file called userinfo.txt and write the name to it
with open("info/userinfo.txt", "w") as file:
    file.write(name)

#get the user's name and greet them
print("Hello, " + name + "!")
print("Today's date is " + date)
print("The time is " + currenttime)

#don't exit the program until the user enters 3
while choice != "6":

    #prints the options for the user to choose from
    printoptions()

    #asks the user to choose an option
    choice = input("Enter your choice: ")
    #clears the screen
    clearscreen()

    #if the user chooses 1, check the time
    if choice == "1" or choice == "time":
        currenttime = gettime()
        print(currenttime)

    #if the user chooses 2, check the date
    elif choice == "2" or choice == "date":
        print(date)

    #if the user chooses 3, get the weather location
    elif choice == "3":
        weatherlocation = input("What is your city? \n")
        with open("info/weatherlocation.txt", "w") as file:
            file.write(weatherlocation)

    #if the user chooses 4, get the weather
    elif choice == "4" or choice == "weather":
        if weatherlocation == "":
            weatherlocation = input("What is your city? \n")
            with open("info/weatherlocation.txt", "w") as file:
                file.write(weatherlocation)
            getweather()
            print("\n")
        else:
            getweather()
            print("\n")

    #if the user chooses 5, get the user's name
    elif choice == "5" or choice == "name":
        name = input("What is your name? \n")
        with open("info/userinfo.txt", "w") as file:
            file.write(name)

    #if the user chooses 6, exit the program
    elif choice == "6" or choice == "exit":
        clearscreen()
        i = input("Press Enter to continue or type cancel to cancel: \n")
        if i == "Cancel" or "cancel" in i:
            print("Canceled\n")
            choice = ""
        else:
            print("Goodbye!")
            time.sleep(0.5)
            exit()

    #if the user chooses 7, delete userinfo.txt
    elif choice == "7" or choice == "delete userinfo":
        try:
            os.remove("info/userinfo.txt")
            print_with_color("Deleting userinfo.txt...", color=Fore.RED, brightness=Style.DIM)
            time.sleep(0.5)
            print_with_color("Done!", color=Fore.GREEN, brightness=Style.DIM)
        except FileNotFoundError:
            print_with_color("Error: userinfo.txt not found", color=Fore.RED, brightness=Style.DIM)

    #if the user chooses 8, delete timeanddate.txt
    elif choice == "8" or choice == "delete timeanddate":
        try:
            os.remove("info/timeanddate.txt")
            print_with_color("Deleting timeanddate.txt...", color=Fore.RED, brightness=Style.DIM)
            time.sleep(0.5)
            print_with_color("Done!", color=Fore.GREEN, brightness=Style.DIM)
        except FileNotFoundError:
            print_with_color("timeanddate.txt does not exist!", color=Fore.RED, brightness=Style.DIM)

    #if the user chooses 9, delete weatherlocation.txt
    elif choice == "9" or choice == "delete weatherlocation":
        try:
            os.remove("info/weatherlocation.txt")
            print_with_color("Deleting weatherlocation.txt...", color=Fore.RED, brightness=Style.DIM)
            time.sleep(0.5)
            print_with_color("Done!", color=Fore.GREEN, brightness=Style.DIM)
        except FileNotFoundError:
            print_with_color("weatherlocation.txt does not exist!", color=Fore.RED, brightness=Style.DIM)

    #if the user chooses 10, clear the screen
    elif choice == "10" or choice == "clear":
        print("Clearing screen...")
        time.sleep(0.5)
        clearscreen()

    #if the user chooses 11, delete the info folder
    elif choice == "11" or choice == "delete info":
        try:
            shutil.rmtree("info")
            print_with_color("Deleting info folder...", color=Fore.RED, brightness=Style.DIM)
            time.sleep(0.5)
            print_with_color("Done!", color=Fore.GREEN, brightness=Style.DIM)
        except FileNotFoundError:
            pass
    
    #if the user chooses 12, list the contents of the current directory
    elif choice == "12" or choice == "list current dir":
        print("Contents of the current directory: \n")
        for i in contentsofdir:
            print(i)
        print("\n")

    #if the user chooses 13, display the time the program was last run
    elif choice == "13" or choice == "time last run":
        if oldtimeanddate == "":
            print("No previous time and date")
        else:
            print(oldtimeanddate)

    #if the user chooses 14, ask the user what url they want to open
    elif choice == "14" or choice == "open url":
        #ask the user what url they want to open
        url = input("What is the url you want to open? \n")
        #open the url in the default browser
        webbrowser.open(url)

    #if the user chooses 15, locate their current location using their IP address
    elif choice == "15" or choice == "ip locate":
        weatherlocation = getcity(ip_address)
        with open("info/weatherlocation.txt", "w") as file:
            file.write(weatherlocation)
        print("Your city is " + weatherlocation + "." + "\n")

    #if the user chooses 16, display their current IP address
    elif choice == "16" or choice == "ip":
        print("Your IP address is " + ip_address + "." + "\n")

    #if the user chooses 17, display contents of the info folder
    elif choice == "17" or choice == "list info":
        print("Contents of the info directory: \n")
        for i in contentsofinfodir:
            print(i)
        print("\n")

    #if the user chooses 18, save a file called audio.mp3 with a text to speech voice
    elif choice == "18" or choice == "save tts":
        # On linux make sure that 'espeak' and 'ffmpeg' are installed
        textinput = input("What would you like to say? \n")
        engine.save_to_file(textinput, "audio.mp3")
        engine.runAndWait()
        print("File saved as audio.mp3")

    #if the user chooses 19, delete the audio.mp3 file
    elif choice == "19" or choice == "delete tts":
        os.remove("audio.mp3")
        print_with_color("Deleting audio.mp3...", color=Fore.RED, brightness=Style.DIM)
        time.sleep(0.5)
        print_with_color("Done!", color=Fore.GREEN, brightness=Style.DIM)

    #if the user chooses 20, choose a random number
    elif choice == "20" or choice == "randomnum":
        firstbetween = int(input("What is the smallest number? \n"))
        secondbetween = int(input("What is the largest number? \n"))
        if firstbetween > secondbetween:
            print_with_color("The first number must be smaller than the second number. \n", color=Fore.RED, brightness=Style.DIM)
        else:
            print("Your random number is " + str(random.randint(firstbetween, secondbetween)) + "." + "\n")

    else:
        print_with_color("Invalid choice." + "\n", color=Fore.RED, brightness=Style.DIM)