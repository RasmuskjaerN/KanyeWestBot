#KanyeWestBot
import requests
from requests import api
import json
import random
import socket

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
Bye = False
Store = []
Greeting = "Yo im Yeezy!"
First_message = input(Greeting)

while Bye == False:
    user_response = input()
    #user_input = Store.append(user_response)
    
    if(user_response == "hi"):
        print(Hi_response[random.randint(0,len(Hi_response))])
    elif(user_response == "how are you?"):
        print(Hi_response[random.randint(0,len(How_are_you_reponse))])
    elif user_response=="Bye":
        Bye=True
        break
    else:
        print(Hi_response[random.randint(0,len(General_response))])
    
       

#UDP
recivedMessage = False;
def recieve():
    while (True):
        data, addr = sock.recvfrom(1024)
        recivedMessage = True
        #print(Greeting)
        message = quotes[random.randint(0,9)]
        print(message)