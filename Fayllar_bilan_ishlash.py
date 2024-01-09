# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 07:30:59 2024
# 33-Dars . Fayllar bilan ishlash
@author: Zohidbek
"""

import pickle # Ozgaruvchilar, Obyektlarni faylga saqlash.

#file = open('pi.txt')
#PI = file.read()
#print(PI)
#file.close()
# Lekin bu usul tavsiya qilinmaydi

#with open('pi.txt') as file:
#    pi = file.read()
    
#pi = float(pi)
#print(pi)

#filename = "data/talabalar.txt"

#with open(filename) as file:
#    for line in file:
#        print(line)

#with open(filename) as file:
#    talabalar = file.readlines()
    
#talabalar = [talaba.rstrip() for talaba in talabalar] # \n larni olib tashlaydi
#print(talabalar)

# Faylga yozishni organamiz
#fayl_nomi = "new_file.txt"
#ism = "Alijon Valiyev"
#tyil = 1998
#with open(fayl_nomi,'w') as file: # 'w'(write) -- faylni yozish uchun ochadi
#    file.write(ism+'\n') # Yangi qatordan ozgaruvchini yozib boradi
#    file.write(str(tyil)+'\n')

#with open(fayl_nomi,'a') as file: # 'a'(append) -- faylga malumot qoshish uchun ochadi
#    file.write("Hasan Husanov\n") # Yangi qatordan ozgaruvchini yozib boradi
#    file.write("2003")

#talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
#talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

#with open('info','wb') as file: # 'wb' (write binary) yozish uchun.
#    pickle.dump(talaba1,file) # dump() --> faylga yozish
#    pickle.dump(talaba2,file)
    
#with open('info','rb') as file: # rb (read binary) oqish uchun
#    talaba1 = pickle.load(file) # load --> oqish. 1 - qatorni oqiydi
#    talaba2 = pickle.load(file)
    
#print(talaba1)
#print(talaba2)

# Organgan narsalarim
# open() -- >  Fileni ochish (mavjud bolgan faylni ochadi)
# file.read() --> Fayldan oqib olish
# file.close() -- > Faylni yopish.
# Faylni ochgandan keyin uni albatta yopish kerak,aks holda faylga 
#shikast yetishi mumkin
# readlines() --> Bu faylni qatorma-qator oqiydi.

#  Amaliyot - 33
# 1 
#filename = 'Fayllar_bilan_ishlash.txt'
#with open(filename) as file:
#    matn = file.read()
    
#print(matn)

#2 and 3
#filename = 'one-million.txt'
#with open(filename) as file:
#    matn = file.read()
    
#matn = matn.rstrip()
#matn = matn.replace('\n','')
#bdate = '31122000'
#print(bdate in matn)
#print(matn)
# 4 
#with open('pi.txt') as file:
#    pi = file.read()
    
#pi = float(pi)
#with open('info','wb') as file:
#    pickle.dump(pi,file)
# 5 
#while True:
#    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
#    if not book: break
#    with open('books.txt','a') as file:
#        file.write(book+'\n')    