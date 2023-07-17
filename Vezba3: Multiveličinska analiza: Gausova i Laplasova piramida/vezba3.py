import osum
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import convolve1d


# 1.2
n = 7
sigma = 1.5
f, x_osa = osum.gaussian(n, sigma)
print(f)

# 1.3
plt.figure()
plt.stem(x_osa, f)
# plt.show()

# 1.5
H = np.outer(f, f)
print(H)

# 1.6
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# # [x, y] = np.meshgrid(np.arange(0, n), np.arange(0, n))
# [x, y] = np.meshgrid(x_osa, x_osa)
# ax.plot_surface(x, y, H, cmap='viridis')
# plt.show()

# plt.show()
# 2.1
im = cv2.imread('mr_glava_1.jpg', cv2.IMREAD_GRAYSCALE)
im = im.astype(np.float32)

# Redukcija
# 2.2
# nearest - prosirenje slike zbog filtriranja ponavljanjem ivicnih piksela
a_f = convolve1d(im, f, axis=1, mode='nearest')
# 2.3
a_f2 = a_f[:,::2]
# 2.4
b_f = convolve1d(a_f2, f, axis=0, mode='nearest')
# 2.5
# prvi nivo Gausove piramide
b_f2 = b_f[::2]

# 2.7
# cv2.imshow('Originalna slika', osum.im_norm(im))
# cv2.imshow('Filtriranje niz vrste', osum.im_norm(a_f))
# cv2.imshow('Decimacija niz vrste', osum.im_norm(a_f2))
# cv2.imshow('Filtriranje niz kolone', osum.im_norm(b_f))
# cv2.imshow('Decimacija niz kolone', osum.im_norm(b_f2))
# cv2.imshow('Prvi nivo Gausove piramide', osum.im_norm(b_f2))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Ekspanzija
# 3.1
c = np.insert(b_f2, range(1, b_f2.shape[0]+1), 0, axis=0)
# 3.2
c_f = convolve1d(c, 2*f, axis=0, mode='nearest')
# 3.3
d = np.insert(c_f, range(1, c_f.shape[1]+1), 0, axis=1)
# 3.4
d_f = convolve1d(d, 2*f, axis=1, mode='nearest')

# 3.5
# cv2.imshow('Originalna slika', osum.im_norm(im))
# cv2.imshow('Dodate nule iza svake vrste', osum.im_norm(c))
# cv2.imshow('Filtriranje niz kolone', osum.im_norm(c_f))
# cv2.imshow('Dodate nule iza svake kolone', osum.im_norm(d))
# cv2.imshow('Filtriranje niz vrste', osum.im_norm(d_f))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 3.6
# Prvi nivo Laplasove piramide
l = im-d_f

# 3.7
l = l.astype(np.int16)
# plt.figure()
# plt.imshow(l, cmap='gray', vmin=l.min(), vmax=l.max())
# plt.axis('off')
# plt.title('Slika detalja na prvom nivou rezolucije')
# plt.show()

# # 3.8
# plt.figure()
# plt.imshow(abs(l), cmap='gray', vmin=abs(l).min(), vmax=abs(l).max())
# plt.axis('off')
# plt.title('Apsolutna vrednost koeficijenata na prvom nivou Laplasove piramide')
# plt.show()

# 4.1
# Redukcija
g = cv2.pyrDown(im, borderType=cv2.BORDER_REPLICATE)
# Ekspanzija
g_ex = cv2.pyrUp(g, cv2.BORDER_REPLICATE)

l = im - g_ex

plt.figure()
plt.imshow(g, cmap='gray', vmin=g.min(), vmax=g.max())
plt.axis('off')
plt.title('Prvi nivo Gausove piramide')
plt.show()

plt.figure()
plt.imshow(l, cmap='gray', vmin=l.min(), vmax=l.max())
plt.axis('off')
plt.title('Prvi nivo Laplasove piramide')
plt.show()

# 4.3
N_razl = 3
LPyr, GPyr, Res = osum.im_pyr_decomp(im, N_razl)

