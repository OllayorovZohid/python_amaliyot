# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:17:06 2024

@author: Zohidbek
"""
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def get_passprot(self):
        return self.__passport
    
inson = Shaxs("Vali", "Aliyev", "Ac4563562", 2004)


class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        Talaba.__talabalar_soni += 1
        
    @classmethod
    def get_talabalar_soni(self,cls):
        return cls.__talabalar_soni
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam
    
    def set_id(self,id):
        self.__idraqam = id
        return self.__idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich."
        return info
    
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        
    def get_fanlar(self):
        return self.fanlar
    
    def remove_fan(self,fan):
        if fan not in self.fanlar:
            print("Siz bu fanga yozilmagansiz")
        else:
            self.fanlar.remove(fan)
            


class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        
    def get_fan(self):
        return self.nomi
    
#matem = Fan("Matematika")
#ona_tili = Fan("Ona tili")
#ingliz_tili = Fan("Ingliz tili")
#rus_tili = Fan("Rus tili")
#fizika = Fan("Fizika")


talaba1_manzil = Manzil("77", "Namangan", "Urganch", "Xorazm")
talaba1 = Talaba("Hasan", "Husanov", "AB8765673", 1996, "N00000011",talaba1_manzil)    
talaba1 = Talaba("Hasan", "Husanov", "AB8765673", 1996, "N00000011",talaba1_manzil)    
talaba1 = Talaba("Hasan", "Husanov", "AB8765673", 1996, "N00000011",talaba1_manzil)    
#talaba1.fanga_yozil(matem)
#talaba1.fanga_yozil(ona_tili)
#talaba1.fanga_yozil(ingliz_tili)
#talaba1.fanga_yozil(rus_tili)
#talaba1.fanga_yozil(fizika)
#talaba1.remove_fan(matem)

    
#print(talaba1.fanlar[1].get_fan())

#class Professor(Shaxs):
#    def __init__(self,ism,familiya,passport,tyil,yonalish):
#        super().__init__(ism, familiya, passport, tyil)
#        self.yonalish = yonalish
        
#    def get_info(self):
#        info = f"{self.ism} {self.familiya} "
#        info += f"{self.yonalish} boyicha professor"
#        return info
    
#professor1 = Professor("ali", 'valiyev',"av562732", 1979, "it")
#print(professor1.get_info())
    
    
#class PHD(Professor):
#    def __init__(self,ism,familiya,passport,tyil,yonalish,tajriba):
#        super().__init__(ism, familiya, passport, tyil,yonalish)
#        self.tajriba = tajriba
        
#    def get_info(self):
#        info = f"{self.ism} {self.familiya} "
#        info += f"{self.yonalish} boyicha professor. {self.tajriba} yillik tajribaga ega"
#        return info
    
#kimdir = PHD('Hasan', "Husanov", "ac7684563", 1986, "IT", 5)
#print(kimdir.get_info())
    
    