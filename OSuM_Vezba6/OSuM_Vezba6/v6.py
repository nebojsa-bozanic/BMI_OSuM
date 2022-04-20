import numpy as np
import cv2
import matplotlib.pyplot as plt
import osum

# 1.1
[im, DetInfo, hdr] = osum.read_raw('Ro_01.fxd')

# 1.2
logLUT = osum.log_LUT(16384, 4096, 0.001)
im_log = logLUT[im]

# 1.3
cv2.imshow('Log slika', im_log/im_log.max())
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2.2
LPyr, GPyr, Res = osum.im_pyr_decomp(im_log, 6)

# 2.3
sigLUT = osum.sigmLUT(2000, 800, 4)
plt.figure()
plt.plot(np.arange(-2000, 2001), sigLUT)
plt.grid()
plt.show()

# 2.4
L3 = LPyr[2]
Lk = sigLUT[np.uint16(L3+2000)]

plt.figure()
plt.imshow(abs(L3), cmap='gray', vmin=abs(L3).min(), vmax=200)  # gornja granica 200 (analiza hist) da poboljsamo kontrast za prikaz
plt.axis('off')
plt.title('3. nivo LP pre pojacanja')
plt.figure()
plt.imshow(abs(Lk), cmap='gray', vmin=abs(L3).min(), vmax=200)
plt.axis('off')
plt.title('3. nivo LP nakon pojacanja')
plt.show()

# 2.5
g = np.arange(-500, 502)
h1 = np.histogram(L3, g)
h2 = np.histogram(Lk, g)

plt.figure()
plt.plot(g[:-1], h2[0], linewidth=1)
plt.plot(g[:-1], h1[0], linewidth=1)
plt.legend(['Lk', 'L3'])
plt.title('Histogram 3. nivoa LP pre i nakon pojacanja')
plt.show()

# 2.6
res_mean = np.mean(Res)
Res2 = (Res-res_mean)*0.7+res_mean  # veci faktor -manje se smanjuju varijacije u intenzitetu

# 2.7
LPyr[2] = Lk
im_rec = osum.im_pyr_recon(LPyr, Res2)

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(im_log, cmap='gray', vmin=im_log.min(), vmax=im_log.max())
plt.axis('off')
fig.canvas.set_window_title('Pre MSE')

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(im_rec, cmap='gray', vmin=im_rec.min(), vmax=im_rec.max())
plt.axis('off')
fig.canvas.set_window_title('Nakon MSE')
plt.show()

# 3.1
pojacanja = [1/0.13, 1/0.38, 1/0.68, 1/0.86, 1/0.94, 1/0.97]
# pojacanja = [1/0.13, 1/0.38, 1/0.68, 3/0.86, 3/0.94, 1/0.97] # 3.4

# 3.2
LPyr, GPyr, Res = osum.im_pyr_decomp(im_log, 6)

for i in range(0, len(LPyr)):
    sigmLUT = osum.sigmLUT(2000, 800, pojacanja[i])
    LPyr[i] = sigmLUT[np.uint16(LPyr[i]+2000)]

# 3.3
im_rec = osum.im_pyr_recon(LPyr, Res)

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(im_log, cmap='gray', vmin=im_log.min(), vmax=im_log.max())
plt.axis('off')
fig.canvas.set_window_title('Pre korekcije MTF-a')

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(im_rec, cmap='gray', vmin=im_rec.min(), vmax=im_rec.max())
plt.axis('off')
fig.canvas.set_window_title('Nakon korekcije MTF-a')
plt.show()

