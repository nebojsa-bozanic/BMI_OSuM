[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba12%3A%20Perspektivne%20transformacije%20i%20kruta%20registracija/OSuM_vezba_12.ipynb)

# Laboratorijska vežba 12: Perspektivne transformacije i kruta registracija

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, osum

## 1. Odabiranje (interpolacija) referentnog regiona za registraciju  
  1.1 U promenljivu r učitati referentnu sliku REG_HE.png, a u promenljivu t učitati test sliku po izboru REG_LE_0X.PNG. Prikazati slike. Sve test slike su translirane po x i/ili y-osi u odnosu na referentnu.  
  1.2 Izdvojiti region pluća (region of interest - ROI) od 15% do 75% visine slike i 10% do 90% širine slike.  
  1.3 Interpolirati referentnu sliku u domenu koji definiše ROI, tako da se između svakog postojećeg piksela da unese dodatna lokacija. Koristiti bilinearnu metodu interpolacije.  
  1.4 Interpolirati referentnu sliku na indeksima (lokacijama) od 500 do 800 po x i y koordinati. Budući da ove lokacije izlaze iz prostora u kome je definisana referentna slika, potrebno je definisati ekstrapolacionu vrednost (npr. neka iznosi 100).  
  1.5 Na domenu koji definiše ROI interpolirati referentnu i test sliku i izračunati koliko iznosi suma njihovih apsolutnih razlika.  
  1.6 Kako bi se uhvatile razlike u strukturi, a ne u osvetljaju, ponoviti korak 1.5 sa z-normalizovanim slikama, izabrati proizvoljne parametre. Kako se promenila suma apsolutnih razlika?

## 2. Perspektivne transformacije  
  2.1 Test slika je translirana u odnosu na referentnu, pa ju je potrebno transformisati (translirati) kako bi se geometrijski poklopila sa referentnom slikom. Zapravo se translira definisani region na test slici. Nakon odabiranja referentne slike potrebno je modifikovati koordinate [x, y] na kojima se odabira test slika tako da im se doda neki proizvoljni pomeraj, npr. (2,3). Pomeranje se mora uraditi odvojeno: x_tr = x + 2; y_tr = y + 3. Raditi sa z-normalizovanim slikama. Da li nakon translacije suma apsolutnih razlika između ROI-a referentne i test slike veća ili manja i šta taj rezultat znači?  
  2.2 Za registraciju naše test slike na referentnu dovoljna nam je transformacija translacijom, međutim postoje i druge perspektivne transformacije koje se mogu primeniti u registraciji. Rotirati referentnu sliku prvo oko koordinatnog početka u gornjoj levoj tački slike, a zatim oko centra slike, za proizvoljni ugao. Koordinate slike nakon rotacije oko proizvoljne tačke za ugao 𝜃 u radijanima definisane su sledećom transformacijom formula  
  2.3 Uveličati (umanjiti) sliku proizvoljnim faktorom s (uveličanje iznosi 1/s) prvo iz koordinatnog početka u gornjem levom uglu, a zatim iz centra slike. Transformacija uveličanjem je definisana na sledeći način: formula  

## 3. Kruta registracija translacijom  
  3.1 Napraviti GUI preko koga korisnik može da definiše referentni ROI za registraciju klikom na gornji levi, a zatim na donji desni ćošak regiona od interesa. Prikazati izabrani region.  
  3.2 Interpolirati z-normalizovanu referentnu sliku na izabranom regionu.  
  3.3 Naći optimalne pomeraje po x i y-osi tako da se minimalizuje suma apsolutnih razlika između slika. Isprobati pomeraje od -20 do 20 i po x i po y-osi. Za svaku kombinaciju pomeraja modifikovati koordinate [x, y] i na njima interpolirati test sliku, a zatim izračunati sumu apsolutnih razlika između z-normalizovane referentne slike I z-normalizovane translirane test slike. Sačuvati vrednosti objektivne funkcije u matricu d (iz koje na osnovu indeksa vrsta i kolona možemo doći do pomeraja po x i y-osi za koje je ostvarena određena vrednost objektivne funkcije).  
  3.4 Pronaći indekse na kojima se nalazi minimalna vrednost objektivne funkcije u matrici d i na osnovu njih izračunati optimalne pomeraje po x i y-osi. Proveriti da li je to u skladu sa izgledom test slike (gde se nalaze crne linije na obodu).  
  3.5 Prikazati optimizacionu površinu.
