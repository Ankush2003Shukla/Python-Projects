import pyttsx3

process = pyttsx3.init() #initializing

process.setProperty('rate',150) #setting up the speed of the sppech

while(True):
    a = str(input("What do you want me to say : ")) #text which will be speaken by the robo
    if(a =='q'):
        process.say("Thank you for your services!") #speaking the text
        process.runAndWait() #waiting for the sppech to finish
        break
    process.say(a) #speaking the text
    process.runAndWait() #waiting for the sppech to finish
    


