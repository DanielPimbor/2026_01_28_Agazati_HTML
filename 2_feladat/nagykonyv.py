"""1. 1.	Készítsen programot a következő feladatok megoldására, melynek kódját nagykonyv.py néven mentse el. 
Olvassa be az UTF-8 kódolású konyvek.txt állományban lévő adatokat és tárolja el egy saját osztály (konyv) típusú listában! 
Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza! Az élő íróknak nincs megadva halálozási év. 
Az adatok tárolásakor ezeknél az íróknál a 2005-ös évet tárolja el halálozási évként!"""

#konyv = {'nev': adatok[0], 'szulEv': adatok[1],'halEv': adatok[2], 'nemzetiseg' : adatok[3], 'cim' : adatok[4], 'helyezes': adatok[5]}

konyvek = []
with open('2_feladat/konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        #nev;szulEv;halEv;nemzetiseg;cim;helyezes
        nev = adatok[0]
        szulEv = int(adatok[1])
        halEv = int(adatok[2]) if adatok[2] != '' else 2005
        nemzetiseg = adatok[3]
        cim = adatok[4]
        helyezes = int(adatok[5])
        konyv = {'nev': nev, 'szulEv': szulEv,'halEv': halEv, 'nemzetiseg' : nemzetiseg, 'cim' : cim, 'helyezes': helyezes}
        konyvek.append(konyv)

print(f'{konyvek=}')

print(f'3.2. feladat: Az állományban {len(konyvek)} db könyv adatai szerepelnek.')

# 3.3 feladat: A legjobb helyezést elért magyar könyv: Gárdonyi Géza: Egri csillagok

magyar_konyvek=[]

for konyv in konyvek:
    if konyv['nemzetiseg'] == 'magyar':
        magyar_konyvek.append(konyv)

print(len(magyar_konyvek))

legjobb_konyv = magyar_konyvek[0]

for konyv in magyar_konyvek:
    if konyv['helyezes'] < legjobb_konyv['helyezes']:
        legjobb_konyv = konyv


print(f'3.3 feladat: A legjobb helyezést elért magyar könyv: {legjobb_konyv['nev']}: {legjobb_konyv['cim']}')

#3.4. feladat: A listában szerepel német író könyve.

van_nemet = False

for konyv in konyvek:
    if konyv['nemzetiseg'] == 'német':
        van_nemet = True
        break
    
    else:
        van_nemet = False


if van_nemet:
    print('A listában szerepel német író könyve')

else:
    print('A listában nem szerepel német író könyve')


#3.5. feladat: 90 évesnél idősebb írók:
	# Szepes Mária
	# Robert Merle
	# Jerome David Salinger
	# Faludy György
	# Maurice Druon

idosebb_mint_90 = []

for konyv in konyvek:
    if (konyv['halEv'] - konyv['szulEv']) > 90 :
        idosebb_mint_90.append(konyv['nev'])

print(f'90 évesnél idősebb írók: {idosebb_mint_90}')