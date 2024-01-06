# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 09:54:59 2024

@author: Zohidbek
"""

#def salom_ber(ism):  # bu yerda ism  -->  parametr
#    '''Foydalanuvchini ismini qabul qilib, salom beuvchi funksiya ''' # Funksiya haqida malumot  docstring
#    print(f"Assalomu aleykum hurmatli {ism.title()}!")
#salom_ber("Zohidbek")   #  bu yerda "Zohidbek"  --> argument

#def toliq_ism(ism, familiya):
#    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}\n"
#          f"Foydalanuvchi familiyasi: {familiya.title()}")

#toliq_ism("Zohidbek", "Ollayorov")
#def yosh_hisobla(ism, tugilgan_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
    
#yosh_hisobla(ism = "Zohidbek",tugilgan_yil=2002)

#def yosh_hisobla(tugilgan_yil, joriy_yil=2024): # joriy yil uchun st.qiymat 2020
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

#yosh_hisobla(2002,2024)

#    Amaliyot - 19

#def tyil_qaytar(ism,yosh,jyil = 2024):
#    '''Foydalanuvchi ismini va yoshini so'rab tugilgan yilini qaytaruvchi funksiya'''
##    print(f"{ism.title()} - {jyil - yosh}yilda tugilgansiz")

#tyil_qaytar("Zohidbek",22)

#def kvadrat_qaytar(a):
#    '''Foydalanuvchidan son olib, uning kvadrati va kubini qaytaruvchi funksiya'''
#    print(f"{a} ning kvadrati {a**2}")
#    print(f"{a} ning kubi {a**3}")

#kvadrat_qaytar(5)

#def juft_toq(a):
#    '''Foydalanuvchidan son olib, son juft yoki toqligini  qaytaruvchi funksiya'''
#    if a%2==0:
#        print(f"{a} juft son")
#    else:
#        print(f"{a} toq son")
#juft_toq(5)

#def kattasini_qaytar(a,b):
#    '''Foydalanuvchidan ikkita son olib, ulardan kattasini qaytaruvchi funksiya'''
#    if a==b:
#        print(f"Sonlar teng")
#    elif a>b:
#        print(a)
#    else:
#        print(b)
#kattasini_qaytar(4, 3)
#def darajani_qaytar(x,y=3):
#    '''Foydalanuvchidan ikkita son olib, x**y ni qaytaruvchi funksiya'''
#    print(x**y)

#darajani_qaytar(3)

#def tekshir(a):
#    '''Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga
#    qoldiqsiz bo'linishini tekshiruvchi funksiya'''
#    for i in range(2,10):
#        if a%i==0:
#            print(f"{a} soni {i} ga qoldiqsiz bo'linadi")

#tekshir(36)

#20 - dars . Funksiyadan qiymat qaytarish

#def toliq_ism_yasa(ism, familiya):
#    """Toliq isma qaytaruvchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism # toliq_ism --> local variable  

#talaba = toliq_ism_yasa("Zohidbek", "Ollayorov")
#print(talaba)

#def toliq_ism_yasa(ism, familiya, otasining_ismi=''): # Ixtiyoriy argument
#    """Toliq isma qaytaruvchi funksiya"""
#    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism = f"{ism} {familiya}"
#    return toliq_ism.title()

#talaba = toliq_ism_yasa("Zohidbek", "Ollayorov","Sanatbek ogli")
#print(talaba)

#def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#    avto = {'kompaniya':kompaniya,
#            'model':model,
#            'rang':rangi,
#            'korobka':korobka,
#            'yil':yili,
#            'narh':narhi}
#    return avto

#avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
#avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
#avtolar = [avto1, avto2]
#print('Onlayn bozordagi mavjud avtomashinalar:')
#for avto in avtolar:
#    if avto['narh']:
#        narh = avto['narh']
#    else:
#        narh = "Noma'lum"
#    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

#def oraliq(min,max,qadam=1):
#    sonlar = [] # bo'sh ro'yxat
#    while min<max:
#        sonlar.append(min)
#        min += qadam
#    return sonlar
#print(oraliq(0,10,3))
#print(oraliq(10,200,6))

#def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#    avto = {'kompaniya':kompaniya,
#            'model':model,
#            'rang':rangi,
#            'korobka':korobka,
#            'yil':yili,
#            'narh':narhi}
#    return avto

