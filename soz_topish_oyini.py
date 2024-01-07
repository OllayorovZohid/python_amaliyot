# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:40:09 2024

@author: Zohidbek
"""
# My code . Soz topish oyini.Sal murakkabroq. Lekin tushunsa bo'ladi.

from uzwords import words
import random

def get_words(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word

def display():
    harflar = ""
    soz = get_words(words)
    soz = soz.upper()
    taxmin = len(soz)*('-')
    print(f"Men {len(soz)} xonali soz oyladim.Topa olasizmi?\n{taxmin}")
    soz = list(soz)
    taxmin = list(taxmin)
    #print(soz)
    ishora = True
    sana = 0
    
    while soz != taxmin:
        sana += 1
        harf = input(f"Харф киритинг: ").upper()
        if harflar.count(harf)==1:
            print(f"Boshqa harf kiriting. Bu harfni avval kiritgansiz.")
            print(f"Shu vaqtgacha kiritgan harflaringiz: {harflar}")
            continue
        if harf in soz:
            print(f"{harf} harfi to'gri")
            cnt = soz.count(harf)
            soz_copy = soz[:]
            cnt1 = -1
            for i in range(cnt):
                cnt1 += 1
                indeks = soz_copy.index(harf)
                taxmin[indeks+cnt1] = harf
                soz_copy.remove(harf)
            print(taxmin)
        else:
            print(f"Bunday harf yoq")
        harflar += harf
        print(f"Shu vaqtgacha kiritgan harflaringiz: {harflar}")
    return taxmin,sana

topdim = display()
topgan_soz = topdim[0]
satr=''
for i in topgan_soz:
    satr += i

print(f"Siz oylagan soz {satr.upper()}. {topdim[1]} ta urinishda topdim")

 #  Mohirdevning kodi. Soz topish oyini.
#import random
#from uzwords import words


#def get_word():
#    word = random.choice(words)
#    while "-" in word or " " in word:
#        word = random.choice(words)
#    return word.upper()


#def display(user_letters, word):
#    display_letter = ""
#    for letter in word:
#        if letter in user_letters:
#            display_letter += letter
#        else:
#            display_letter += "-"
#    return display_letter


#def play():
#    word = get_word()
#    # So'zdagi harflar
#    word_letters = set(word)
#    # Foydalanuvchi kiritgan harflar
#    user_letters = ""
#    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
#    # print(word)
#    while word_letters:
#        print(display(user_letters, word))
#        if user_letters:
#            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")

#        letter = input("Ҳарф киритинг: ").upper()
#        if letter in user_letters:
#            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
#            continue
#        elif letter in word:
#            word_letters.remove(letter)
#            print(f"{letter} ҳарфи тўғри.")
#        else:
#            print("Бундай ҳарф йўқ.")
#        user_letters += letter
#    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
#play()