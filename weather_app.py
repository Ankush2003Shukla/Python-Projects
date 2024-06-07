import requests
import json
import pyttsx3
while(True):
    city = input("Enter the city name : ") #city name
    process = pyttsx3.init() #initializing
    process.setProperty('rate',150) #setting robo property
    if(city == 'q'):
        process.say("Thank you for your services!")
        process.runAndWait()
        break
    url = f"http://api.weatherapi.com/v1/current.json?key=1341dfb4aff0415dacc42727241703&q={city}" #weather api

    a =  requests.get(url) #running the url

    dic = json.loads(a.text) #loading the text in json 
    p = f"The current weather around {city} is {dic["current"]["temp_c"]} degree celcius"
    print(p)
    process.say(p)
    process.runAndWait()
    