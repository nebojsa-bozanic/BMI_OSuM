import cv2
import osum
import matplotlib.pyplot as plt
import numpy as np

# 1.1
[im, DetInfo, hdr] = osum.read_raw('Ro_01.fxd')

# 1.3
cv2.imshow('Ulazna slika', im/im.max())
cv2.waitKey(0)
# cv2.destroyAllWindows()

# 1.4
g = np.arange(0, 16385, 8)
h1 = np.histogram(im, g)

# 1.5
plt.figure()
plt.plot(g[:-1], h1[0])
plt.show()

# 2.2
lut = osum.log_LUT(16384, 4096, 0.001)
# lut = osum.log_LUT(16384, 4096, 0.1) # 2.5
im_log = lut[im]

# 2.3
cv2.imshow('Slika nakon log kompresije opsega', im_log/im_log.max())
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2.4
h2 = np.histogram(im_log, g)

plt.figure()
plt.plot(g[:-1], h1[0])
plt.plot(g[:-1], h2[0], 'r')
plt.legend(['original', 'log kompresija'])
plt.show()

