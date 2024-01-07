# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:26:49 2024

@author: Zohidbek
"""
from transliterate import to_cyrillic,to_latin
import telebot

TOKEN = "6774393254:AAGrn2_mmz36Apc5sYYCEdpAl7gSShEXTNY"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu aleykum! Xush kelibsiz"
    javob += "\nMatn kiriting:"
    bot.reply_to(message,javob )
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg:to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    #if msg.isascii() == True:
    #    javob = to_cyrillic(msg)
    #else:
    #    javob = to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()

#matn = input("Matn kiriting:\n>>>")

#if matn.isascii() == True:
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))
    

         
# isascii()  --> matnni kril yoki lotinlikka tekshiradi
         

         

         
