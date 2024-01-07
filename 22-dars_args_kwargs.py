# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:36:32 2024

@author: Zohidbek
"""
# *args  va  **kwargs
#def summa(*sonlar):  # Ozgarmas royxat kabi saqlanadi yani tuple korinishida
#    yigindi = 0
#    for son in sonlar:
#        yigindi += son
#    return yigindi

#def summa(*sonlar):  # Ozgarmas royxat kabi saqlanadi yani tuple korinishida
#    return sum(sonlar)



#def summa(x,y,*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#    return x+y+sum(sonlar)

#print(summa(1,2,3,4))
#print(summa(1,2,3,4,-9,23,4))

#def avto_info(kompaniya,model,**malumotlar):
#    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#    malumotlar['kompaniya']=kompaniya
#    malumotlar['model']=model
#    return malumotlar

#avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
#avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

#print(avto2)

# Amaliyot - 22
# 1
#def multiply(*sonlar):
#    kopaytma = 1
#    for son in sonlar:
#        kopaytma *= son
#    return kopaytma

#print(multiply(3,5,6,3))

# 2 
#def talaba_malumoti(ism,familiya,**malumotlar):
#    '''Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya'''
#    malumotlar['ism'] = ism
#    malumotlar['familiya'] = familiya
#    return malumotlar

#talaba1 = talaba_malumoti("Zohidbek", "Ollayorov", kurs = 4,fakultet = 'Dasturiy injinering',tyil=2002)
#print(talaba1)

## Organgan narsalarim
# *args --> funksiyaga istalgancha qiymat berish mumkin.
# bular tuple korinishida saqlanadi
# **kwargs --> funkssiyaga istalgancha kalit,qiymat juftligini berish mumkin.
#  23 - dars. Modullar



#import dars_funksiya as df #  as  --> modulga qisqa nom berish. 
# import deb chaqirib olish uchun fayllar 1 papkada bolishi kerak

#avto1 = df.avto_info('GM', "Jentra", "Oq", "Mexanik", 2023)
#df.info_print(avto1)

#from dars_funksiya import avto_info as ai,info_print as ip 
# funksiyani nomini ham qisqartiramiz

#avto1 = ai('GM', "Jentra", "Oq", "Mexanik", 2023)
#ip(avto1)

#from dars_funksiya import *  #  * barcha funksiyalarni chaqirib oladi.
# Lekin bu usul tavsiya etilmaydi. Chunki modulda koplab funksiyalar bolishi mumkin
# Modul kichkina bolsa foydalansa boladi.
#avto1 = avto_info('GM', "Jentra", "Oq", "Mexanik", 2023)
#info_print(avto1)

#import math
#x = 400
#print(math.sqrt(x))
#print(math.pi)

#import random
#son = random.randint(0,100)
#print(son)

#ismlar = ['olim','anvar','hasan','husan']
#ism = random.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
#print(ism)
#print(random.choice(ism))

#x = list(range(0,51,5))
#print(x)
#print(random.choice(x))
#x = list(range(11))
#print(x)
#random.shuffle(x)
#print(x)

# 24 - dars. Lambda, map,

#import math
#from math import sqrt
#uzunlik = lambda pi,r:2*pi*r
#print(uzunlik(3.14,3))
#kvadrat = lambda x,y:x**y
#print(kvadrat(3,2))

#def daraja(n):
#    return lambda x:x**n

#kvadrat = daraja(2)
#kub = daraja(3)
#print(kvadrat(5))
#print(kub(6))
 
#sonlar = list(range(11))
#ildizlar = list(map(sqrt,sonlar))
#print(ildizlar)

#def daraja2(x):
#    return x**2

#print(daraja2(5))
#print(list(map(daraja2,sonlar)))
#kvadratlar = list(map(lambda x:x**2,sonlar))
#print(kvadratlar)

#a = [4,5,6]
#b = [7,8,9]
#a_plus_b = list(map(lambda x,y:x+y,a,b))
#print(a_plus_b)

#import random as r

#sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
#def juftmi(x):
#    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#    return x%2==0

#juft_sonlar = list(filter(lambda x:x%2==0,sonlar))
#print(sonlar)
#print(juft_sonlar)


#mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

#mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
#mevalar2 = list(filter(lambda meva:len(meva)>5,mevalar))
#print(mevalar2)
q = 0
def binary_search(x,y,z):
    global q
    q+=1
    while x<y:
        mid = (x+y)//2
        if  mid == z :
            return q
        elif z>mid:
            return binary_search(mid, y, z)
        else:
            return binary_search(x, mid, z)
print(binary_search(1, 10, 3))


#mevalar3 = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')),mevalar))
#print(mevalar3)
#  O'rgangan narsalarim
# random moduli
# random.randint() -- > berilgan oraliqdagi sonlardan birsini chiqaradi
# random.choice() -- > berilgan ro'yxatdan 1 element tanlaydi.
# Agar ro'yxat bo'sh bolsa xatolik kelib chiqadi
# random.shuffle() --> Ro'yxatni aralashtirib tashlaydi.
# random.sample(range(100),10) -- > 10 ta tasodifiy qiymatni olib beradi
# lambda --> nomsiz funksiya
# map --> 
# filter() --> 





