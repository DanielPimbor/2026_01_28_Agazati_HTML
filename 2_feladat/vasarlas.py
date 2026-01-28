"""1. feladat: Vásárlás	8 pont
Írjon programot vasarlas.py néven, ami billentyűzetről bekéri egy 
termék árát forintban, az euro árfolyamát és egy 
euro összeget, majd kiírja a minta szerint, hogy a beírt
euroért meg tudjuk-e vásárolni a terméket. 
"""

termek_ara= int(input('Kérem a termék árát forintban: '))
euro_arfolyam= float(input('Kérem az euro árfolyamát: '))
euro_van_nalam = float(input('Mennyi euróval rendelkezel: '))

if euro_van_nalam * euro_arfolyam >= termek_ara:
    print('A terméket meg tudod vásárolni!')

else:
    print('Nincs elég euród a termék megvásárlására!')
