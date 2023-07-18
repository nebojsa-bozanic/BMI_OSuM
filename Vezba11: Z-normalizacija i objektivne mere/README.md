[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba11%3A%20Z-normalizacija%20i%20objektivne%20mere/OSuM_vezba_11.ipynb)

# Laboratorijska vežba 11: Z-normalizacija i objektivne mere

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, osum, skimage.metrics.structural_similarity

## 1. Globalna z-normalizacija  
  1.1 U skripti v11_1.py u promenljivu im1 učitati sliku REG_HE.png, a u promenljivu b učitati sliku REG_LE_X.jpg (izabrati iz skupa). Prikazati ih i zaključiti kako se one razlikuju. Prikazati sliku apsolutnih razlika. Izračunati sumu apsolutnih razlika i apsolutnu razliku srednjih vrednosti slika (razlika prosečnih osvetljaja).  
  1.2 Napraviti njihove histograme i prikazati ih na istom grafiku. Po čemu se razlikuju histogrami?  
  1.3 Normalizovati slike im1 i im2 tako da im se poklapaju globalne statistike, tj. da srednja vrednost bude 0 a standardna devijacija 1 (globalna z-normalizacija). Srednja vrednost se postavlja na 0 oduzimanjem početne srednje vrednosti od svih piksela. Standardna devijacija se postavlja na 1 deljenjem svakog piksela sa početnom standardnom devijacijom (koja se može računati kao koren iz varijanse).  
  1.4 Prikazati slike nakon z-normalizacije. Da li su sada slike sličnije? Kako sada izgleda slika apsolutnih razlika? Koliko iznose srednje vrednosti i standardne devijacije nakon z-normalizacije? Koliko iznosi suma apsolutnih razlika i apsolutna razlika srednjih vrednosti slika?  
  1.5 Prikazati histograme slika nakon z-normalizacije na istom grafiku. Da li su sada sličniji?

## 2. Lokalna z-normalizacija  

Preko Gausovog filtra  

  2.1 U skripti osum.py napraviti funkciju z_norm koja radi lokalnu z-normalizaciju (ujednačava statistiku po lokalnim regionima slike). Ulazni parametri funkcije su slika, dužina Gausovog filtra d, standardna devijacija filtra s i prag za varijansu pr. Izlaz je slika nakon lokalne z-normalizacije. Prvo je potrebno izračunati lokalnu srednju vrednost slike. Slika isfiltrirana Gausovim filtrom predstavlja procenu lokalne srednje vrednosti, tj. srednje vrednosti u regionu koji obuhvata filtar oko svakog piksela. Od originalne slike oduzeti ovako napravljenu sliku lokalne srednje vrednosti. Globalna varijansa se računa kao $var(X) = E[(X – μ)^2]$, gde je $E[X]$ srednja vrednost $X$. Lokalna varijansa se računa tako što se od slike oduzme lokalna srednja vrednost, zatim se rezultat kvadrira i računa se lokalna srednja vrednost od tog kvadrata pomoću Gausovog filtra. Z-normalizacija podrazumeva deljenje sa standardnom devijacijom (korenom iz varijanse), što može biti problematično kada je ta vrednost jako mala ili čak 0 (šum na pozadini koji ima malu std). Zbog toga je potrebno ograničiti varijansu da ne pada ispod određenog praga pr. Lokalna z-normalizacija se radi tako što se od slike oduzme lokalna srednja vrednost i podeli se sa lokalnom standardnom devijacijom koja se računa kao koren iz lokalne varijanse.  
  2.2 Primeniti funkciju z_norm na slike im1 i im2 i prikazati ih. Isprobati različite vrednosti parametara. Kako izgledaju lokalno z-normalizovane slike u odnosu na originalne i globalno z-normalizovane? Kako različiti parametri i njihove kombinacije utiču na izgled slika? Prikazati sliku apsolutnih razlika i uporediti je sa slikom apsolutnih razlika pre z-normalizacije i nakon globalne z-normalizacije.  
  2.3 Koliko iznosi globalna srednja vrednost i standardna devijacija slika? Koliko iznosi suma apsolutnih razlika između slika i apsolutna razlika srednjih vrednosti? Da li je manja ili veća nego između globalno z-normalizovanih slika? Zbog čega je došlo do promene? Preko integralnih slika  
  2.4 Za računanje lokalne srednje vrednosti mogu se koristiti integralne slike. Piksel u integralnoj slici predstavlja sumu intenziteta piksela koji se nalaze gore i levo od njega. U skriptu osum.py napraviti funkciju integral_img koja za datu ulaznu sliku pravi njenu integralnu sliku. 
  
  <p align="center">
  <img width="340" height="180" src="https://github.com/nebojsa-bozanic/BMI_OSuM/assets/28110404/7135a525-8282-4e83-b18f-a7b8cf605ef3">
