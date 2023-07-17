[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nebojsa-bozanic/BMI_OSuM/blob/master/Vezba6%3A%20Obrada%20rendgenske%20slike%3A%20Multiveli%C4%8Dinsko%20poja%C4%8Davanje%20strukture%20u%20slikama/OSuM_vezba_6.ipynb)

# Laboratorijska vežba 6: Obrada rendgenske slike: Multiveličinsko pojačavanje strukture u slikama

Potrebne biblioteke: cv2, numpy, matplotlib.pyplot, osum

## 1. Logaritamska kompresija opsega  
  1.1 Učitati sirovu sliku Ro_01.fxd koristeći funkciju read_raw iz modula osum.py.  
  1.2 Napraviti LUT za logaritamsku kompresiju opsega tako da se ulazni opseg od 16384 pretvori u opseg 4096 sa tolerancijom 0.001. Primeniti LUT na ulaznu sliku i smestiti je u promenljivu im_log.  
  1.3 Prikazati sliku nakon logaritamske kompresije.

## 2. Multiveličinsko pojačavanje struktura  
  2.1 U modulu osum.py napraviti funkciju sigmLUT koja pravi sigmoidalnu transformaciju za pojačanje detalja Laplasove piramide. Ulazni parametri funkcije su ulazi opseg, izlazni opseg i nagib sigmoidalne funkcije.  
  2.2 Dekomponovati sliku im_log na Laplasovu piramidu od 6 nivoa.  
  2.3 Napraviti LUT koji se koristi za sigmoidalno pojačanje Laplasovih koeficijenata tako da je ulazni opseg -2000 do 2000, izlazni opseg -800 do 800, a faktor nagiba krive 4. Prikazati dobijeni LUT.  
  2.4 Primeniti LUT iz prethodnog koraka na treći nivo Laplasove piramide (LP) i smestiti ga u promenljivu Lk. Prikazati treći nivo LP pre i nakon transformacije.  
  2.5 Napraviti histogram trećeg nivoa LP u rasponu -500 do 501, pre i nakon sigmoidalne transformacije. Prikazati histograme na istom grafiku. Kako se razlikuju histogrami?  
  2.6 Modifikovati rezidual u Res2 množenjem faktorom 0.7. Voditi računa da prosečni osvetljaj ostane isti.  
  2.7 Rekonstruisati sliku koristeći LP na čijem se trećem nivou nalazi Lk i Res2. Prikazati rekonstruisanu sliku. Kako se razlikuju ova slika i im_log?  
  2.8 Isprobati prethodne korake na različitim nivoima LP (ili na više nivoa odjednom) i sa različitim faktorima k u sigmoidalnoj tranformaciji. Koji je efekat većeg, a koji manjeg k. Kako izgleda slika sa modifikovanim prvim, a kako sa petim nivoom LP?

## 3. Korekcija MTF-a

Modulation Transfer Function, prenosna funkcija digitalnog panela kojim je snimana slika, prikazan je na slici ispod. Veličina piksela je 139 μm, ekvivalentno maksimalnoj rezoluciji 3.6 lp/mm (para linija po milimetru). MFT panela je određen „Std CsI“ krivama.

  3.1 Pretpostavljajući da je filter kojim radimo dekompoziciju piramide polu-opsežni, sračunati optimalne faktore pojačanja na svakom nivou piramide kako bi što bolje ispravili efekat MTF-a digitalnog panela u slici. Posmatrajte „Std CsI“ krive. Koje imaju vrednosti? Računati da je prosečan odziv u svakom opsegu vrednost MTF-a u sredini opsega. Kompenzujte njega pojačanjem da bude 1.  
  3.2 Dekomponovati sliku im_log do 6. nivo veličine u Laplasovu piramidu i pojačati svaki nivo detalja adekvatnim faktorom pojačanja za korekciju MTF (da odziv u celom opsegu bude 1).  
  3.3 Rekonstruisati sliku sa pojačanim slikama detalja. Uporediti dobijenu sliku sa slikom im_log.  
  3.4 Ponoviti korake 3.2 i 3.3 koristeći dodatno pojačanje na 4. i 5. nivou LP. Koji je efekat na rekonstruisanoj slici?
