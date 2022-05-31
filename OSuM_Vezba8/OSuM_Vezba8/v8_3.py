import cv2
import osum
import os
from scipy.ndimage.filters import convolve1d
import numpy as np

# 4.1
d = 'Img_1'
files = [os.path.join(d,f) for f in sorted(os.listdir(d))]
[im, DetInfo, hdr] = osum.read_raw(files[0])

im_sekv = np.zeros((im.shape[0], im.shape[1], len(files)))

# 4.2
logLUT = osum.log_LUT(2**16, 2**16, 0.001)

# 4.3
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
fps = 4  # proizvoljno
frame_size = (im.shape[0], im.shape[1])
isColour = 0
video_out = cv2.VideoWriter('fluoro.avi', fourcc, fps, frame_size, isColour)

# 4.4
for i in range(len(files)):
    [im, DetInfo, hdr] = osum.read_raw(files[i])
    im = logLUT[im]
    im_sekv[:,:,i] = im
    video_out.write(np.uint8((1-osum.im_norm(im))*255))

video_out.release()

# 4.5
g, x_osa = osum.gaussian(11, 2)
im_f = convolve1d(im_sekv, g, axis=2, mode='nearest')

# 4.6
video_out2 = cv2.VideoWriter('fluoro_filt.avi', fourcc, fps, frame_size, isColour)
for i in range(im_f.shape[2]):
    fr = im_f[:,:,i]
    video_out2.write(np.uint8((1-osum.im_norm(fr))*255))

video_out2.release()

