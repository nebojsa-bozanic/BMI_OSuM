import numpy as np
import osum
import matplotlib.pyplot as plt
import pydicom

# 1.1
[im, DetInfo, hdr] = osum.read_raw('Ro_01.fxd')

logLUT = osum.log_LUT(16384, 4096, 0.001)
im_log = logLUT[im]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_log, cmap='gray', vmin=im_log.min(), vmax=im_log.max())
plt.axis('off')
fig.canvas.set_window_title('Logaritamska kompresija opsega')
plt.show()

# 1.2
Lpyr, Gyr, Res, size_vec = osum.im_pyr_decomp(im_log, 4)

# 1.3
sigLUT_z = osum.sigmLUT_z(2000, 800, 7, 0.05)
sigLUT_lin = osum.sigmLUT_lin(2000, 800, 7, 0.05)
sigLUT1 = osum.sigmLUT(2000, 800, 7)
sigLUT2 = osum.sigmLUT(2000, 800, 3)

Lpyr[0] = sigLUT_z[np.uint16(Lpyr[0]+2000)]
Lpyr[1] = sigLUT_lin[np.uint16(Lpyr[1]+2000)]
Lpyr[2] = sigLUT1[np.uint16(Lpyr[2]+2000)]
Lpyr[3] = sigLUT2[np.uint16(Lpyr[3]+2000)]

# 1.4
im_mse = osum.im_pyr_recon(Lpyr, Res, size_vec)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_mse, cmap='gray', vmin=im_mse.min(), vmax=im_mse.max())
plt.axis('off')
fig.canvas.set_window_title('MSE')
plt.show()

# 2.1
g = np.arange(round(im_mse.min()), round(im_mse.max())+1, 20)
h = np.histogram(im_mse, g)
plt.figure()
plt.plot(g[:-1], h[0])
plt.title('Histogram MSE slike')
plt.show()

# 2.2
Lmin = -350
Lmax = 3000

# 2.3
im_ts1  =im_mse
im_ts1[im_ts1<Lmin] = Lmin
im_ts1[im_ts1>Lmax] = Lmax
im_ts1 = (1-osum.im_norm(im_ts1))*255

plt.figure()
plt.imshow(im_ts1, cmap='gray', vmin=im_ts1.min(), vmax=im_ts1.max())
plt.axis('off')
plt.title('Linearno toniranje 1')
plt.show()

# 2.4
hn = h[0]/np.sum(h[0])
ch = np.cumsum(hn)
plt.figure()
plt.plot(g[:-1], hn)
plt.title('Normalizovani histogram')

plt.figure()
plt.plot(g[:-1], ch)
plt.title('Kumulativni histogram')
plt.show()

# 2.7
limits = osum.stat_hist_lims_fromh(hn, g[:-1], [0.001, 0.01])
Lmin = limits[0]
Lmax = limits[1]

im_ts2 = im_mse
im_ts2[im_ts2<Lmin] = Lmin
im_ts2[im_ts2>Lmax] = Lmax
im_ts2 = np.uint8((1-osum.im_norm(im_ts2))*255)

plt.figure()
plt.imshow(im_ts2, cmap='gray')
plt.axis('off')
plt.title('Linearno toniranje 2')
plt.show()

# 2.8
dc = pydicom.dcmread('00044.dcm')
im = dc.pixel_array

plt.figure()
plt.imshow(im, cmap='gray', vmin=im.min(), vmax=im.max())
plt.axis('off')
plt.title('CT pre toniranja')

L = int(dc.WindowCenter[0])
W = int(dc.WindowWidth[0])
Lmin = L-0.5*W
Lmax = L+0.5*W

im[im<Lmin] = Lmin
im[im>Lmax] = Lmax

plt.figure()
plt.imshow(im, cmap='gray', vmin=Lmin, vmax=Lmax)
plt.axis('off')
plt.title('CT nakon toniranja')
plt.show()

# 3.2
im_ts3 = osum.ts_sigma(im_mse, [0.5, 3], 4096)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.imshow(im_ts3, cmap='gray', vmin=im_ts3.min(), vmax=im_ts3.max())
plt.axis('off')
fig.canvas.set_window_title('Sgmoidalno toniranje')
plt.show()








