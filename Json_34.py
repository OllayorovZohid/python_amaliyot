# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:59:19 2024

@author: Zohidbek
"""
import requests
import json

#url = "https://uz.wikipedia.org/wiki/Alisher_Navoiy"
#responce = requests.get(url)
#print(json.dumps(responce.json()))

#x = 10
#x_json = json.dumps(x) # dumps() --json formatga otiradi
 
#y = 5.5
#y_json = json.dumps(y)

#m = True
#m_json = json.dumps(m)
#m2 = json.loads(m_json)

#sonlar = (12,23,34,45)
#sonlar_json = json.dumps(sonlar)
#sonlar2 = json.loads(sonlar_json) # loads() - json formatdan pythonga otkazadi

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor,indent=4) # indent --> konsolga chiroyli chiqarish uchun
#print(bemor_json)

with open('bemor.json','w') as f:
    json.dump(bemor,f) # dump() --> json formatga otirip faylga saqlash
    
bemor2 = json.loads(bemor_json)
#print(bemor2)
    
filename = 'bemor.json'
with open(filename) as f:
    bemor3 = json.load(f)    
    
#print(bemor3)
#print(type(bemor3))
    
# indent --> konsolga chiroyli chiqarish uchun
# dumps() --json formatga otiradi
#  # loads() - json formatdan pythonga otkazadi
# dump() --> json formatga otirip faylga saqlash
# load() --> json formatdan oqish uchun ishlatiladi.
    
    
# Amaliyot - 34
# 1
#data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
#data_json = json.dumps(data)
#print(data_json)
#with open('data.json','w') as file:
#    json.dump(data,file) # data.json fayliga yozildi
#print(type(data_json))
# 2
#talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
#talaba = json.loads(talaba_json) 
#print(f"{talaba['ism']} {talaba['familiya']}")
#with open('talaba.json','w') as file:
#    json.dump(talaba,file) # talaba.json fayliga yozildi
     
# 4
python_data = {"batchcomplete":"","query":{"pages":{"13801":{"pageid":13801,"ns":0,"title":"Python","extract":"Python ([\u02c8p\u028c\u026a\u03b8 (\u0259)n] \u2014 payton, piton) \u2014 turli sohalar uchun yuqori darajadagi umumiy maqsadli dasturlash tili. Uning dizayn falsafasi muhim chekinishdan foydalangan holda kodning o\u02bbqilishiga urg\u02bbu beradi. Uning til konstruksiyalari va obyektga yo\u02bbnaltirilgan yondashuvi dasturchilarga kichik va yirik loyihalar uchun aniq, mantiqiy kod yozishda yordam berishga qaratilgan. Shuningdek Python sun\u02bciy intellekt hamda ma\u02bclumotlar muhandisiligi sohalarining tili hisoblanadi.\nPython deyarli barcha platformalarda ishlay oladi, xususan Windows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar shular jumlasidandir. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud bo\u02bblib, uning nomi \u2014 IronPython dasturlash muhitidir.\nGuido van Rossum 1980-yillarning oxirida ABC dasturlash tilining davomchisi sifatida Python ustida ishlay boshladi va birinchi marta 1991-yilda Python 0.9.0 versiyasini ommaga e\u02bclon qildi.\nPython dasturlash tiliga bo\u02bblgan talab yildan yilga oshib bormoqda. CodingDojo portalining tadqiqotlariga ko\u02bbra, 2020\u20142021-yillarda aynan Python tilida dasturlovchi mutaxassislarga eng ko\u02bbp talab bo\u02bblgan.\n\n"}}}}    
print(python_data['query']['pages']['13801']['title']) 
print(python_data['query']['pages']['13801']['extract'])
    
    
    
    
    