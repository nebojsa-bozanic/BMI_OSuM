[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba8%3A%20Obrada%20rendgenske%20slike%3A%20Suzbijanje%20%C5%A1uma%202/OSuM_vezba_8.ipynb)

# Laboratorijska vežba 8: Obrada rendgenske slike: Suzbijanje šuma 2

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, pywt, bm3d, os, scipy.ndimage.filters (convolve1d), osum

## 1. Modifikacije sigmoidalne krive za multiveličinsko pojačanje

Ako pretpostavimo da na višim nivoima piramide dominira šum, multiveličinsko pojačanje struktura običnom sigmoidalnom krivom dodatno pojačava šum na tim nivoima. Uvodimo dve modifikacije sigmoidalne krive kako bismo prevazišli ovaj problem. Ublaženo pojačanje

  1.1 U modulu osum napraviti funkciju sigmLUT_lin modifikacijom sigmLUT tako da niske vrednosti budu mapirane linearno. Ulazni parametri funkcije su ulazni opseg, izlazni opseg, nagib i procenat opsega oko nule koji se transformiše linearno.  
  1.2 U skripti v8_1.py Napraviti LUT za običnu sigmoidalnu transformaciju kojom se transformiše ulazni opseg -2000 do 2000 u opseg -800 do 800 sa nagibom 7. Prikazati LUT.  
  1.3 Napraviti LUT za modifikovanu sigmoidalnu transformaciju sa linearnim delom koristeći iste parametre kao u prethodnoj tački i 6% opsega koji se transformiše linearno. Prikazati ovaj LUT.  
  1.4 Učitati sliku Ro_01.fxd i uraditi logaritamsku kompresiju opsega (im_log).  
  1.5 Napraviti Laplasovu piramidu i primeniti napravljene LUT za pojačanje detalja na prvom nivou.  
  1.6 Rekonstruisati slike, prikazati ih i analizirati razlike.  
  1.7 Isprobati različite vrednosti parametra t u sigmLUT_lin. Takođe isprobati sve na 2. nivou i na prvom i drugom nivou u isto vreme. Direktno potiskivanje šuma  
  1.8 Druga modifikacija sigmoida podrazumeva da se niski koeficijenti potpuno potisnu, tj. da se svedu na 0. U modulu osum napraviti funkciju sigmLUT_z u kojoj se implementira ova modifikacije. Ulazni parametri su ulazni opseg, izlazni opseg, nagib i procenat opsega oko nule koji se suzbija.  
  1.9 Napraviti LUT za ovu modifikovanu sigmoidalnu transformaciju sa parametrima kao u 1.3. Prikazati LUT i uporediti ga sa običnom sigmoidalnom transformacijom.  
  1.10 Primeniti ovaj LUT na prvi nivo LP, rekonstruisati sliku i analizirati je.  
  1.11 Isprobati različite vrednosti parametra t u sigmLUT_z. Takođe isprobati sve na 2. nivou i na prvom i drugom nivou u isto vreme.

## 2. Procena šuma iz vejvlet piramide  

Deo opsega koji se suzbija u modifikovanim sigmoidalnim krivama može se preciznije proceniti kao (umnožak) standardne devijacije šuma. Dijagonalni koeficijenti najviših nivoa vejvlet piramide potiču skoro potpuno od šuma što se može iskoristiti za procenu std.

  2.1 U promenljivu im2 učitati sliku abdomen.png i razložiti je u vejvlet piramidu sa 2 nivoa koristeći vejvlet db4.  
  2.2 Proceniti standardnu devijaciju šuma sa dijagonalnih koeficijenata prvog nivoa piramide koristeći formulu:
𝜎! = 𝑚𝑒𝑑𝑖𝑎𝑛(|𝐷"|) 0.6745
  2.3 Modifikovati sigmLUT_z tako da je moguće uneti apsolutnu vrednost intenziteta ispod koga će koeficijenti biti suzbijeni.  
  2.4 Napraviti LUT za sigmoidalno pojačanje i LUT sa direktnim potiskivanjem šuma koristeći parametre ip_range=1000, op_range=800, k=7 i nivo intenziteta 3𝜎!.  
  2.5 Rekonstruisati slike sa modifikovanim prvim nivoom vejvlet piramide u dijagonalnom pravcu i uporediti ih.

## 3. Sličnost po blokovima  
  3.1 U skripti v8_2.py u promenljivu im učitati sliku abdomen_crop.png.  
  3.2 Primenti Non-local Means filtar na sliku im koristeći parametre templateWindowSize=11, searchWindowSize=11, n=9. Prikazati dobijenu sliku I uporediti je sa slikom pre filtriranja.  
  3.3 Primeniti bm3d filtar na sliku im. Primeniti oba stepena (filtraciju pragovanjem i Vinerov filtar), a standardnu devijaciju proceniti na osnovu dijagonalnih koeficijenata prvog nivoa vejvlet piramide (kao u prethodnom delu). Prikazati sliku pre i posle filtriranja.  

## 4. Temporalno filtriranje  
  4.1 U skripti v8_3.py učitati fluoroskopsku sekvencu iz foldera Img_1 u 3D matricu im_sekv  
  4.2 Napraviti LUT za logaritamsku kompresiju opsega sa ulaznim i izlaznim opsegom 2"# i tolerancijom ulaznog opsega 0.1 %  
  4.3 Definisati parametre za pravljenje video zapisa  
  4.4 U for petlji učitati frejm po frejm i primeniti log kompresiju opsega. Invertovati vrednosti i upisati frejm u video sekvencu u opsegu uint8  
  4.5 Definisati 1D Gausov filtar sa parametrima n=11 i sigma=2. Primeniti ovaj filtar za filtriranje sekvence kroz vreme (temporalno filtriranje) i sačuvati je u im_f.
4.6 Napravit video zapis od sekvence im_f.
