[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/OSuM/blob/master/Vezba1%3A%20Osnovne%20manipulacije/OSuM_vezba_1.ipynb)

# Laboratorijska vežba 1: Osnovne manipulacije

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, pydicom

## 1. Učitavanje, prikaz i snimanje slike  
  1.1 U promenljivu im1 učitati sliku mr_glava_1.jpg u odgovarajućem režimu za sliku u sivoj skali.  
  1.2 Sliku im1 prikazati koristeći funkcije iz cv2 biblioteke.  
  1.3 Sliku im1 prikazati koristeći funkcije iz matplotlib.pyplot biblioteke.  
  1.4 Napraviti sliku im2 indeksiranjem slike im1. Iz im1 iseći piksele [100:200, :]. Koliko vrsta ima slika im2?  
  1.5 Sačuvati sliku im2 pod nazivom mr1_crop.jpg.
   
## 2. Tipovi podataka i dubina sive skale  
  Dva osnovna tipa podataka kojima su predstavljeni pikseli slike:  
    1. float – može da prikaže decimalne vrednosti  
    2. integer – celobrojne vrednosti  
  Znak: unsigned (uint) – prikazuje nenegativne vrednosti signed (int) – prikazuje i negativne vrednosti  
  Veličina: 8, 16, 32… - broj bita kojim je predstavljen jedna piksel  
  2.1 U promenljivu im3 učitati sliku rtg_2.png. U pitanju je uint16 slika, pa je potrebno izabrati odgovarajući režim.  
  2.2 Koja je dubina sive skale uint8, int8, a koja uint16 tipa?  
  2.3 Prikazati sliku im3 vodeći računa o granicama dinamičkog opsega.

## 3. Slika razlika  
  3.1 U promenljivu im4 učitati sliku mr_glava_2.jpg u režimu za sliku u sivoj skali.  
  3.2 Napraviti sliku razlika im_r1 oduzimanjem im1 i im4. Analizirati vrednosti piksela te slike. Da li su dobijene vrednosti tačne?  
  3.3 Promeniti tip slika im1 i im4 u int16 (ili neki drugi kojim mogu da se zapišu negativne vrednosti i odgovarajući opseg) i napraviti sliku razlika im_r2. Koje su sada vrednosti piksela?  
  3.4 Prikazati sliku im_r2. Definisati granice dinamičkog opsega za prikaz.  
  3.5 Napraviti sliku apsolutnih razlika im_r3 i prikazati je. Kako se razlikuju slike im_r2 i im_r3?  
  3.6 Napraviti sliku im_n normalizaijom vrednosti im_r3 na opseg [0, 1]. Kog tipa je ova slika? Prikazati sliku.  

## 4. Matematičke operacije  
  4.1 Napraviti sliku im1_2 dodavanjem vrednosti 200 na svaki piksel im1. Voditi računa o opsegu vrednosti nove slike pa u skladu sa tim izabrati odgovarajući tip.  
  4.2 Napraviti sliku im1_3 oduzimanjem vrednosti 200 od svakog piksela slike im1. Voditi računa o opsegu vrednosti nove slike pa u skladu sa tim izabrati odgovarajući tip.  
  4.3 U jednom prozoru prikazati sliku im1, im2 i im3. Izabrati granice dinamičkog opsega za prikaz tako da je moguće uporediti ove slike. Kakav je efekat povećanja, a kakav smanjenja vrednosti piksela?  
  4.4 Sliku im1 skalirati množenjem sa 3.5 i deljenjem sa 1.5. Koji su efekti?

## 5. Osnovne statistike slike  
  5.1 Odrediti minimum i maksimum slike im1. Koji je opseg slike?  
  5.2 Odrediti srednju vrednost slike im1. Šta možemo zaključiti na osnovu ove vrednosti?  
  5.3 Odrediti varijansu i standardnu devijaciju slike im1. U kojoj su vezi varijansa standardna devijacija?  

## 6. Histogram  
  6.1 Napraviti histogram slike im1 u opsegu od 0 do 255 sa korakom 1. Koliko odbiraka ima u ovom vektoru? Prikazati histogram.  
  6.2 Napravit normalizovani histogram? Šta je normalizovani histogram? Prikazati ga.  
  6.3 Koliki udeo (%) slike im1 ima vrednost 206?  
  6.4 Koliki udeo (%) slike im1 ima vrednost ispod 200?

## 7. Osnovne manipulacije nad DICOM fajlovima  
  7.1 Učitati fajl 00044.dcm u promenljivu dc i ispisati je na ekranu. Analizirati kako su predstavljeni podaci.  
  7.2 Izbrisati atribut PatientID iz promenljive dc.  
  7.3 Anonimizovati DICOM fajl tako što ćete zameniti PatientName praznim stringom i dodati proizvoljni PatientID. Sačuvati ove izmene u 00044_1.dcm  
  7.4 Pristupiti atributu PatientID pomoću njegovor taga [0x0010, 0x0020].  
  7.5 Iz DICOM fajla izvući sliku u promenljivu im. Prikazati sliku vodeći računa o granicama dinamičkog opsega. Koji modalitet snimanja je u pitanju? Proveriti pretpostavku analizom atributa Modality u promenljivoj dc (tag [0x0008, 0x0060]).
