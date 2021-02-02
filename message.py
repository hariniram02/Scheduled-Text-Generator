#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 02:23:34 2020

@author: hariniram
"""

# step 1: have preset messages
quotes = ['good morning!', 'wake up fugly slut ;)', 'who is josh groban? kill yourself', 
          'where where where are the duckies??', "i can't take right now i'm doing hot girl shit :D"]


# step 2: send message
from twilio.rest import Client
import schedule
import random

cellphone = 9725206216
twilio_num = 2314128705

def sendMessage(quote):
    account = 'AC36e22f4cc1856d063d4608d0a8c6937d'
    token = 'd81ca9bb93ceda2b1ec439ee9e654627'
    client = Client(account, token)
    
    client.messages.create(to=cellphone, 
                           from_=twilio_num, 
                           body=quote)

# step 3: schedule message
randQuote = quotes[random.randint(0, len(quotes))]
schedule.every().day.at("10:30").do(sendMessage, randQuote)
