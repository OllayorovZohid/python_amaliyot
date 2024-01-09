# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:47:16 2024

@author: Zohidbek
"""
# ValueError
#yosh = input("Yoshingizni kiriting: ")
#try:
#    yosh = int(yosh)
    
#except ValueError:
#    print("Siz butun son kiritmadingiz")
#else:
#    print(f"Siz {2021-yosh} yilda tug'ilgansiz")

#print("Dastur davom etmoqda")
# ZeroDivisionError
#x,y = 5,10
#try:
#    y/(x-5)
#except:
#    print("0 ga bolish mumkin emas")

# IndexError
#mevalar = ['olma','anor','anjir','uzum']
#try:
#    print(mevalar[4])
#except IndexError:
#    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# KeyError

#user = {"username":"sariqdev",
#        "status":"admin",
#        "email":"admin@sariq.dev",
#        "phone":"99897123456"}

#key="tel"
#try:
#    print(f'Foydalanuvchi: {user[key]}')
#except KeyError:
#    print("Bunday kalit mavjud emas")

# FileNotFoundError
#filename = 'nimadir.txt'
#try:
#    with open(filename) as file:
#        text = file.read()
#except FileNotFoundError:
#    print(f"{filename} mavjud emas")


#import json
#files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
#for filename in files:
#    try:
#        with open(filename) as f:
#            talaba = json.load(f)        
#    except FileNotFoundError:
#        #print(f"{filename} mavjud emas")
#        pass # Hech narsa bajarmaydi
#    else:
#        print(talaba['ism'])

# 1 tadan kop exceptlarni yozish

#n = input("Butun son kiriting: ")
#try:
#    n = int(n)
#    x=20/n
#except ValueError: # agar foydalanuvchi butun son kiritmasa
#    print("Butun son kiritmadingiz")
#except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#    print("0 ga bo'lib bo'lmaydi")
#else:
#    print(f"x={x}")

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit(): # isdigit() --> raqamlardan tashkil topganini tekshiradi.
        yosh = int(yosh)
        break        

print(f"Siz {2024-yosh} yilda tug'ilgansiz")

