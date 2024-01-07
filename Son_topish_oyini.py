# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:40:05 2024

@author: Zohidbek

Son topish o'yini
"""
#  Men yozgan  kod. 1 2 ta kamchiliki bor. Pastda Mohirdevning kodi.
import random
print("Keling o'ylagan sonni topish o'ynaymiz!")
son = int(input("1 dan 10 gacha son o'yladim. Topa olasizmi? \n >>>"))
men_oylagan_son = random.randint(1, 10)
ishora = True
cnt = 0
while ishora:
    cnt += 1
    if men_oylagan_son == son:
        print(f"Topdingiz. {son} sonini o'ylagan edim. {cnt} ta taxmin bilan topdingiz!")
        ishora = False
    else:
        if men_oylagan_son<son:
            son = int(input(f"Xato, men o'ylagan son bundan kichikroq!"
                  f"Yana harakat qiling!\n>>>>"))
        else:
            son = int(input(f"Xato, men o'ylagan son bundan kattaroq!"
                  f"Yana harakat qiling!\n>>>"))
matn = input("Keling endi siz son o'ylaysiz!. Men topaman!")  

def cp():
    cnt1 = 0
    quyi = 1
    yuqori = 10
    ishora1 = True
    number = input(f"Siz 5 sonini o'ylagansiz.to'gri(T),men oylagan son bundan kattaroq(+), yoki kichikroq(-)?\n>>>")
    while ishora1:
            cnt1 += 1 
            if quyi != yuqori:
                taxmin = random.randint(quyi, yuqori)
            else:
                taxmin = quyi
            javob = input(
                f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
            )
            if javob == "-":
                yuqori = taxmin - 1
            elif javob == "+":
                quyi = taxmin + 1
            else:
                ishora1 = False
    print(f"Men {cnt1} ta taxmin bilan topdim!")
    return cnt1
cnt1 = cp()
            
if cnt == cnt1:
    print(f"Durrang. Ikkalamiz ham {cnt} ta urinishda topdik")
elif cnt>cnt1:
    print(f"Men yutdim.Men {cnt1} ta urinishda. Siz esa {cnt} ta urinishda topdingiz")
else:
    print(f"Yutdingiz. Siz {cnt} ta urinishda , men esa {cnt1} ta urinishda topdim")



#  Mohirdev kodi
#import random


#def sontop(x=10):
#    tasodifiy_son = random.randint(1, x)
#    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
#    taxminlar = 0
#    while True:
#        taxminlar += 1
#        taxmin = int(input(">>>"))
#        if taxmin < tasodifiy_son:
#            print("Kattaroq son ayting:", end="")
#        elif taxmin > tasodifiy_son:
#            print("Kichikroq son ayting:", end="")
#        else:
#            print("Yutdingiz!")
#            break

#    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
#    return taxminlar


#def sontop_pc(x=10):
#    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
#    quyi = 1
#    yuqori = x
#    taxminlar = 0
#    while True:
#        taxminlar += 1
#        if quyi != yuqori:
#            taxmin = random.randint(quyi, yuqori)
#        else:
#            taxmin = quyi
#        javob = input(
#            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
#            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
#        )
#        if javob == "-":
#            yuqori = taxmin - 1
#        elif javob == "+":
#            quyi = taxmin + 1
#        else:
#            break
#    print(f"Men {taxminlar} ta taxmin bilan topdim!")
#    return taxminlar


#def play(x=10):
#    yana = True
#    while yana:
#        taxminlar_pc = sontop_pc(x)
#        taxminlar_user = sontop(x)

#        if taxminlar_user > taxminlar_pc:
#            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
#        elif taxminlar_user < taxminlar_pc:
#            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
#        else:
#            print("Durrang!")
#        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))

#play()











     
