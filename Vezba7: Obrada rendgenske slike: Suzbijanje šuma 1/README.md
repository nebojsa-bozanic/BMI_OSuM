[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba7%3A%20Obrada%20rendgenske%20slike%3A%20Suzbijanje%20%C5%A1uma%201/OSuM_vezba_7.ipynb)

# Laboratorijska vežba 7: Obrada rendgenske slike: Suzbijanje šuma 1

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, scipy.ndimage.filters (convolve1d, convolve), medpy.filter.smoothing (anisotropic_diffusion), osum

## 1. Razdvojivi 2D NF filtar  
  1.1 Učitati sliku lspine_crop.png u promenljivu im1.  
  1.2 Koristeći funkciju gaussian iz modula osum.py napraviti 1D Gausov filtar sa proizvoljnim n i sigma (npr. n=19, sigma =3).  
  1.3 Prikazati 1D filtar, a zatim prikazati 2D filtar H koji se dobija vektorskim množenjem dva 1D filtra.  
  1.4 Isfiltrirati sliku im1 1D gausovim filtrom prvo po jednoj dimenziji, a zatim po drugoj. Gausov filtar je razdvojiv filtar, pa je ovo ekvivalentno direktnom filtriranju sa 2D filtrom. Koja je prednost filtriranja 1D filtrima u odnosu na 2D filtar?  
  1.5 Prikazati sliku nakon filtriranja i uporediti je sa originalnom. Koji je efekat filtriranja na šum, a koji na ivice.  
  1.6 Ponoviti prethodne korake za različite kombinacije n i sigma. Koji je efekat kada se koriste veće, a koji kada se koriste manje vrednosti n, odnosno sigma?  
  1.7 Ponoviti prethodne korake sa slikom lspine.png učitanom u promenljivu im11.

## 2. Usmereno filtriranje  
  2.1 Od filtra H napraviti usmereni filtar H1 koji prati ivice. Prikazati ga.  
  2.2 Primeniti filtar na sliku im1 i prikazati je. Uporediti je sa slikom slikom isfiltriranomprethodnim filtrom. Isto uraditi i sa slikom im11. Zašto slika izgleda tamnije?  

## 3. Anizotropski filtar  
U promenljivu im2 učitati sliku abdomen_crop.png i isfiltrirati je funkcijom anisotropic_diffusion. Inicijalno postaviti parametre niter=5 i kappa=100. Menjati parametre i analizirati efekte. Prikazati isfiltriranu sliku.

## 4. Bilateralni filtar  

Primeniti bilateralni filtar na sliku im2. Inicijalno postaviti parametre velicina prozora d=15, std prostornog kernela sigmaSpace=15, std kernela za intenzitet sigmaColor=15. Isprobati različite kombinacije parametara i analizirati efekte. Uraditi isto sa slikom
abdomen.png učitanom u promenljivu im22.

## 5. Multiveličinsko filtriranje  

### Skraćivanje u piramidi  
  5.1 Napraviti Laplasovu piramidu sa 2 nivoa od slike im2. Prikazati histogram prvog nivoa LP u granicama -200 do 200.  
  5.2 Skraćivanje piramide se radi na višim nivoima piramida slike uz pretpostavku da na tim nivoima dominira šum, pa želimo da smanjimo kontrast, tj. vidljivost šuma. Vrednosti svih koeficijenata smanjujemo (skraćujemo) za vrednost cs (inicijalno postaviti na 15). Koeficijente koji su po apsolutnoj vrednosti manji od cs treba svesti na 0.
  5.3 Napraviti histogram prvog nivoa LP nakon skraćivanja i prikazati ga preko histograma originalnog nivoa.  
  5.4 Prikazati sliku pre i posle skraćivanja i uporediti ih.  
  5.5 Menjati vrednosti cs (odabrati vrednosti analizom histograma) i analizirati efekte. Isprobati skraćivanje i na drugi nivou LP.  
  5.6 Ponoviti sve korake za sliku im22.

### Pragovanje u piramidi  
  5.7 Pragovanje se iz istog razloga kao i skraćivanje radi na višim nivoima piramide. Koeficijente koji su po apsolutnoj vrednosti manji od praga t treba svesti na 0. Inicijalno uzeti t=15.  
  5.8 Prikazati histograme pre i posle pragovanja.  
  5.9 Prikazati slike pre i posle pragovanja.  
  5.10 Isporbati različite vrednosti za prag t (odabrati vrednosti analizom histograma)
kao i za drugi nivo LP i analizirati efekte. Ponoviti sve korake za sliku im22.