</p>
  Slika 1. Piksel u integralnoj slici predstavlja sumu regiona iznad i levo od njega. Različitim bojama je objašnjeno indeksiranje u z_norm2 (2.5)  

  2.5 U skriptiosum.py napraviti funkciju z_norm2 koja radi lokalnu z-normalizaciju koristeći integralne slike za računanje lokalne srednje vrednosti. Suma lokalnog regiona može se izračunati pomoću 4 piksela (ćoškovi regiona) u integralnoj slici i operacija sabiranja i oduzimanja. Srednja vrednost dobija se deljenjem sume sa brojem elemenata, što je određeno veličinom regiona k (ulazni parametar funkcije).  
  2.6 Primeniti funkciju z_norm na slike im1 i im2 i prikazati ih. Kako izgledaju lokalno z-normalizovane slike u odnosu na originalne i globalno z-normalizovane?  
  2.7 Koliko iznosi globalna srednja vrednost i standardna devijacija slika? Koliko iznosi suma apsolutnih razlika između slika i apsolutna razlika srednjih vrednosti? Da li je manja ili veća nego između globalno z-normalizovanih slika? Zbog čega je došlo do promene?  

## 3. Objektivne mere
  3.1 U skripti v11_2.py učitati 3 proizvoljne mr_0x.png slike u promenljive im1, im2 i im3.  
  3.2 Izračunati sumu kvadrata razlika između im1 i im2, a zatim između im1 i im3. Koja slika je sličnija slici im1? Izračunati i sumu kvadrata razlika po pikselu.  
  3.3 Izračunati sumu apsolutnih razlika između im1 i im2, a zatim između im1 i im3. Koja slika je sličnija slici im1? Izračunati i sumu apsolutnih razlika po pikselu. Kako se rezultati razlikuju od sume kvadrata razlika?  
  3.4 U skripti osum.py napraviti funkciju mutual_information koja implementira zajedničke informacije između slika (mera sličnosti), po formuli
  
  $$ NMI(X, Y) = \sum \sum p(X, Y) log \frac{p(X, Y)}{p(X)p(Y)} $$
  
  pri čemu $p(X, Y)$ je združena verovatnoća $X$ i $Y$ (normalizovani 2D histogram slika X i Y), a $p(X)$, $p(Y)$ marginalne verovatnoće po $X$ i $Y$. Računati samo nenulte odbirke u 2D histogramu.  
  3.5 U promenljive im4 i im5 učitati slike 2_CT.png i 2_PET.png. Izračunati zajedničke informacije između ovih slika. Ponoviti postupak sa invertovanom slikom im4. Uporediti sa rezultatima koji se dobijaju sa nekom od statističkih mera, npr. sumom apsolutnih razlika. Da li zajedničke informacije mere statističku ili strukturnu sličnost?  
  3.6 U skripti osum.py napraviti funkciju normalized_mutual_information u kojoj se implementira mera normalizovane zajedničke informacije, po formuli 

  $$ NMI(X, Y) = 1 - \frac{MI(X, Y)}{max(H(X), H(Y))'} $$
  
  gde su $H(X)$ i $H(Y)$ entropije slika X i Y.  
  3.7 Izračunati normalizovane zajedničke informacije između slika im4 i im5. Ponoviti postupak sa invertovanom slikom im5. Uporediti sa rezultatima koji se dobijaju sa nekom od statističkih mera, npr. sumom apsolutnih razlika. Da li normalizovane zajedničke informacije mere statističku ili strukturnu sličnost?  
  3.8 Pronaći indeks strukturne sličnosti slika im1 i im2, a zatim im2 i im3. Koja slika je sličnija im1? Prikazati slike lokalnih sličnosti za obe kombinacije i izanalizirati ih. Da li su slike slične po kriterijumu koji koristi ova mera?  
  3.9 Izračunati gradijentnu meru QAB koristeći funkciju osum.imq_qab između slika im1 i im2. Prikazati sliku lokalnih sličnosti qab_im i mapu značaja w. Da li su slike slične po kriterijumu koji koristi ova mera?
