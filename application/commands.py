# coding=utf-8
from application import bot
import Launch, requests, json

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['next'])
def nextLaunch(message):
    #a = Launch(json.load(urlopen('https://api.spacexdata.com/v3/launches/next')))
    r = requests.get('https://api.spacexdata.com/v3/launches/next')
    pipo = json.loads(r.content)


    print(pipo['flight_number'])
    #print(json.loads(r.content.encode('utf-8')))
    a = Launch(pipo)

    #bot.reply_to(message, a.name)
