import pywt
import matplotlib.pyplot as plt
import cv2

#1.1
im = cv2.imread('mr_glava_1.jpg', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('knee.tif', cv2.IMREAD_GRAYSCALE)  #1.7

#1.2
w = 'db1'
coeffs = pywt.dwt2(im, w, mode='periodization')
cA, (cH, cV, cD) = coeffs

#1.3
plt.figure()
plt.subplot(2,2,1)
plt.imshow(cA, cmap='gray')
plt.title('NF aproksimacija')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(cH, cmap='gray')
plt.title('Horizontalni detalji')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(cV, cmap='gray')
plt.title('Vertikalni detalji')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(cD, cmap='gray')
plt.title('Dijagonalni detalji')
plt.axis('off')
plt.show()

#1.4
im_r = pywt.idwt2(coeffs,w,mode='periodization')

plt.figure()
plt.imshow(im, cmap='gray')
plt.title('Originalna slika')
plt.axis('off')

plt.figure()
plt.imshow(im_r, cmap='gray')
plt.title('Rekonstruisana slika')
plt.axis('off')
plt.show()

r = sum(sum(abs(im-im_r)))
print('Suma apsolutnih razlika između originalne i rekonstruisane slike:', round(r))

#1.5
w = 'db1'
n = 3
C = pywt.wavedec2(im, wavelet=w, mode='periodization', level=n)

C[0] = C[0]/abs(C[0]).max()
C[1] = [d/abs(d).max() for d in C[1]]
C[2] = [d/abs(d).max() for d in C[2]]
C[3] = [d/abs(d).max() for d in C[3]]

cA3 = C[0]
(cH3, cV3, cD3) = C[1]
(cH2, cV2, cD2) = C[2]
(cH1, cV1, cD1) = C[3]

C[1][0] = cV3
C[1][1] = cH3
C[2][0] = cV2
C[2][1] = cH2
C[3][0] = cV1
C[3][1] = cH1

coeff_array, coeff_slices = pywt.coeffs_to_array(C)

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(abs(coeff_array), cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.title('Vejlet piramida sa 3 nivoa')
plt.show()

