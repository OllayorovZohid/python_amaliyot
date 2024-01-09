# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:04:26 2024

@author: Zohidbek
"""

from uuid import uuid4 # tasodifiy id raqam generatsiya qilib beradi
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km # togridan togri murojaat qilib bolmaydi
        self.__id = uuid4()
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")
            
    #def __str__(self):
    #    return f"{self.rang} {self.model}"
    
    def __repr__(self): # __repr__ va __str__ funksiyalari bir vazifani bajaradi
        return f"{self.rang} {self.model}"
    
    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narh == boshqa_avto.narh
    
    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narh<boshqa_avto.narh
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narh<=boshqa_avto.narh
    
    def __len__(self):
        return 
    
#print(uuid4()) # c93e9fbc-89a2-4ff3-a46f-b7293aa0352d --> tasodifiy generatsiya qiladi
#avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)
#print(avto1.make)
#print(avto1.get_km())
#print(avto1.get_id())

#class Avto:
#    """Avtomobil klassi"""
#    __num_avto = 0
#    def __init__(self,make,model,rang,yil,narh,km=0):
#        """Avtomobilning xususiyatlari"""
#        self.make = make
#        self.model = model
#        self.rang = rang
#        self.yil = yil
#        self.narh = narh
#        self.__km = km
#        self.__id = uuid4()
#        Avto.__num_avto += 1
        
#    @classmethod
#    def get_num_avto(cls):
#        return cls.__num_avto
    
#    def get_km(self):
#        return self.__km
    
#    def get_id(self):
#        return self.__id
    
#    def add_km(self,km):
#        """Mashinaning km ga yana km qo'shish"""
#        if km>=0:
#            self.__km += km
#        else:
#            print("Mashina km kamaytirib bo'lmaydi")
    
#class Bus:
#    pass

#avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)
#avto2 = Avto("GM","Jentra","Oq",2023,20000,3456)
#print(avto1) # Qora Malibu

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index] = qiymat
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting:")
        
    
salon1 = AvtoSalon("MaxAvto")
avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)
avto2 = Avto("GM","Jentra","Oq",2023,20000,3456)
salon1.add_avto(avto1,avto2)






