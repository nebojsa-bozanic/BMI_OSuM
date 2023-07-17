import cv2
import numpy as np
import matplotlib.pyplot as plt
import osum
from scipy.ndimage.filters import convolve1d, convolve
from medpy.filter.smoothing import anisotropic_diffusion

# 1.1
im1 = cv2.imread('lspine_crop.png', cv2.IMREAD_GRAYSCALE)
# 1.7
im11 = cv2.imread('lspine.png', cv2.IMREAD_GRAYSCALE)

# 1.2
n = 19
sigma = 3
# 1.6
# n = 11
# sigma = 1.5

f, x_osa = osum.gaussian(n, sigma)

# 1.3
plt.figure()
plt.stem(x_osa, f)
# plt.show()

H = np.outer(f,f)
fig = plt.figure()
ax = plt.axes(projection='3d')
[x,y] = np.meshgrid(x_osa, x_osa)
ax.plot_surface(x, y, H, cmap='viridis')
plt.show()

# 1.4
im_f1 = convolve1d(im1, f, axis=0, mode='nearest')
im_f1 = convolve1d(im_f1, f, axis=1, mode='nearest')

# 1.5
cv2.imshow('Originalna slika', im1)
cv2.imshow('NF filtrirana', im_f1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Usmereno filtriranje
# 2.1
H2 = H
ind = int(np.ceil(n/2))
H2[ind:, :] = H2[ind:, :]*0.1

fig = plt.figure()
ax = plt.axes(projection='3d')
[x,y] = np.meshgrid(x_osa, x_osa)
ax.plot_surface(x, y, H2, cmap='viridis')
plt.show()

# 2.2
im_f2 = convolve(im1, H, mode='nearest')
cv2.imshow('Usmereno filtriranje', im_f2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Anizotropska difuzija

im2 = cv2.imread('abdomen_crop.png', cv2.IMREAD_GRAYSCALE)
im_f3 = anisotropic_diffusion(im2, niter=5, kappa=100)
# manje kappa->manji gradijent sprecava provodjenje->difuzija kroz manji prostor, manje se usrednjava

plt.figure()
plt.imshow(im_f3, cmap='gray', vmin=im_f3.min(), vmax=im_f3.max())
plt.axis('off')
plt.title('AD filtriranje')
plt.show()

# 4. Bilateralni filtar

im22 = cv2.imread('abdomen.png', cv2.IMREAD_GRAYSCALE)
im_f4 = cv2.bilateralFilter(im2, d=15, sigmaSpace=15, sigmaColor=15)
# im_f4 = cv2.bilateralFilter(im2, d=15, sigmaSpace=15, sigmaColor=75)

cv2.imshow('Bilateralno filtriranje', im_f4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Skracivanje u piramidi
# 5.1
Lpyr, Gpyr, Res, size_vec = osum.im_pyr_decomp(im2, 2)
L1 = Lpyr[0]
# L2 = Lpyr[1]  # 5.5

g = np.arange(-200, 201)
h1 = np.histogram(L1, g)
plt.figure()
plt.plot(g[:-1], h1[0])
# plt.show()

# 5.2
cs = 15  # cs = 20, cs = 10, cs = 5  # 5.5
L1[L1>0] = np.maximum(L1[L1>0]-cs, 0)
L1[L1<0] = np.minimum(L1[L1<0]+cs, 0)

# 5.3
h2 = np.histogram(L1, g)
plt.plot(g[:-1], h2[0])
plt.legend(['original', 'skracivanje'])
plt.title('L1')
plt.show()

# 5.4
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im2, cmap='gray', vmin=im2.min(), vmax=im2.max())
plt.axis('off')
fig.canvas.set_window_title('Originalna slika')

Lpyr[0] = L1
im_r1 = osum.im_pyr_recon(Lpyr, Res, size_vec)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_r1, cmap='gray', vmin=im_r1.min(), vmax=im_r1.max())
plt.axis('off')
fig.canvas.set_window_title('Nakon skracivanja u piramidi')
plt.show()

# Pragovanje u piramidi
# 5.7
Lpyr, Gpyr, Res, size_vec = osum.im_pyr_decomp(im2, 2)
L1 = Lpyr[0]

g = np.arange(-200, 201)
h1 = np.histogram(L1, g)

t = 15
L1[abs(L1)<t] = L1[abs(L1)<t]*0

# 5.8
h2 = np.histogram(L1, g)
plt.figure()
plt.plot(g[:-1], h1[0])
plt.plot(g[:-1], h2[0])
plt.legend(['original', 'pragovanje'])
plt.title('L1')
plt.show()

# 5.9
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im2, cmap='gray', vmin=im2.min(), vmax=im2.max())
plt.axis('off')
fig.canvas.set_window_title('Originalna slika')

Lpyr[0] = L1
im_r2 = osum.im_pyr_recon(Lpyr, Res, size_vec)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_r2, cmap='gray', vmin=im_r2.min(), vmax=im_r2.max())
plt.axis('off')
fig.canvas.set_window_title('Nakon pragovanja u piramidi')
plt.show()
