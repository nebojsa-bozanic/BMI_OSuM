import pydicom as dicom
import numpy as np
import cv2

# 1.1
pd = dicom.dcmread('0002.DCM')
im = pd.pixel_array

# 1.2
im = np.swapaxes(im, 0, 1)
im = np.swapaxes(im, 1, 2)

# 1.3
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
fps = 10  # frame rate
frame_size = (im.shape[0], im.shape[1])  # dimeznije frejma; ako je izostavljen korak 1.2 prilagoditi ovaj deo
isColour = 0

# Video Writer objekat
video_out = cv2.VideoWriter('videoXA.avi', fourcc, fps, frame_size, isColour)

# zapisivanje frejm po frejm
for i in range(im.shape[2]):
    video_out.write(im[:, :, i])

video_out.release()

# 1.4

# Video Capture objekat
cap = cv2.VideoCapture('videoXA.avi')
while cap.isOpened():  # cap.isOpened bice true ako je inicijalizacija prosla kako treba
    # citanje frejm po frejm; ret - true ako je frejm procitan
    ret, frame = cap.read()
    if not ret:
        break
    # frejm se prikazuje kao slika
    cv2.imshow('Video', frame)
    # delay nakon koga se prikazuje sledeci frejm - to nizanje frejmova vidimo kao vide0
    cv2.waitKey(100)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
