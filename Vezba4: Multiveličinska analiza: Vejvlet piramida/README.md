[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba4%3A%20Multiveli%C4%8Dinska%20analiza%3A%20Vejvlet%20piramida/OSuM_vezba_4.ipynb)

# Laboratorijska vežba 4: Multiveličinska analiza: Vejvlet piramida

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, pywt (PyWavelets), dtcwt

## 1. Diskretna vejvlet transformacija
  1.1 Napraviti skriptu dwt.py i u njoj učitati sliku mr_glava_1.jpg.  
  1.2 Primeniti 2D diskretnu vejvlet transformaciju kojom se dobija vejvlet piramida sa jednim nivoom. Koristiti db1 vejvlet. Izvući koeficijente u piramide u zasebne slike. Šta koja slika predstavlja?
  1.3 Prikazati piramidu koristeću subplot funkciju. Položaj koeficijenata je prikazan na slici ispod:

<p align="center">
  <img width="184" height="105" src="https://github.com/nebojsa-bozanic/BMI_OSuM/assets/28110404/fca864ec-e185-4bfc-ad35-4d0d0ff8cd81">
</p>
  
  1.4 Rekonstruisati piramidu. Prikazati rekonstruisanu sliku i odrediti sumu apsolutnih razlika između originalne i rekonstruisane slike. Da li rekonstrukciju možemo smatrati idealnom?  
  1.5 Od iste ulazne slike napraviti vejvlet piramidu sa 3 nivoa. Koristiti db1 vejvlet. Pre formiranja slike piramide zameniti položaj cV i cH koeficijenata na svakom nivou, kako bi piramida bila organizovana na način prikazan iznad. Za potrebe prikaza normalizovati opseg (rekonstrukciju raditi sa nenormalizovanim koeficijentima). Analizirati šta se vidi na višim, a šta na nižim rezolucijama u sva tri pravca.  
  1.6 Promeniti tip vejvleta (db2, db3, db5, haar…) i dubinu razlaganja. Koje efekte primećujete? Kako izgleda piramida dobijena db1, a kako db5 vejvletom?  
  1.7 Ponoviti korake iz 1.5 i 1.6 na slici knee.tif.

## 2. Kompresija  
  2.1 U skriptu kompresija.py učitati sliku 1_MR.jpg i od nje napraviti vejvlet piramidu od 4 nivoa koristeći db1 vejvlet.  
  2.2 Pronaći prag intenziteta ispod koga se nalazi 90 % koeficijenata vejvlet piramide i svasti na 0 one čija je apsolutna vrednost manja od t (zadržati 10 % koeficijenata).  
  2.3 Rekonstruisati sliku sa preostalih 10 % koeficijenata i uporediti je sa originalnom.  
  2.4 Prethodne korake ponoviti tako da se zadrži 5, 1 i 0.5 % koeficijenata.  
  2.5 Ponoviti prethodna 4 koraka za sliku knee.tif.
  
## 3. Dual Tree kompleksna vejvlet transformacija  
  3.1 Napraviti skriptu dt_kompl_vejvlet.py i od slike 1_MR.jpg napraviti Dual Tree kompleksnu vejvlet piramidu od 2 nivoa.  
  3.2 Prikazati moduo i argument za sve orijentacije i za sve rezolucije. Na kojim slikama se može uočiti orijentacija detalja?