#print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
#avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#while True:
#    print("\nQuyidagi ma'lumotlarni kiriting",end='')
#    kompaniya=input("Ishlab chiqaruvchi: ")
#    model=input("Modeli: ")
#    rangi=input("Rangi: ")
#    korobka=input("Korobka: ")
#    yili=input("Ishlab chiqarilgan yili: ")
#    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
#    javob = input("Yana avto qo'shasizmi? (yes/no): ")
#    if javob=='no':
#        break

# Amaliyot  -  20
# 1
#def biografiya_qatrar(ism,familiya,t_yil,t_joy,email=None,tel=None,j_yil=2024):
#    '''Foydalanuvchining biografiyasini qaytaruvchi funksiya'''
#    lugat = {}
#    lugat["Ismi"] = ism
#    lugat["Familyasi"] = familiya
#    lugat["Tugilgan yili"] = t_yil
#    lugat["Tugilgan joyi"] = t_joy
#    lugat["Email"] = email
#    lugat["Tel"] = tel
#    lugat["Yoshi"] = j_yil - t_yil
#    return lugat

#print("Mijozlar haqida ma'lumot")
#mijozlar = []
#while True:
#    ism = input("Ismi: ")
#    familiya = input("Familiyasi: ")
#    t_yil = int(input("Tug'ilgan yili: "))
#    t_joy = input("Tug'ilgan joyi: ")
#    email = input("Email: ")
#    telefon = input("Telefon raqami: ")
#    mijozlar.append(biografiya_qatrar(ism, familiya, t_yil, t_joy,email,telefon))
#    savol = input("Yana malumot kiritasizmi (ha/yo'q)")
#    if savol == "yo'q":
#        break
    
#print("Mijozlar haqida ma'lumot")
#for mijoz in mijozlar:
#    print(f"{mijoz['Ismi'].title()} {mijoz['Familyasi'].title()}. {mijoz['Tugilgan yili']} - yilda {mijoz['Tugilgan joyi']}da tugilgan."
#          f"Emaili - {mijoz['Email']}.Telefon raqami - {mijoz['Tel']}. Hozirda {mijoz['Yoshi']} yoshda.")
# 3
#def kattasini_qaytar(a,b,c):
#    '''Uchta sondan kattasini qaytaruvchi funksiya'''
#    q = [a,b,c]
#    return max(q)

#print(kattasini_qaytar(4, 6, -23))
# 4
#def lugat_qaytar(radius):
#    '''Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
#    diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya'''
#    lugat = {}
#    lugat['radius'] = radius
#    lugat['diametr'] = radius*2
#    lugat['perimetr'] = 2*radius*3.14
#    lugat['aylana_yuzi'] = 3.14*radius*radius
#    return lugat

#print(lugat_qaytar(3))

# 5
#def tub_son_qaytar(a,b):
#    '''Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya'''
#    tub_sonlar = []
#    for i in range(a,b):
#        for j in range(2,i):
#            if i%j==0:
#                break
#        else:
#            tub_sonlar.append(i)        
#    return tub_sonlar

#print(tub_son_qaytar(2, 1000))

# 6 

#def fibonatchi_qaytar(a):
#    '''Foydalanuvchidan son qabul qilib, shu son miqdoricha
#    Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya'''
#    fibonatchi_sonlar = []
#    for i in range(a):
#        if i==0 or i ==1:
#            fibonatchi_sonlar.append(1)
#        else:
#            fibonatchi_sonlar.append(fibonatchi_sonlar[i-1]+fibonatchi_sonlar[i-2])
#    return fibonatchi_sonlar

#print(fibonatchi_qaytar(10))

# 21-dars. Funksiyaga ro'yxat uzatish

#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism] = int(baho)
#    return baholar

#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar[:])
#print(baholar)
#print(talabalar)

#  Amaliyot - 21 
# 1 
#def kattaga_aylantir(matn):
#    '''Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir 
#    matnning birinchi harfini katta harfga o'zgatiruvchi funksiya'''
#    q = []
#    for i in matn:
#        q.append(i.capitalize()) 
#    return q
#
#ismlar = ['ali', 'vali', 'hasan', 'husan']
#print(kattaga_aylantir(ismlar))

def bahola(ismlar):
    baholar = {}
    for i in ismlar:
        baho = input(f"Talaba {i.title()}ning bahosini kiriting: ")
        baholar[i] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)
# docstring  -- > Funksiya haqida malumot qaytaradi. ''' ichida yoziladi'''
# funksiya_nomi.__doc__  --> funksiya haqida malumot qaytaradi.
#print(salom_ber.__doc__)