import pydicom as dicom
import matplotlib.pyplot as plt

# 7.1
dc = dicom.dcmread('00044.dcm') # ukoliko se fajl nalazi u drugom folderu ovde staviti putanju do njega
print(dc)
print()

# 7.2
del dc.PatientID

# 7.3
dc.PatientName = ''
dc.PatientID = '000123_123'
dc.save_as('00044_1.dcm')

# 7.4
print(dc[0x0010, 0x0020])

# 7.5
im = dc.pixel_array
plt.figure(1)
plt.imshow(im, cmap='gray', vmin=im.min(), vmax=im.max())
plt.show()
print()
print(dc[0x0008, 0x0060])