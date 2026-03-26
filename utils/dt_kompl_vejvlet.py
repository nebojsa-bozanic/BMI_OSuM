import dtcwt
import numpy as np
import matplotlib.pyplot as plt
import cv2


#3.1
im = cv2.imread('1_MR.jpg', cv2.IMREAD_GRAYSCALE)

n = 2
transform = dtcwt.Transform2d()
C = transform.forward(im, nlevels=n)

#3.2
for l in range(0, n):
    fig = plt.figure()
    fig.canvas.set_window_title(('Moduo koeficijenata na nivou '+str(l)))
    for slice in range(C.highpasses[l].shape[2]):
        plt.subplot(2, 3, slice+1)
        sl = abs(C.highpasses[l][:,:,slice])
        plt.imshow(sl, cmap='gray', vmin=sl.min(), vmax=sl.max())
        plt.axis('off')

# plt.show()


for l in range(0, n):
    fig = plt.figure()
    fig.canvas.set_window_title(('Argument koeficijenata na nivou '+str(l)))
    for slice in range(C.highpasses[l].shape[2]):
        plt.subplot(2, 3, slice+1)
        sl = np.angle(C.highpasses[l][:,:,slice])
        plt.imshow(sl, cmap='gray', vmin=-np.pi, vmax=np.pi)
        plt.axis('off')

plt.show()

