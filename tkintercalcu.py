import client

client = client.Client("aditya5@outlook.com", "hlciofambiaic12@#")
friends = client.getUsers("rajeev")  # return a list of names
friend = friends[0]
sent = client.send(friend.uid, "Your Message")
if sent:
    print("Message sent successfully!")

import requests
import json
from uuid import uuid1
from random import random, choice
from datetime import datetime
from bs4 import BeautifulSoup as bs
from mimetypes import guess_type