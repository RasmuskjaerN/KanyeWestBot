#KanyeWestBot
import requests
from requests import api
import json
import random
import socket

#Set up of the socket to recieve UDP messages.
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

API = "https://api.kanye.rest/"

test_api = requests.get("https://api.kanye.rest/")
kanye_quote = test_api.json()
Hi_response = []
How_are_you_reponse = []
General_response = []

for i in range(10):
    test_api = requests.get("https://api.kanye.rest/")
    kanye_quote = test_api.json()
    Hi_response.append(kanye_quote['quote'])

for i in range(5):
    test_api = requests.get("https://api.kanye.rest/")
    kanye_quote = test_api.json()
    General_response.append(kanye_quote['quote'])

for i in range(3):
    test_api = requests.get("https://api.kanye.rest/")
    kanye_quote = test_api.json()
    How_are_you_reponse.append(kanye_quote['quote'])


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)


#Chat bot
Store = []
Greeting = "Yo im Yeezy!"
First_message = input(Greeting)

#function that takes a user input from the terminal and responds based
#on input.
def botMessageTerm():
    Bye = False
    while Bye == False:
        user_response = input()
        #user_input = Store.append(user_response)
    
        if(user_response == "hi"):
            print(Hi_response[random.randint(0,len(Hi_response))])
        elif(user_response == "how are you?"):
            print(Hi_response[random.randint(0,len(How_are_you_reponse))])
        elif (user_response=="Bye"):
            Bye=True
            break
        else:
            print(Hi_response[random.randint(0,len(General_response))]) 

"""Same function as above, but taking udp messages. 
Please note that it's necessary to hit enter i the terminal before 
the messages will start showing"""
def botMessageUDP():
    Bye = False
    while Bye == False:
        udpMessage = sock.recvfrom(1024)
        #user_input = Store.append(user_response)
    
        if(udpMessage =="hi"):
            print(Hi_response[random.randint(0,len(Hi_response))])
        elif(udpMessage == "how are you?"):
            print(Hi_response[random.randint(0,len(How_are_you_reponse))])
        elif (udpMessage =="Bye"):
            Bye=True
            break
        else:
            print(Hi_response[random.randint(0,len(General_response))]) 

#botMessageTerm()
#botMessageUDP()
