import cv2
import osum
import matplotlib.pyplot as plt
import numpy as np

# 1
# 1.1
im1 = cv2.imread('REG_HE.png', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread('REG_LE_08.PNG', cv2.IMREAD_GRAYSCALE)

im1_nim1 = np.float32(im1)
im2 = np.float32(im2)
osum.disp_im(im1, title='im1')
osum.disp_im(im2, title='im2')
osum.disp_im(np.abs(im1-im2), title='abs razlika')
# plt.show()
d = np.sum(np.sum(np.abs(im1-im2)))
d_mu = np.abs(np.mean(im1)-np.mean(im2))


# 1.2
g = np.arange(0, 256)
h1 = np.histogram(im1, g)
h2 = np.histogram(im2, g)

plt.figure()
plt.plot(g[:-1], h1[0])
plt.plot(g[:-1], h2[0])
plt.legend(['im1', 'im2'])
plt.title('Histogrami pre z-normalizacije')
# plt.show()

# 1.3
im1_n = (im1-np.mean(im1))/np.sqrt(np.var(im1))
im2_n = (im2-np.mean(im2))/np.sqrt(np.var(im2))

# 1.4
osum.disp_im(im1_n, title='im1 nakon z-normalizacije', lmin=im1_n.min(), lmax=im1_n.max())
osum.disp_im(im2_n, title='im2 nakon z-normalizacije', lmin=im2_n.min(), lmax=im2_n.max())
abs_n = np.abs(im1_n-im2_n)
osum.disp_im(abs_n, title='abs razlika nakon z-normalizacije', lmin=abs_n.min(), lmax=abs_n.max())
# plt.show()

print(np.mean(im1_n))
print(np.mean(im2_n))
print(np.std(im1_n))
print(np.std(im2_n))
d_n = np.sum(np.sum(np.abs(im1_n-im2_n)))
d_mu_n = np.abs(np.mean(im1_n)-np.mean(im2_n))

# 1.5
g = np.linspace(-2, 2, num=200)
h1 = np.histogram(im1_n, g)
h2 = np.histogram(im2_n, g)

plt.figure()
plt.plot(g[:-1], h1[0])
plt.plot(g[:-1], h2[0])
plt.legend(['im1_n', 'im2_n'])
plt.title('Histogrami nakon z-normalizacije')
plt.show()


# 2
# 2.2
im1_n_lok1 = osum.z_norm(im1)
im2_n_lok1 = osum.z_norm(im2)

# imz1 = osum.z_norm(im1, d=55, s=10)
# imz2 = osum.z_norm(im1, d=11, s=2)
# imz3 = osum.z_norm(im1, d=21, s=5)
# osum.disp_im(imz1, title='d=55, s=10', lmin=imz1.min(), lmax=imz1.max())
# osum.disp_im(imz2, title='d=11, s=2', lmin=imz2.min(), lmax=imz2.max())
# osum.disp_im(imz3, title='d=21, s=5', lmin=imz3.min(), lmax=imz3.max())
# plt.show()

osum.disp_im(im1_n_lok1, title='im1 lokalna z-normalizacija 1', lmin=im1_n_lok1.min(), lmax=im1_n_lok1.max())
osum.disp_im(im2_n_lok1, title='im2 lokalna z-normalizacija 1',lmin=im2_n_lok1.min(), lmax=im2_n_lok1.max())
abs_n_lok1 = np.abs(im1_n_lok1-im2_n_lok1)
osum.disp_im(abs_n_lok1, title='abs razlika nakon lokalne z-normalizacije 1', lmin=abs_n_lok1.min(), lmax=abs_n_lok1.max())
plt.show()

# 2.3
print(np.mean(im1_n_lok1))
print(np.mean(im2_n_lok1))
print(np.std(im1_n_lok1))
print(np.std(im2_n_lok1))

d_n_lok1 = np.sum(np.sum(np.abs(im1_n_lok1-im2_n_lok1)))
d_mu_n_lok1 = np.abs(np.mean(im1_n_lok1)-np.mean(im2_n_lok1))

# 2.6
im1_n_lok2 = osum.z_norm2(im1)
im2_n_lok2 = osum.z_norm2(im2)
osum.disp_im(im1_n_lok2, title='im1 lokalna z-normalizacija 2', lmin=im1_n_lok2.min(), lmax=im1_n_lok2.max())
osum.disp_im(im2_n_lok2, title='im2 lokalna z-normalizacija 2',lmin=im2_n_lok2.min(), lmax=im2_n_lok2.max())
osum.disp_im(np.abs(im1_n_lok2-im2_n_lok2), title='abs razlika nakon lokalne z-normalizacije 2', lmin=np.abs(im1_n_lok2-im2_n_lok2).min(), lmax=np.abs(im1_n_lok2-im2_n_lok2).max())
plt.show()

print(np.mean(im1_n_lok2))
print(np.mean(im2_n_lok2))
print(np.std(im1_n_lok2))
print(np.std(im2_n_lok2))
d_n_lok2 = np.sum(np.sum(np.abs(im1_n_lok2-im2_n_lok2)))
d_mu_n_lok2 = np.abs(np.mean(im1_n_lok2)-np.mean(im2_n_lok2))

