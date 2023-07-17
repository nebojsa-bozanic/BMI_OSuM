[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba5%3A%20Obrada%20rendgenske%20slike%3A%20Logaritamska%20kompresija%20opsega/OSuM_vezba_5.ipynb)

# Laboratorijska vežba 5: Obrada rendgenske slike: Logaritamska kompresija opsega

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot

## 1. Sirova slika  
  1.1 Učitati sirovu sliku Ro_01.fxd koristeći funkciju read_raw iz modula osum.py.  
  1.2 U kom opsegu se nalaze vrednosti slike? Koji je tip slike? Koje su dimenzije slike?  
  1.3 Prikazati sliku. Koji modalitet je u pitanju i šta se vidi na slici?  
  1.4 Napraviti histogram slike u granicama od 0 do 16384 sa korakom 8.  
  1.5 Prikazati histogram. Kako izgleda raspodela i kako se to odražava na izgled snimka?

## 2. Logaritamska kompresija opsega  
  2.1 U modulu osum.py napraviti funkciju log_LUT u kojoj se pravi look-up tabela sa logaritamskom kompresijom opsega. Ulazni parametri funkcije su ulazni opseg, izlazni opseg i tolerancija do koje se komprimuje linearno.  
  2.2 Napraviti LUT za logaritamsku kompresiju opsega tako da se ulazni opseg od 16384 pretvori u opseg 4096 sa tolerancijom 0.001. Primeniti LUT na ulaznu sliku.  
  2.3 Prikazati sliku nakon logaritamske kompresije opsega. Koji je efekat ove transformacije?  
  2.4 Napraviti histogram slike nakon primenjene transformacije i na istom grafiku prikazati histogram pre i nakon transformacije. Kako se razlikuju raspodele?  
  2.5 Ponoviti korak 2.2 koristeći toleranciju od 0.1. Prikazati sliku. Zašto se vidi manje struktura?
