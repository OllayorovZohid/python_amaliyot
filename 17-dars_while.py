# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:15:00 2024

@author: Zohidbek
"""


#ism = input("Ismingiz nima?\n>>>>>")
#print(ism)
#savol = f"Salom {ism.title()}. Yoshingiz nechada?\n>>>>"
#yosh = int(input(savol))
#height = float(input("Boyingiz necha metr?"))

#son = 1
#while son<=5:
#    print(son)
#    son += 1

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting"
#savol += "(daasturni to'xtatish uchun 'exit' deb yozing):"
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#    else:
#        ishora = False

#   break 
#while True:   # abadiy sikl
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#    else:
#        break
#print("Dastur tugadi")

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son ==5:
#        break
#    else:
#        print(son**2)

#  continue 

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son ==5:
#        continue
#    else:
#        print(son**2)

#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)
#print("Dastur tugadi")

#     Amaliyot -- 17

#savol = "Yaxshi ko'rgan kitoblaringizni kiriting "
#savol += "(daasturni to'xtatish uchun 'stop' deb yozing):"
#ishora = True
#kitoblar = []
#while ishora:
#    qiymat = input(savol)
#    if qiymat != 'stop':
#        kitoblar.append(qiymat)
#    else:
#        ishora = False
#print(kitoblar)

#savol = "Yoshingizni kiriting. (Dasturni to'xtatish uchun 'stop' yoki 'exit' deb yozing)"
#while True:
#    qiymat = input(savol)
#    if qiymat =='stop' or qiymat == 'exit':
#        break
#    else:
#        if int(qiymat)<=7:
#            narx = 2000
#        elif int(qiymat)<=18:
#            narx = 3000
#        elif int(qiymat)<=65:
#            narx = 10000
#        elif int(qiymat)>65:
#            narx = 0
#    print(f"Chiptaning narxi - {narx} so'm")
#print("Dastur tugadi")

#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
#    qiymat = input(savol)
#    if qiymat=='Exit':
#        break
#    elif int(qiymat)<0:
#        continue
#    else:
#        ildiz = float(qiymat)**(0.5)
#       print(f"{qiymat} ning ildizi {ildiz} ga teng")

# 18 - dars. While , Ro'yxatlar va lugatlar.
#ismlar = []
#print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
#n=1 # ismlarni sanash uchun o'zgaruvchi
#while True:
#    savol = f"{n}-do'stingiz ismini kiriting:"
#    ism = input(savol)
#    ismlar.append(ism)
#    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#    if javob =='ha':
#        n+=1
#        continue
#     else:
#        break
#print("Dastur tugadi")
#print("Dos'tlaringiz ro'yxati")
#for ism in ismlar:
#       print(ism.title())

#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingiz ismini kiriting: ")
#    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#    if javob == "yo'q":
#        ishora = False

#for ism, yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")

#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
#print(cars)

#talabalar = ['hasan', 'husan', 'olim', 'botir']
#baholangan_talabalar = {}
#while talabalar:
#    talaba = talabalar.pop()
#    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#    print(f"{talaba.title()} baholandi")
#    baholangan_talabalar[talaba] = int(baho)
#print(baholangan_talabalar)

#     Amaliyot  -  18
#print("Buyurtma qabul qilamiz")
#savat = []

#while True:
#    savol = "Buyurtmangizni kiriting:\n>>>"
#    javob = input(savol)
#    savat.append(javob)
#    savol1 =  "Yana buyurtma kiritasizmi (ha/yo'q):\n>>>"
#    javob1 = input(savol1)
#    if javob1 == 'yo\'q':
#        break



#e_bozor = {'olma':20000,
#           'shaftoli':25000,
#           'tarvuz':18000,
#           'uzum':22000
#           }

#while True:
#    savol = input("Mahsulotingizni kiriting:\n>>>>")
#    javob = float(input(f"{savol.title()}ning narxini kiriting:\n>>>>"))
#    e_bozor[savol] = javob
#    savol1 = input("Yana mahsulot kiritasizmi (ha/yo'q)")
#    if savol1 == "yo'q":
#        break
    
#print("Mahsulotlar ro'yxati")
#for i,j in e_bozor.items():
#    print(f"{i.title()}ning narxi {j} so'm")


#while savat:
#    mahsulot = savat.pop()
#    if mahsulot in e_bozor:
#        print(f"{mahsulot.title()}ning narxi - {e_bozor[mahsulot]} so'm")
#    else:
#        print(f"Bizda {mahsulot} yo'q")










