"""2. feladat: Oszthatóság	14 pont
Írjon programot oszthato.py néven. A programban hozzon létre egy függvényt oszthato néven, ami egy egész számot 
kap paraméterként és igaz értéket ad vissza, ha a szám 7-tel osztható, 
de 3-mal nem. A függvény segítségével számolja ki azon 3 jegyű 
számok átlagát, amire a függvény igaz értékkel tér vissza.
Minta:
A 7-tel osztható és 3-mal nem osztható 3 jegyű számok átlaga: 
551.2705882352941
"""

#a zarojelben van a paramétek, a def a fuggvény, igazi érték a True
def oszthato(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        return True #return !!!!!!!!!!
    
    #az else is fontos a false miatt
    else:
        return False #return !!!!!!!!!!

#meghivom a fuggvenyt
# print(oszthato(14))
#///////////////////////////////////

#AZ EN MEGOLDASOM

true_3_jegyuk=[] #fontos hamarabb meghatározni vagyis a for cikluson kivul a listat

for i in range(100,1000):  #ezekbe (vagyis az i ben) van a 100-999 de az utso nem szamitodik bele szoval 1000
    if oszthato(i):
        true_3_jegyuk.append(i) #hozzaadjuk a helyes listához

true_3_jegyuk_atlaga= sum(true_3_jegyuk) / len(true_3_jegyuk) #atlag = sum/ darabszam és a darabszam = a lista hosszával

print(true_3_jegyuk_atlaga) 

#///////////////////////////////////

#TABALAS MEGOLDAS
# darab = 0
# osszeg = 0
# for i in range(100,1000):
#     if oszthato(i):
#         darab += 1
#         osszeg += i

# atlag = osszeg / darab
# print(atlag)

#///////////////////////////////////