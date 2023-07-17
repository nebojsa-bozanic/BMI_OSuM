[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba9%3A%20Obrada%20rendgenske%20slike%3A%20Toniranje%20snimaka/OSuM_vezba_9.ipynb)

# Laboratorijska vežba 9: Obrada rendgenske slike: Toniranje snimaka

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, pydicom, osum

## 1. Logaritamska kompresija i MSE  
  1.1 Učitati sirovu sliku Ro_01.fxd i uraditi logaritamsku kompresiju opsega (im_log).  
  1.2 Od slike im_log napraviti Laplasovu piramidu od 4 nivoa.  
  1.3 Detalje na prvom nivou pojačati sigmoidalnom transformacijom sa direktnim potiskivanjem šuma (lazni opseg -2000 do 2000, izlazni opseg -800 do 800, nagib 7 i ukupno 10 % vrednosti oko nule suzbiti). Detalje na drugom nivou pojačati sigmoidalnom transformacijom sa ublaženim pojačanjem (isti parametri kao prethodno). Na treći i četvrti nivo primeniti običnu sigmoidalnu transformaciju, ali detalje na trećem pojačati više (nagib 7) nego na četvrtom nivou (nagib 3).
  1.4 Rekonstruisati ovako izmenjenu piramidu u sliku im_mse i prikazati tu sliku.

## 2. Linearno toniranje  
  2.1 Napraviti i prikazati histogram im_mse.  
  2.2 Vizuelnom analizom histograma odraditi granice za toniranje.  
  2.3 Primeniti granice toniranja tako da sve ispod donje i sve iznad gornje ode u zasićenje. Takođe invertovati sliku kako bi se dobio uobičajeni prikaz rtg slike i korigovati izlazni opseg na [0, 255]. Dobijenu sliku nazvati im_ts1. Prikazati sliku.  
  2.4 Prikazati sliku im_ts1.  
  2.5 Napraviti kumulativnu sumu normalizovanog histograma i analizirati je paralelno sa normalizovanim histogramom. Šta predstavljaju vrednosti na ovom grafiku?  
  2.6 U modulu osum napraviti funkciju stat_hist_lims_fromh koja vraća granice intenziteta za toniranje na osnovu prosleđene količine (procenta) najsvetlijih i najtamnijih piksela koje želimo da odvedemo u zasićenje. Ulazni parametri funkcije su još i normalizovani histogram i vektor granica histograma.  
  2.7 Pomoću funckije napravljene u prethodnom koraku pronaći Lmin i Lmax tako da se 0.1% najtamnijih i 1% najsvetlijih intenziteta odvede u zasićenje (isporbati posle različite parametre i pratit promene). Koliko se razlikuju ovako dobijene vrednosti  Lmin i Lmax i one korišćene u 2.2? Koristeći ove granice tonirati sliku (kao u 2.3) i smestiti je u promenljivu im_ts2. Prikazati sliku.  
  2.8 Učitati DICOM fajl 00044.dcm i istonirati CT sliku koja se nalazi u njemu koristeći vrednosti atributa W (WindowWidth) i L (WindowCenter). Slika se tonira tako da se zadrži opseg sa centrom u L širine W, a ostatak se odvodi u zasićenje. Takođe je u pitanju linearno toniranje, ali se Lmin i Lmax indirektno definišu, preko L i W. Prikazati sliku pre i nakon toniranja. Da li se poboljšao prikaz nakon toniranja?

## 3. Sigmoidalno toniranje  
  3.1 U modulu osum napraviti funkciju ts_sigma koja implementira sigmoidalno toniranje. Ovakva transformacija treba dodatno da razvuče kontrast u svom centralnom delu. Transformaciju treba implementirati preko LUT. Ulazni parametri funkcije su slika koja se tonira, vektor parametara kapa (kontroliše nagib) i sigma (pomera sigmoid levo-desno) i gornja granica izlaznog opsega.  
  3.2 Primentiti ovu funkciju na im_mse kako bi se dobila im_ts3. Koristiti paramtere kapa=0.5 i sigma=3 (možete isprobati i druge vrednosti) i gornju granicu izlaznog opsega 4096. Prikazati sliku nakon toniranja.
