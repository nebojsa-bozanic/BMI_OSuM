import pywt
import numpy as np
import matplotlib.pyplot as plt
import cv2


#2.1
im = cv2.imread('1_MR.jpg', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('knee.tif', cv2.IMREAD_GRAYSCALE) #2.5

plt.figure()
plt.imshow(im, cmap='gray')
plt.axis('off')
plt.title('Originalna slika')

w = 'db1'
n = 4
C = pywt.wavedec2(im, wavelet=w, mode='periodization', level=n)
coeff_array, coeff_slices = pywt.coeffs_to_array(C)

#2.2
Csort = np.sort(abs(coeff_array.reshape(-1)))  #sortiranje u rastucem poretku

for x in [0.1, 0.05, 0.01, 0.005]:  # x - koliko se koeficijenata zadrzava

    # t - vrednost na poziciji poslednjek koeficijenta koji se odbacuje
    t = Csort[int(np.floor((1-x)*len(Csort)))]
    # maska sa 0 i 1; 1 - koeficijent je veci od definisanog praga
    m = abs(coeff_array)>t
    coeff_filt = coeff_array*m

    #2.3
    Cfilt = pywt.array_to_coeffs(coeff_filt, coeff_slices, output_format='wavedec2')
    im_r = pywt.waverec2(Cfilt, wavelet=w, mode='periodization')

    plt.figure()
    plt.imshow(np.uint8(im_r), cmap='gray')
    plt.axis('off')
    plt.title('Rekonstrukcija sa '+str(x*100)+'% koeficijenata')

plt.show()



