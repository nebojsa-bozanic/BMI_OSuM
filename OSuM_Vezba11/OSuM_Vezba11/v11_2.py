import cv2
import osum
import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import structural_similarity as ssi

# 3
# 3.1
im1 = cv2.imread('mr_glava_1.jpg', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('mr_glava_10.jpg', cv2.IMREAD_GRAYSCALE)
im3 = cv2.imread('mr_glava_5.jpg', cv2.IMREAD_GRAYSCALE)
osum.disp_im(im1, title='im1')
osum.disp_im(im2, title='im2')
osum.disp_im(im3, title='im3')
plt.show()

# 3.2
ssd1 = np.sum(np.sum((im1-im2)**2))
ssdp1 = ssd1/im1.size
ssd2 = np.sum(np.sum((im1-im3)**2))
ssdp2 = ssd2/im1.size

# 3.3
sabs1 = np.sum(np.sum(np.abs(im1-im2)))
sabsp1 = sabs1/im1.size
sabs2 = np.sum(np.sum(np.abs(im1-im3)))
sabsp2 = sabs2/im1.size

# 2D histogram
h2d, xedges, yedges = np.histogram2d(np.reshape(im1, -1), np.reshape(im2, -1), bins=10)
plt.figure()
plt.imshow(h2d, cmap='gray', vmin=h2d.min(), vmax=h2d.max())
plt.title('2D histogram im1 i im2')
plt.xlabel('im1')
plt.ylabel('im2')
plt.show()

# 3.5
im4 = cv2.imread('2_CT.png', cv2.IMREAD_GRAYSCALE)
im5 = cv2.imread('2_PET.png', cv2.IMREAD_GRAYSCALE)
osum.disp_im(im4, title='im4')
osum.disp_im(im5, title='im5')
plt.show()

mi1, hx1, hy1 = osum.mutual_information(im4, im5, 20)
mi2, hx2, hy2 = osum.mutual_information(im4, 255-im5, 20)

sabs11 = np.sum(np.abs(im4-im5))
sabsp11 = sabs11/im4.size
sabs22 = np.sum(np.abs(im4-(255-im5)))
sabsp22 = sabs22/im4.size

# 3.7
nmi1 = osum.normalized_mutual_information(im4, im5, 20)
nmi2 = osum.normalized_mutual_information(im4, (255-im5), 20)

# 3.8
ssi1, lok_sl1 = ssi(im1, im2, full=True)  # full=True - da se kao izlaz racuna i slika lokalne slicnosti
ssi2, lok_sl2 = ssi(im1, im3, full=True)
osum.disp_im(lok_sl1, lmin=lok_sl1.min(), lmax=lok_sl1.max(), title='Lokalna slicnost po ssi izmedju im1 i im2')
osum.disp_im(lok_sl2, lmin=lok_sl2.min(), lmax=lok_sl2.max(), title='Lokalna slicnost po ssi izmedju im1 i im3')
plt.show()

# 3.9
qab, qab_im, w = osum.imq_qab(im1, im2)
osum.disp_im(qab_im, lmin=qab_im.min(), lmax=qab_im.max(), title='Lokalna slicnost po Qab')
osum.disp_im(w, lmin=w.min(), lmax=w.max(), title='Mapa znacaja lokacija')
plt.show()

print()