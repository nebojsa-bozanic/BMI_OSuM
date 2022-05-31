import cv2
import numpy as np
import pywt
import bm3d

# 3.1
im = cv2.imread('abdomen_crop.png', cv2.IMREAD_GRAYSCALE)

# 3.2
im_f1 = cv2.fastNlMeansDenoising(im, templateWindowSize=11, searchWindowSize=11, h=9)
# vece h - vise se ocuvavaju ivice ali i sum
# templateWindow i searchWindow ne moraju da budu istih dimenzija

cv2.imshow('Originalna slika', im)
cv2.waitKey(0)

cv2.imshow('Non-local Mens', im_f1)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# 3.2
w = 'db4'
n = 2
C = pywt.wavedec2(im, wavelet=w, mode='periodization', level=n)
cA2 = C[0]
(cH2, cV2, cD2) = C[1]
(cH1, cV1, cD1) = C[2]
C = [list(c) for c in C]

sigma = np.median(np.abs(cD1))/0.6745
im_f2 = bm3d.bm3d(im, sigma_psd=sigma, stage_arg=bm3d.BM3DStages.ALL_STAGES)

cv2.imshow('BM3D', np.uint8(im_f2))
cv2.waitKey(0)
cv2.destroyAllWindows()
