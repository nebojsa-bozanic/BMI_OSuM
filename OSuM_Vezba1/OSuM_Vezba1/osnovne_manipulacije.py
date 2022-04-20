import cv2
import matplotlib.pyplot as plt
import numpy as np


# 1
# 1.1
im1 = cv2.imread('mr_glava_1.jpg', cv2.IMREAD_GRAYSCALE) # ukoliko slika nije u ovom folderu ovde staviti putanju do nje
# IMREAD_GRAYSCALE - siva slika uint8 tipa


# 1.2
# cv2.imshow('Slika 1', im1)
# cv2.waitKey(0) # 0-beskonacni delay; neka druga vrednost - delay u ms
# cv2.destroyAllWindows()
#
# # 1.3imread
# plt.figure(1)
# plt.imshow(im1, cmap='gray')
# plt.title('Slika 1')
# plt.show()

# 1.4
im2 = im1[100:200, :]

# 1.5
cv2.imwrite('mr1_crop.jpg', im2)

# 2
# 2.1
im3 = cv2.imread('OSuM_Vezba1/rtg_2.png', cv2.IMREAD_ANYDEPTH) # rezim koji ucitava sivu sliku proizvoljnog tipa

# 2.3
# plt.figure()
# plt.imshow(im1, cmap='gray', vmin=im2.min(), vmax=im2.max()) # pun opseg: vmin=0, vmax=65535
# plt.title('Slika 2')
# plt.show()

# 3
# 3.1
im4 = cv2.imread('mr_glava_2.jpg', cv2.IMREAD_GRAYSCALE)

# 3.2
im_r1 = im1-im4

# 3.3
im_r2 = im1.astype(np.int16)-im4.astype(np.int16)

# 3.4
# plt.figure()
# plt.imshow(im_r2, cmap='gray', vmin=im_r2.min(), vmax=im_r2.max())
# plt.title('Slika razlka')
# plt.show()

# 3.5
im_r3 = abs(im1.astype(np.int16)-im4.astype(np.int16))
plt.figure()
plt.imshow(im_r3, cmap='gray', vmin=im_r3.min(), vmax=im_r3.max())
plt.title('Slika apsolutnih razlka')
plt.show()

# 3.6
im_n = (im_r3-im_r3.min())/(im_r3.max()-im_r3.min())
print(im_n.dtype)
# cv2.imshow('Normalizovana slika apsolutnih razlika', im_n)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 4
# 4.1
im1_2 = im1.astype(np.int16)+200

# 4.2
im1_3 = im1.astype(np.int16)-200

# 4.3
fig, axs = plt.subplots(1, 3)
axs[0].imshow(im1, cmap='gray')
axs[0].set_title('Originalna slika')
axs[1].imshow(im1_2, cmap='gray', vmin=0, vmax=im1_2.max())
axs[1].set_title('Slika + 200')
axs[2].imshow(im1_3, cmap='gray', vmin=im1_3.min(), vmax=255)
axs[2].set_title('Slika - 200')
plt.show()

# 4.4
im1_4 = im1*3.5
im1_5 = im1/1.5

# 5
# 5.1
im1_min = im1.min()
im1_max = im1.max()
print('Dinamicki opseg slike je', im1_max-im1_min, ', od', im1.min(), ' do', im1.max())

im1.min(0) # minimum po kolonama
im1.min(1) # minimum po vrstama

# 5.2
im1_srvr = im1.mean()
print('Srednja vrednost slike je', im1_srvr)

# 5.3
im1_var = im1.var()
im1_std = im1.std()
print('Varijansa slike je ', im1_var)
print('Standardna devijacija slike je', im1_std)

# 6
# 6.1
h = cv2.calcHist([im1], [0], None, [256], [0, 256])
print('Broj odmeraka u histogramu je', h.size)
plt.figure()
plt.plot(h)
plt.title('Histogram slike')
plt.show()

# 6.2
h_n = h/im1.size
plt.figure()
plt.plot(h_n)
plt.title('Normalizovani histogram slike')
plt.show()

# 6.3
udeo206 = h_n[206]
print(round(udeo206[0]*100, 2), '% slike ima vrednost 206')

# 6.4
udeo_do_200 = sum(h_n[:200])
print(round(udeo_do_200[0]*100, 2), '% slike ima vrednost ispod 200')
