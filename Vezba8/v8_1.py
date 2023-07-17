import cv2
import numpy as np
import matplotlib.pyplot as plt
import osum
import pywt


# 1.2
sigLUT = osum.sigmLUT(2000, 800, 7)
plt.figure()
plt.plot(np.arange(-2000, 2001), sigLUT)
plt.grid()
plt.title('LUT za sigmoidalno pojacanje')

# 1.3
sigLUT_lin = osum.sigmLUT_lin(2000, 800, 7, 0.03)
plt.figure()
plt.plot(np.arange(-2000, 2001), sigLUT_lin)
plt.grid()
plt.title('LUT za ublazeno pojacanje')
plt.show()

# 1.4
[im, DetInfo, hdr] = osum.read_raw('Ro_01.fxd')
logLUT = osum.log_LUT(16384, 4096, 0.001)
im_log = logLUT[im]

# 1.5
Lpyr, Gpyr, Res, size_vec = osum.im_pyr_decomp(im_log, 2)
L1 = Lpyr[0]

Lk1 = sigLUT[np.uint16(L1+2000)]
Lpyr1 = Lpyr
Lpyr1[0] = Lk1

Lk2 = sigLUT_lin[np.uint16(L1+2000)]
Lpyr2 = Lpyr
Lpyr2[0] = Lk2

# 1.6
im_rec1 = osum.im_pyr_recon(Lpyr1, Res, size_vec)
im_rec2 = osum.im_pyr_recon(Lpyr2, Res, size_vec)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_rec1, cmap='gray', vmin=im_rec1.min(), vmax=im_rec1.max())
plt.axis('off')
fig.canvas.set_window_title('Sigmoidalno pojacanje')

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_rec2, cmap='gray', vmin=im_rec2.min(), vmax=im_rec2.max())
plt.axis('off')
fig.canvas.set_window_title('Ublazeno sigmoidalno pojacanje')
plt.show()


# 1.9
sigLUT_z = osum.sigmLUT_z(2000, 800, 7, 0.03)
plt.figure()
plt.plot(np.arange(-2000, 2001), sigLUT_z)
plt.grid()
plt.title('LUT za direktno potiskivanje suma')
plt.show()

# 1.10
Lpyr, Gpyr, Res, size_vec = osum.im_pyr_decomp(im_log, 2)
L1 = Lpyr[0]

Lk3 = sigLUT_z[np.uint16(L1+2000)]
Lpyr3 = Lpyr
Lpyr3[0] = Lk3
im_rec3 = osum.im_pyr_recon(Lpyr3, Res, size_vec)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_rec3, cmap='gray', vmin=im_rec3.min(), vmax=im_rec3.max())
plt.axis('off')
fig.canvas.set_window_title('Direktno potiskivanje suma')
plt.show()


# 2.1

im2 = cv2.imread('abdomen.png', cv2.IMREAD_GRAYSCALE)

w = 'db4'
n = 2
C = pywt.wavedec2(im2, wavelet=w, mode='periodization', level=n)

cA2 = C[0]
(cH2, cV2, cD2) = C[1]
(cH1, cV1, cD1) = C[2]
C = [list(c) for c in C]  # pretvaramo iz tuple u listu da bismo mogli da menjamo

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(abs(cD1), cmap='gray', vmin=abs(cD1).min(), vmax=abs(cD1).max())
plt.axis('off')
fig.canvas.set_window_title('cD1')
plt.show()

# 2.2
sigma = np.median(np.abs(cD1))/0.6745

# 2.4
sigLUT = osum.sigmLUT(1000, 800, 7)
sigLUT_z = osum.sigmLUT_z(1000, 800, 7, 3*sigma)

# 2.5
cD1_k = sigLUT[np.uint16(cD1+1000)]
cD1_k2 = sigLUT_z[np.uint16(cD1+1000)]

C[2][2] = cD1_k
im_rec1 = pywt.waverec2(C, wavelet=w, mode='periodization')

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_rec1, cmap='gray', vmin=im_rec1.min(), vmax=im_rec1.max())
plt.axis('off')
fig.canvas.set_window_title('Sigmoidalna transformacija')

C[2][2] = cD1_k2
im_rec2 = pywt.waverec2(C, wavelet=w, mode='periodization')

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_rec2, cmap='gray', vmin=im_rec2.min(), vmax=im_rec2.max())
plt.axis('off')
fig.canvas.set_window_title('Direktno potiskivanje suma')
plt.show()