for i in range(1, N_razl):
    plt.figure()
    g = GPyr[i]
    plt.imshow(g, cmap='gray', vmin=g.min(), vmax=g.max())
    plt.axis('off')
    plt.title(str(i+1)+'. nivo Gausove piramide')
    plt.show()

plt.figure()
plt.imshow(Res, cmap='gray', vmin=Res.min(), vmax=Res.max())
plt.axis('off')
plt.title('Rezidual')
plt.show()

for i in range(0, N_razl):
    plt.figure()
    l = 5*LPyr[i]+128
    plt.imshow(l, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.title(str(i+1)+'. nivo Laplasove piramide')
    plt.show()

# 4.5
im_rec = osum.im_pyr_recon(LPyr, Res)
print('Suma apsolutnih razlika iznosi '+str(sum(sum(abs(im-im_rec)))))

# 5.1
im = im.astype(np.int32)
plt.figure(10)
plt.imshow(im, cmap='gray', vmin=im.min(), vmax=im.max())
plt.axis('off')
plt.title('Originalna slika')

for i in range(N_razl):

    LPyr_tmp = LPyr
    LPyr_tmp[i] = LPyr[i]*2
    im_rec = osum.im_pyr_recon(LPyr_tmp, Res)
    im_rec = im_rec.astype(np.int32)

    plt.figure(i)
    plt.imshow(im_rec, cmap='gray', vmin=im.min(), vmax=im.max())
    plt.axis('off')
    plt.title('Rekonstrukcija nakon modifikacije nivoa '+str(i+1))
    print(sum(sum(abs(im-im_rec))))

plt.show()

# 5.2
im = im.astype(np.int32)
plt.figure(10)
plt.imshow(im, cmap='gray', vmin=im.min(), vmax=im.max())
plt.axis('off')
plt.title('Originalna slika')

for i in range(N_razl):
    LPyr_tmp = LPyr
    LPyr_tmp[i] = LPyr[i]*5
    im_rec = osum.im_pyr_recon(LPyr_tmp, Res)
    im_rec = im_rec.astype(np.int32)

    plt.figure(i)
    plt.imshow(im_rec, cmap='gray', vmin=im.min(), vmax=im.max())
    plt.axis('off')
    plt.title('Rekonstrukcija nakon modifikacije nivoa ' + str(i+1))
    print(sum(sum(abs(im - im_rec))))

plt.show()

# 5.3
im = im.astype(np.int32)
plt.figure(10)
plt.imshow(im, cmap='gray', vmin=im.min(), vmax=im.max())
plt.axis('off')
plt.title('Originalna slika')

for i in range(N_razl):
    ind = abs(LPyr[i]) < 10
    LPyr_tmp = LPyr
    LPyr_tmp[i][ind] = 0
    im_rec = osum.im_pyr_recon(LPyr_tmp, Res)
    im_rec = im_rec.astype(np.int32)

    plt.figure(i)
    plt.imshow(im_rec, cmap='gray', vmin=im.min(), vmax=im.max())
    plt.axis('off')
    plt.title('Rekonstrukcija nakon modifikacije nivoa ' + str(i + 1))
    print(sum(sum(abs(im - im_rec))))

plt.show()

# 5.4
im = im.astype(np.int32)
plt.figure(10)
plt.imshow(im, cmap='gray', vmin=im.min(), vmax=im.max())
plt.axis('off')
plt.title('Originalna slika')

for i in range(N_razl):
    ind = abs(LPyr[i]) < 30
    LPyr_tmp = LPyr
    LPyr_tmp[i][ind] = 0
    im_rec = osum.im_pyr_recon(LPyr_tmp, Res)
    im_rec = im_rec.astype(np.int32)

    plt.figure(i)
    plt.imshow(im_rec, cmap='gray', vmin=im.min(), vmax=im.max())
    plt.axis('off')
    plt.title('Rekonstrukcija nakon modifikacije nivoa ' + str(i + 1))
    print(sum(sum(abs(im - im_rec))))

plt.show()

