# coding=utf-8
from application import bot
from telebot import types
#import Launch, requests, json
from Launch import *
from RocketInfo import *
from Roadster import *
import requests, json


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['latest'])
def nextLaunch(message):
    r = requests.get('https://api.spacexdata.com/v3/launches/latest')
    pipo = json.loads(r.content)

    a = Launch(pipo)

    bot.reply_to(message, a.imprimir())

@bot.message_handler(commands=['next'])
def nextLaunch(message):
    r = requests.get('https://api.spacexdata.com/v3/launches/next')
    pipo = json.loads(r.content)

    a = Launch(pipo)

    bot.reply_to(message, a.imprimir())

@bot.message_handler(commands=['rocket'])
def nextLaunch(message):
    r = requests.get('https://api.spacexdata.com/v3/rockets/falcon9')
    pipo = json.loads(r.content)

    a = RocketInfo(pipo)

    bot.send_message(message.chat.id, a.imprimir())

@bot.message_handler(commands=['roadster'])
def roadster(message):
    r = requests.get('https://api.spacexdata.com/v3/roadster')
    print(r.status_code)
    pipo = json.loads(r.content)

    a = Roadster(pipo)

    bot.send_message(message.chat.id, a.imprimir())
