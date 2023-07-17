[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba10%3A%20Sjedinjavanje%20multi-modalnih%20slika/OSuM_vezba_10.ipynb)

# Laboratorijska vežba 10: Sjedinjavanje multi-modalnih slika

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, osum

## 1. Mešanje  
  1.1 U promenljivu a učitati sliku 1_CT.jpg, a u promenljivu b učitati sliku 1_MR.jpg. Prikazati ih.  
  1.2 Sjediniti slike običnim mešanjem koristeći faktor k=0.5. Prikazati sliku nakon sjedinjavanja.  
  1.3 Isprobati više vrednosti za faktor mešanja k i svaki put prikazati sliku nastalu sjedinjavanjem. Analizirati koja slika ima više uticaja za različite faktore k.

## 2. Multiveličinsko sjedinjavanje  
  2.1 Razložiti slike a i b u Laplasove piramide sa 6 nivoa.  
  2.2 Za sjedinjavanje slika detalja može se koristiti select abs max pravilo koje maksimizuje kontrast u svakoj tački sjedinjene slike. Prvo je potrebno napraviti binarnu masku biramA koja definiše lokacije na kojima je slika a značajnije od slike b (veći lokalni kontrast) na datom nivou veličine, tj. tačke koje će se uzeti iz slike a. biramB je binarna maska koja definiše lokacije piksela koji se uzimaju sa slike b. Napraviti i prikazati maske biramA i biramB za prvi nivo Laplasove piramide.  
  2.3 Sjediniti slike detalja na svim nivoima veličine koristeći select abs max pravilo.  
  2.4 Sjediniti bazne uzimanjem srednje vrednosti baznih slika a i b.  
  2.5 Rekonstruisati piramidu sjedinjene slike i prikazati je. Da li je rezultat bolji nego sjedinjavanje mešanjem i na koji način?

## 3. Mešanje u boji  
  3.1 Učitati sliku lena_color.png u promenljivu lena i prikazati je pomoću funkcija iz openCV biblioteke, a zatim pomoću funkcija iz matplotlib biblioteke. Redosled kanala boje u matplotlib je RGB, a u openCV BGR. Ako se slika u boji prikazuje pomoću matplotlib funkcija potrebno je prvo reorganizovati redosled kanala boje.  
  3.2 U promenljivu a1 učitati sliku 2_CT.png, a u promenljivu b1 učitati sliku 2_PET.png. Invertovati PET sliku kako bi pozadina bila tamna, a mesta najveće prokrvljenosti svetla. Ovo su slike sa različitih modaliteta. Sjediniti ih običnim mešanjem sa različitim faktorima k. Kako izgledaju sjedinjene slike.  
  3.3 Slike koje potiču sa različitih modaliteta (CT-anatomski, PET-funkcionalni) obično se sjedinjuju u boji. Sjedinjavanje u boji indeksiranjem i mešanjem radimo tako što koristimo proizvoljno izabranu mapu boja da jednu od monohromatskih ulaznih slika pretvorimo u sliku u boji (RGB), a zatim je mešamo sa drugom monohromatskom slikom klasičnim linearnim mešanjem. U promenljivu a1_c učitati sliku 2_CT.png kao kolor sliku. Budući da sve komponente boje jednog piksela imaju iste vrednosti ova slika je i dalje u sivoj skali, ali je neophodno da ima 3 kanala kako bi mogla da se kombinuje sa CT slikom u koju ćemo uneti boju. U promenljivu b1 učitati sliku 2_PET.png u režimu sive skale i invertovati je. Uneti boju u sliku primenom kolormape. Dobar izbor za medicinske slike su JET i PARULA, a solidan rezultat daju i HOT i COOL. Na kraju promeniti redosled kanala boje iz BGR u RGB. Prikazati slike.  
  3.4 Sjedinite dve slike mešanjem koristeći različite faktore k i prikazati dobivenu sliku. Da li je rezultat sjedinjavanja u boji bolji nego sjedinjavanje u sivoj skali? Kako se menja rezultujuća slika sa različitim faktorima k?

## 4. CIELAB kolor prostor  
  4.1 Osim u RGB, sjedinjavanje je moguće raditi i u nekom drugom prostoru boja, pri čemu je potrebno je definisati vrednosti komponenti boje definisanih u tom prostoru. CIELAB prostor je definisan preko osvetljaja L* i oponenata a* (zelena-crvena) i b* (plava-žuta). Kanal L* ćemo definisati kao nivo intenziteta u slici anatomskog modaliteta, pa u promenljivu L treba učitati sliku 2_CT.png. Jedan od kanala boje definišemo slikom funkcionalnog modaliteta, te u promenljivu a učitati sliku 2_PET.png. Kanal b definisati kao proizvoljnu vrednost (isprobati 0 i 100). U openCV vrednosti komponenti L*a*b* su u opsegu [0, 255].  
  4.2 Napraviti sliku im_c kombinovanjem ovako definisanih kanala.
4.3 Sjedinjenu sliku prikazati u RGB domenu.
