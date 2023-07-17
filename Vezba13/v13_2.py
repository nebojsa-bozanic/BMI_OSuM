import cv2
import numpy as np
import matplotlib.pyplot as plt
import osum

# 3
# 3.1
im = cv2.imread('hand.tif', cv2.IMREAD_GRAYSCALE)
# im = cv2.imread('shoulder.png', cv2.IMREAD_GRAYSCALE)  # 3.10
osum.disp_im(im, title='Ulazna slika')
# plt.show()

LPyr, GPyr, Res, size_vec = osum.im_pyr_decomp(im, 3)
im_g = GPyr[2]
osum.disp_im(im_g, 'Ulazna slika na nizoj rezoluciji')
plt.show()

# 3.2
sx, sy, g, o = osum.sobel_grad(im_g)
osum.disp_im(sx, title='Gradijent po x', lmin=sx.min(), lmax=sx.max())
osum.disp_im(sy, title='Gradijent po y', lmin=sy.min(), lmax=sy.max())
osum.disp_im(g, title='Magnituda gradijenta', lmin=g.min(), lmax=g.max())
osum.disp_im(o, title='Orijentacija gradijenta', lmin=o.min(), lmax=o.max())
plt.show()

# 3.3
g = osum.im_norm(g)
t = 0.1
im_gs = g>t
osum.disp_im(im_gs, lmin=0, lmax=1, title='Lokacije sa jakim gradijentom')
plt.show()

# 3.4
d = cv2.dilate(np.uint8(im_gs), np.ones((3,3)))
osum.disp_im(d, lmin=0, lmax=1, title='Ivice i susedi oko njih')
plt.show()

# 3.5
d2 = np.logical_and(d, np.logical_not(im_gs))
osum.disp_im(np.logical_not(im_gs), lmin=0, lmax=1, title='Invertovana slika ivica')
osum.disp_im(d2, lmin=0, lmax=1, title='Susedi oko ivica')
plt.show()

# 3.6
t0 = np.mean(im_g[d2])

# 3.7
g_tamno = im_g<t0
g_svetlo = im_g>=t0
osum.disp_im(g_tamno, lmin=0, lmax=1, title='Pozadina')
osum.disp_im(g_svetlo, lmin=0, lmax=1, title='Anatomija')
plt.show()

# 3.8
t_svetlo = np.mean(im_g[g_svetlo])
t_tamno = np.mean(im_g[g_tamno])
tc = (t_svetlo+t_tamno)/2

# 3.9
im_s = im>tc
osum.disp_im(im>tc, lmin=0, lmax=1, title='Segmentirana slika')
plt.show()
