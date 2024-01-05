# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 20:47:01 2024

@author: Zohidbek
"""
#car_0 = {'model':'ferrari','rang':'qizil'}
#print(car_0['model'])
#print(car_0['rang'])

#en_uz = {'apple':'olma','apricot':'orik','banana':'banan'}
#print(en_uz)
#print(en_uz['apple'])

#mevalar = {'olma':10000,'tarvuz':8000,'qovun':10000}
#print(f"Olmaning narxi {mevalar['olma']} som")

#talaba = {'ism':'Zohid_Ollayorov','yosh':22,'t_yil':2002}
#talaba['kurs'] = 4
#talaba['fafultet'] = 'Dasturiy injinering'
#print(f"{talaba['ism'].title()},\
#      {talaba['yosh']}  -yoshda,\
#      {talaba['t_yil']} - yilda tugilgan")
#talaba['ism'] = 'Zohidbek'
#print(talaba)

#talaba_1 = {}
#print(talaba_1)
#talaba_1['ism'] = "Zohid Ollayorov"
#talaba_1['kurs'] = 4
#talaba_1['yosh'] = 22
#print(talaba_1)
#print(f"{talaba_1['ism'].title()} {talaba_1['kurs']}  - kurs")
#del talaba_1['yosh']
#print(talaba_1)

#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#    }
#phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#print(phone)

#    Amaliyot  -  14


#onam = {'ism':'Shoira','t_yil':1981,'manzili':'Xonqa'}
#print(f"Onamning ismi {onam['ism']}.\
#      Tugilgan yili {onam['t_yil']} . Manzili {onam['manzili']}")
#taomlar = {"Otam":"baliq","Onam":"palov","opam":"somsa","ukam":"moshxorda","Buvam":"norin"}
#print(f"Otamning sevimli taomi - {taomlar['Otam']}")
#print(f"Onamning sevimli taomi - {taomlar['Onam']}")
#print(f"Opamning sevimli taomi - {taomlar['opam']}")

#izohli_lugat = {
#    'for':"takrorlash operatori",
#    'if':'shart operatori',
#    'int':'Butun sonni ifodalaydi',
#    'float':'onlik sonni ifodalaydi',
#    'str':'matnni ifodalaydi',
#    'dict':'lugat',
#    'list':'ro\'yxat',
#    'tuple':'o\'zgarmas r\'oyxat',
#    'boolean':'True va False qaytaradi',
#    'github':'Dasturchining yuzi'
#    }
#matn = input("Istagan so'z kiriting:\n>>>>>")
#soz = izohli_lugat.get(matn,"Kechirasiz bunday so'z topilmadi")
#print(soz)
#if matn in izohli_lugat:
#    print(izohli_lugat[matn])
#else:
#    print("Kechirasiz bunday soz topilmadi")

# 15-dars. Lugat bilan ishlash
#talaba = {'ism':'Zohid_Ollayorov','yosh':22,'t_yil':2002}
#talaba['kurs'] = 4
#talaba['fafultet'] = 'Dasturiy injinering'
#print(talaba['yosh'])
#print(talaba.items())

#for key,value in talaba.items():
#    print(f"Kalit: {key}")
#    print(f"Qiymat: {value}\n")

#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#    }
#for k,q in telefonlar.items():
#    print(f"{k.title()} ning telefoni - {q}")
#print(telefonlar.keys())
#for ism in telefonlar: # keys() ni yozmaslik ham mumkin. Baribir shu natija
#    print(ism.title(    ))
#mahsulotlar = { # Do'kondagi mahsulotlar
#    'olma':10000,
#    'anor':20000,
#    'uzum':40000,
#    'anjir':25000,
#    'shaftoli':30000
#    }
#bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos dokoningizga {buyum} ni ham olib keling")
#print("Dokonimizdagi mahsulotlar")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())

#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310',
#    'hamida':'galaxy s9',
#    'maryam':'huawei p30',
#    'tohir':'iphone x',
#    'umar':'iphone x'    
#    }
#print(telefonlar.values())
#for tel in set(telefonlar.values()):
#    print(tel.title())

#toys = {'ball','car','lamp','ball'}
#print(type(toys))  # set
#print(toys)  # {'ball', 'car', 'lamp'}

#  Amaliyot - 15

#izohli_lugat = {
#    'for':"takrorlash operatori",
#    'if':'shart operatori',
#    'int':'Butun sonni ifodalaydi',
#    'float':'onlik sonni ifodalaydi',
#    'str':'matnni ifodalaydi',
#    'dict':'lugat',
#    'list':'ro\'yxat',
#    'tuple':'o\'zgarmas r\'oyxat',
#    'boolean':'True va False qaytaradi',
#   'github':'Dasturchining yuzi'
#    }
#for i,j in sorted(izohli_lugat.items()):
#    print(f"{i} -- {j}")

#davlatlar = {
#    "o'zbekiston":'toshkent',
#    'aqsh':'washington d.c.',
#    'rossiya':'moskva',
#    'tojikiston':'dushanbe',
#    "qirg'iziston":'bishkek',
#    'qozog\'iston':'nursulton',
#    'malayziya':'kuala-lumpur',
#    'singapur':'sungapur',
#    'italiya':'rim'
#    }
#print("Davlatlar quyidagilar")
#for davlat in sorted(davlatlar):
#    print(davlat.title())

#print("Poytaxtlar quyidagilar")
#for davlat in sorted(davlatlar.values()):
#   print(davlat.title())

#davlat = input("Istagan davlatni kiriting:\n>>>>>>")
#poytaxt = davlatlar.get(davlat,"Bizda bunday ma'lumot yo'q")
#if poytaxt == "Bizda bunday ma'lumot yo'q":
#    print("Bizda bunday ma'lumot yo'q")
#else:
#    print(f"{davlat.upper()} ning poytaxti - {poytaxt.title()}")

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
print("3 ta ovqat buyurtma qiling!")
buyurtmalar = []
for i in range(3):
    buyurtmalar.append(input(f"{i+1} - buyurtmani kiriting:\n>>>>>>"))

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} ning narxi - {menu[buyurtma]}")
    else:
        print("Bizda bunday taom yo'q")










# O'rgangan narsalrim
# dictdan element o'chirish  -->  del talaba_1['yosh']
# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#  get --> metodi  dictda shunday qiymat  bo'lmasa  xatolik qaytarmaydi, 
#dictni ozidan murojaat qilsa KeyErron qaytaradi. Yuqoridagi kodni ishlatib koring
#dict.ietms() --> kalit,qiymat  juftlikini qaytaradi.
# dict.keys() --> faqat kalitlarni qaytaradi.
# dict.values() --> faqat qiymatlarni qaytaradi.
# set() --> listlar kabi malumot turi. Bu faqat har xil qiymatli elementlarni saqaydi
