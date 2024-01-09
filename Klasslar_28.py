# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:00:37 2024

@author: Zohidbek
"""
#x = 10
#print(type(x))

#def salom():
#    print("Assalom aleykum")
    
#salom()
#print(type(salom))

#class Talaba: # classni nomini katta harf bilan boshlash kerak iloji boricha
#    def __init__(self,ism,familya,tyil):
#        self.ism = ism
#        self.familya = familya
#        self.tyil = tyil
        
#    def get_name(self):
#        return self.ism
    
#    def get_lastname(self):
#        return self.familya
        
#    def get_age(self,yil):
#        return yil - self.tyil
        
#    def tanishtir(self):
#        return f"Ismim {self.ism} {self.familya}, tugilgan yilim {self.tyil}"
    
#talaba1 = Talaba("Zohidbek", "Ollayorov", 2002)
#print(talaba1.ism) # Zohidbek
#talaba2 = Talaba("Ali", "Valiyev", 2007)
#print(talaba2.tyil) # 2007
#talaba1.tanishtir() # Ismim Zohidbek Ollayorov, tugilgan yilim 2002
#talaba2.tanishtir() # Ismim Ali Valiyev, tugilgan yilim 2007
#print(talaba1.get_name()) # Zohidbek
#print(talaba1.get_age(2024)) # 22

#  Amaliyot - 28

#class User:
#    def __init__(self,ism,foydalanuvchi_ismi,email,tel):
#        self.ism = ism
#        self.foydalanuvchi_ismi = foydalanuvchi_ismi
#        self.email = email
#        self.tel = tel
        
#    def get_ism(self):
#        return self.foydalanuvchi_ismi
    
#    def get_tel(self):
#        return self.tel
        
#    def get_info(self):
#        return f"Foydalanuvchi : {self.ism}, ismi:{self.foydalanuvchi_ismi} , email : {self.email}, Telefo raqami: {self.tel}"
        
#user1 = User("Student1340","Zohidbek","ollayorovzohidbek1340@gamil.com","991234567")
#user2 = User("Ali2343","Alibek","valiyevali@gamil.com","997654321")
#print(user1.get_info())
#print(user2.get_info())
#print(user2.get_ism())




# 29 - dars. Obyektlar bilan ishlash.

#class Talaba: # classni nomini katta harf bilan boshlash kerak iloji boricha
#    def __init__(self,ism,familya,tyil):
#        self.ism = ism
#        self.familya = familya
#        self.tyil = tyil
#        self.bosqich = 4 # standart qiymat
        
#    def set_bosqich(self,yangi_bosqich):
#        return self.yangi_bosqich
    
#    def update_bosqich(self):
#        self.bosqich += 1
        
#    def get_name(self):
#        return self.ism
    
#    def get_lastname(self):
#         return self.familya
        
#    def get_age(self,yil):
#        return yil - self.tyil
        
#    def get_info(self):
#        return f"{self.ism} . {self.bosqich} - kurs talabasi"
    
#talaba1 = Talaba("Ali", "Valiyev", 2000)
#talaba2 = Talaba("Bobur", "Temurov", 1998)
#talaba1.update_bosqich()
#print(talaba1.ism) # Ali
#print(talaba1.bosqich)  # 4
#print(talaba1.get_info())

#class Fan():
#    def __init__(self,nomi):
#        self.nomi = nomi
#        self.talabalar_soni = 0
#        self.talabalar = []
    
#    def add_student(self,talaba):
#        """Fanga talabalar qo'shish"""
#        self.talabalar.append(talaba)
#        self.talabalar_soni += 1
        
#    def get_students(self):
#        return [x.get_name() for x in self.talabalar]
    
    
#def see_methods(klass):
#    return [x for x in dir(klass) if not x.startswith('__')]

#matem = Fan('Oliy matematika')

#print(matem.talabalar_soni)
#matem.add_student(talaba1)
#matem.add_student(talaba2)
#print(matem.talabalar_soni)

#print(matem.get_students())
#print(dir(Talaba))
#print(see_methods(Talaba))
#print(talaba1.__dict__) # talaba1 ning xususiyatlarini qaytaradi
#print(talaba1.__dict__.keys()) # dict_keys(['ism', 'familya', 'tyil', 'bosqich'])
#print(see_methods(talaba1))
#  O'rgangan narsalarim 
# dir() --> obyektning barcha xususiyatlarini chiqaradi. 
# __eq__ --> kabi sozlar dunder metodlar deyiladi. bunday deyilishiga sabab 
# double underscore yani pastki ikki chiziq

#  Amaliyot - 29

class Avto():
    def __init__(self,model,rang,korobka,narx,tyil):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.tyil = tyil
        self.km = 0
        
    def get_model(self):
        return self.model
        
    def get_info(self):
        return f"{self.rang} {self.model} {self.korobka} korobka probeg {self.km} {self.tyil} - yil. Narxi : {self.narx}"
    
    def update_km(self,km):
        self.km = km
        return self.km

Jentra = Avto("Jentra", "oq", "Mexanik",13000,2022)
#print(Jentra.get_info())
Jentra.update_km(1345)
#print(Jentra.get_info())
Malibu = Avto("Malibu", "Qora", "avtomat", 18000, 2023)
Cobalt = Avto("Cobalt","Kulrang",'Mexanik',14000,2023)

class Avtosalon():
    def __init__(self,nomi,manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avtomobillar = []
        self.avtomobillar_soni = 0
        
    def add_avtomobil(self,avtomobil):
        self.avtomobillar.append(avtomobil)
        self.avtomobillar_soni += 1

    def get_avtomobillar(self):
        avtomobillar = []
        for avtomobil in self.avtomobillar:
            avtomobillar.append(avtomobil.get_info())
        return avtomobillar
    
xonqa_avtosavdo = Avtosalon("Xonqa_avtosavdo", "Xonqa")
xonqa_avtosavdo.add_avtomobil(Jentra)
xonqa_avtosavdo.add_avtomobil(Malibu)
xonqa_avtosavdo.add_avtomobil(Cobalt)

#print(xonqa_avtosavdo.get_avtomobillar())
#print(xonqa_avtosavdo.avtomobillar[0].get_info())
def see_methods(klass):
    return [x for x in dir(klass) if not  x.startswith('__')]
print(see_methods(Avto)) # ['get_info', 'get_model', 'update_km']
print(see_methods(Jentra)) # ['get_info', 'get_model', 'km', 'korobka', 'model', 'narx', 'rang', 'tyil', 'update_km']