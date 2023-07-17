# Laboratorijska vežba 2: Manipulacije nad 3D slikom

Potrebne biblioteke: pydicom, cv2, numpy, matplotlib.pyplot, matplotlib.widgets

## 1. Video iz DICOM fajla  
  1.1 Učitati DICOM fajl 0002.dcm i u posebnu promenljivu izvući atribut koji se odnosi na snimak, tj. sekvencu snimaka u ovom primeru. Koje su dimenzije te promenljive? Koji je modalitet snimanja u pitanju?  
  1.2 Reorganizovati redosled dimenzija tako da se dimenzija koja se odnosi na vreme nalazi na poslednjem mestu. (Ovaj korak nije neophodan.)  
  1.3 Sačuvati učitanu angiografsku sekvencu u video fajl videoXA.avi.  
  1.4 Prikazati video napravljen u prethodnom koraku.

## 2. Učitavanje 3D slike  
  2.1 Napraviti novi modul slika_3d.py i u njemu funkciju imread_3d za učitavanje 3D slike u formatu .img sa propratnih .hdr fajlom.  
  2.2 U glavnom modulu učitati sliku iz fajlova 01006_t1_cma.img i 01006_t1_cma.hdr. Kojih dimenzija je ova slika?  
  2.3 Prikazati presek ove 3D slike u xy ravni, za z=100. Obratiti pažnju da je redosled dimenzija (z,x,y). Koji modalitet snimanja je u pitanju?

## 3. GUI za prikaz 3D slike u 3 projekcije  
GUI za jedanu dimenziju (prikaz_z.py):  
  3.1 Prikazati presek 3D MRI slike u xy ravni na jednom subplot-u.  
  3.2 Definisati slajder kojim će se kontrolisati vrednosti preseka po z-osi.  
  3.3 Definisati callback funkciju koja definiše akciju koja se dešava na promenu vrednostislajdera. Pozvati tu funkciju. 
  
GUI za 3 dimenzije:  
  3.4 U modulu slika_3d.py napraviti funkciju imshow_slice koja prikazuje 3D sliku u sva tri preseka. U okviru nje definisati slajdere za promenu vrednosti preseka po svim dimenzijama.  
  3.5 U glavnom modulu definisati callback funkcije za sva tri preseka.  
  3.6 Iskoristiti matplotlib podmodul gridspec za organizaciju subplot-ova.

## 4. Koordinate na kojima se nalazi sadržaj slike  
  4.1 Napraviti funkciju koordinate u modulu slika_3d.py koja pronalazi početnu i krajnju koordinatu na kojima se nalazi sadržaj slike. Očitati vrednosti koordinata na kojimapočinje i na kojima se završava sadržaj slike, za sve tri dimenzije. Da li se očitane vrednosti slažu sa vrednostima koje su dobijene iz funkcije?
