import cv2
import numpy as np
import matplotlib.pyplot as plt
import osum
from scipy.ndimage import convolve1d
from scipy.signal import find_peaks

# 1
# 1.1
im = cv2.imread('mr_01.png', cv2.IMREAD_GRAYSCALE)
osum.disp_im(im, title='Ulazna slika')
# plt.show()

# 1.2
h, g = np.histogram(im, np.arange(0, 256))
plt.figure()
plt.plot(g[:-1], h)
plt.show()

# 1.3
t1 = 75
t2 = 115
im_s1 = np.logical_and((im>t1), (im<t2))
osum.disp_im(im_s1, lmin=0, lmax=1, title='Rucno nadjeni pragovi za segmentaciju')
plt.show()

# 1.4
f, x_osa = osum.gaussian(21, 4)
# plt.figure()
# plt.plot(x_osa, f)
# plt.show()
h_f = convolve1d(h, f, mode='nearest')

# 1.5
peaks, props = find_peaks(h_f, distance=30, prominence=50)
plt.figure()
plt.plot(g[:-1], h_f)
plt.plot(peaks, h_f[peaks], marker='*', linestyle='None')
plt.title('Lokalni maksimumi na ublazenom histogramu')
plt.show()

# 1.6
vals = g[peaks]
tr = (g[peaks[0]]+g[peaks[1]])/2

im_s2 = im>tr
osum.disp_im(im_s2, lmin=0, lmax=1, title='Automatski pronadjen prag za segmentacijju')
plt.show()

# 2
# 2.1
lab = cv2.imread('lab_01.png', cv2.IMREAD_GRAYSCALE)
osum.disp_im(lab, lmin=lab.min(), lmax=lab.max(), title='Rucno labelirana slika')
plt.show()

labs = np.unique(lab)

# 2.2
lD = lab == 41  # bela masa desne hemisfere
lL = lab == 2  # bela masa leve hemisfere
lS = np.logical_or(lL, lD)
osum.disp_im(lD, title='lD', lmin=0, lmax=1)
osum.disp_im(lL, title='lL', lmin=0, lmax=1)
osum.disp_im(lS, title='lS', lmin=0, lmax=1)
plt.show()

# 2.4
t1 = osum.tanimoto(lS, im_s1)
t2 = osum.tanimoto(lS, im_s2)

# 2.5
abs1 = np.abs(np.uint8(lS)-np.uint8(im_s1))
osum.disp_im(abs1, lmin=0, lmax=1, title='Apsolutne razlike im_s1 i lS')
abs2 = np.abs(np.uint8(lS)-np.uint8(im_s2))
osum.disp_im(abs2, lmin=0, lmax=1, title='Apsolutne razlike im_s2 i lS')
plt.show()

# 2.6
t = []
pr = []
for p in range(im.min()+10, im.max()-9, 10):
    imS = im>p
    t.append(osum.tanimoto(imS, lS))
    pr.append(p)

ind = np.argmax(t)
maxT = t[ind]
optP = pr[ind]

im_s3 = im>optP
osum.disp_im(im_s3, lmin=0, lmax=1, title='Optimalni prag: '+str(optP))
plt.show()

