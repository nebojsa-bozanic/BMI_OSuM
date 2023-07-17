[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/OSuM/blob/master/Vezba3%3A%20Multiveli%C4%8Dinska%20analiza%3A%20Gausova%20i%20Laplasova%20piramida/OSuM_vezba_3.ipynb)

# Laboratorijska vežba 3: Multiveličinska analiza: Gausova i Laplasova piramida

Potrebne biblioteke: math, scipy, cv2, numpy, matplotlib.pyplot

## 1. Gausov filtar  
  1.1 U modulu osum.py napisati funkciju gaussian koja pravi 1D Gausov filtar. Parametri filtra su broj odbiraka (n) i standardna devijacija (sigma). Definisati default-ne vrednosti za parametre. Proizvoljno, izlaz funkcije takođe može biti i x-osa za crtanje grafika. Jednodimenzionalni Gausov filtar dat je izrazom:  
  
  $$ G(x) = \frac{1}{\sqrt{2 \pi σ^2}} e^{- \frac{x^2}{2 \sigma^2}} $$
  
  1.2 U glavnoj skripti vezba3.py pomoću prethodno definisane funkcije napraviti Gausov filtar f sa parametrima n=7 i sigma=1.5. Koliko iznosi vrednost centralnog, a koliko vrednost ugaonih koeficijenata (odbiraka) ovog filtra?  
  1.3 Prikazati koeficijente ovog filtra.  
  1.4 Isprobati nekoliko različitih kombinacija n i sigma. Kakav efekat imaju ovi parametri na izgled filtra i vrednosti njegovih koeficijenata?  
  1.5 Napraviti 2D Gausov filtar vektorskim množenjem 2 1D filtra. Koliko iznose njegovi koeficijenti?  
  1.6 Prikazati 2D filtar. Kako izgleda ovaj filtar?  

## 2. Redukcija  
  2.1 U glavnom modulu vezba3.py učitati sliku mr_glava_10.jpg u promenljivu im. Slika je tipa uint8.  
  2.2 Promeniti tip slike u float32, a zatim je isfiltrirati niz vrste koristeći Gausov filtar definisan u koraku 1.5. Filtriranje raditi konvolucijom. Isfiltriranu sliku sačuvati u promenljivu a_f.  
  2.3 Napraviti sliku a_f2 decimacijom a_f sa faktorom 2 niz vrste (odbaciti svaku drugu kolonu).  
  2.4 a_f2 filtrirati niz kolone, pomoću operacije konvolucije, koristeći filtar f. Isfiltriranu sliku sačuvati u promenljivu b_f.  
  2.5 Zatim sliku b_f decimirati faktorom 2 niz vrste, tj. odbaciti joj svaku drugu kolonu. Time se dobija slika b_f2.  
  2.6 U osum.py modulu napraviti funkciju im_norm za normalizaciju slika na opseg [0,1].2.7 Prikazati sliku nakon svakog koraka 2.2-2.5. Preporuka je da se prikazuju normalizovane slike. Kojih su dimenzija slike. Šta predstavlja slika b_f2? Kako se razlikuje od originalne slike?

## 3. Ekspanzija  
  3.1 Upisati vrstu nula iza svake vrste slike b_f2. Novu sliku nazvati c.  
  3.2 Filtrirati sliku c niz kolone filtrom 2f, koristeći konvoluciju. Sačuvati isfiltriranu sliku u promenljivu c_f.  
  3.3 Sada iza svake kolone slike c_f dodati kolonu nula. Sliku sačuvati kao promenljivu d.  
  3.4 Sliku d_f napraviti filtriranjem slike d filtrom 2f niz vrste.  
  3.5 Prikazati sliku nakon svakog koraka. Kako se menjaju dimenzije slike? Koje efekte primećujete nakon svakog koraka?  
  3.6 Napraviti prvi nivo Laplasove piramide kao razliku im i d_f.  
  3.7 Prikazati ovu sliku. Kako izgleda slika? Šta predstavljaju najsvetliji i najtamniji pikseli a šta srednji nivoi sivog?  
  3.8 Prikazati apsolutnu vrednost ove slike? Šta se vidi na njoj?

## 4. Piramide  
  4.1 Isprobati funkcije za ekspanziju i redukciju iz openCV biblioteke.  
  4.2 Iskoristiti ove funkcije za pravljenje funkcije im_pyr_decomp u modulu osum.py za razlaganje slike na piramide. Ulaz funkcije treba da bude slika i nivo razlaganja N, a izlaz Laplasova, Gausova piramida i rezidual (bazna slika).  
  4.3 U glavnom modulu napraviti 3 nivoa Gausove i Laplasove piramide slike im. Radi poboljšanja prikaza, nivoe Laplasove piramide pre prikazivanja pomnožiti sa 5 i dodati im 128 i sliku prikazati na opsegu [0, 255]. Šta prikazuje Gausova, a šta Laplasova piramida? Šta se menja na svakoj iz nivoa u nivo?  
  4.4 U modulu osum.py napraviti funkciju im_pyr_recon za rekonstrukciju slike pomoću Laplasove piramide i bazne slike.  
  4.5 Rekonstruisati sliku im koristeći njenu nepromenjenu Laplasovu piramidu i rezidual. Kvantifikovati kvalitet rekonstrukcije sumom apsolutnih razlika između originalne i slike dobijene rekonstrukcijom. Koliko iznosi suma apsolutnih vrednosti i šta se može zaključiti iz tog rezultata?  

## 5. Manipulacija Laplasove piramide  
  5.1 Pomnožiti svaki nivo Laplasove piramide ponaosob faktorom 2 i zatim rekonstruisati sliku koristeći tako modifikovanu piramidu. Prikazati originalnu sliku i slike dobijene nakon rekonstrukcije nakon modifikacije svakog od nivoa. Šta je efekat ove modifikacije i kako se manifestuje na različitim nivoima? Da li je rekonstrukcija idealna?  
  5.2 Ponoviti korake iz 5.1 koristeći faktor 5. Šta se promenilo?  
  5.3 Za svaki nivo Laplasove piramide ponaosob, postaviti sve koeficijenta koji imaju apsolutnu vrednost manju od 10 na 0. Rekonstruisati sliku nakon modifikacije svakog nivoa i prikazati je. Koji je efekat ove modifikacije? Šta se dešava kada se suzbiju malikoeficijenti na nižim, a šta navišim nivoima? Kakav je efekat na šum, a kakav na kontrast?  
  5.4 Ponoviti korake iz 5.3 koristeći prag 30. Analizirati efekte.
