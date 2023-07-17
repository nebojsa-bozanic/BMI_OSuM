import cv2
import matplotlib.pyplot as plt
import numpy as np
import osum

# 1
# 1.1
r = cv2.imread('RAD_HE.png', cv2.IMREAD_GRAYSCALE)
t = cv2.imread('REG_LE_01.PNG', cv2.IMREAD_GRAYSCALE)

osum.disp_im(r, title='Referentna slika')
osum.disp_im(t, title='Test slika')
plt.show()

# 1.2
v,k = r.shape
v1 = round(0.15*v)
v2 = round(0.75*v)
k1 = round(0.1*k)
k2 = round(0.9*k)
r_roi = r[v1-1:v2, k1-1:k2]
osum.disp_im(r_roi, title='Referentni ROI')
plt.show()

# 1.3
nx = 0.5
ny = 0.5
[X, Y] = np.meshgrid(np.arange(k1-1, k2, nx), np.arange(v1-1, v2, ny))
X = np.float32(X) # funkcija cv2.remap zahteva koordinate u tipu float32
Y = np.float32(Y)
iR = cv2.remap(r, X, Y, interpolation=cv2.INTER_LINEAR)
osum.disp_im(iR, title='Referentni ROI, veca rezolucija')
plt.show()

# 1.4
[X, Y] = np.meshgrid(np.arange(500, 801), np.arange(500, 801))
X = np.float32(X)
Y = np.float32(Y)
iR = cv2.remap(r, X, Y, interpolation=cv2.INTER_LINEAR, borderValue=100)
osum.disp_im(iR, title='Interpolacija van domena slike')
plt.show()

# 1.5
[X, Y] = np.meshgrid(np.arange(k1-1, k2), np.arange(v1-1, v2))
X = np.float32(X)
Y = np.float32(Y)
iR = cv2.remap(r, X, Y, interpolation=cv2.INTER_LINEAR)
iT = cv2.remap(t, X, Y, interpolation=cv2.INTER_LINEAR)
sAbs = np.sum(np.abs(iR-iT))

# 1.6
iRz = cv2.remap(osum.z_norm(r), X, Y, interpolation=cv2.INTER_LINEAR)
iTz = cv2.remap(osum.z_norm(t), X, Y, interpolation=cv2.INTER_LINEAR)
sAbsZ = np.sum(np.abs(iRz-iTz))

# 2
# 2.1
[x, y] = np.meshgrid(np.arange(k1-1, k2), np.arange(v1-1, v2))
x = np.float32(x)
y = np.float32(y)
iRz = cv2.remap(osum.z_norm(r), x, y, interpolation=cv2.INTER_LINEAR)

x_tr = X+2
y_tr = Y+3
iTt = cv2.remap(osum.z_norm(t), x_tr, y_tr, interpolation=cv2.INTER_LINEAR)

sAbst = np.sum(np.abs(iRz-iTt))

# 2.2
th_deg = 30
th = th_deg*np.pi/180 # transformacija iz stepena u radijane
# koordinatni pocetak u gornjem levom uglu slike
# xc = 0
# tc = 0
# tacka u centru slike
xc = int(np.floor(r.shape[1]/2))
yc = int(np.floor(r.shape[0]/2))
[x, y] = np.meshgrid(np.arange(0, r.shape[1]), np.arange(0, r.shape[0]))
xr = np.cos(th)*(x-xc)-np.sin(th)*(y-yc)+xc
yr = np.sin(th)*(x-xc)+np.cos(th)*(y-yc)+yc
xr = np.float32(xr)
yr = np.float32(yr)
rr = cv2.remap(r, xr, yr, interpolation=cv2.INTER_LINEAR, borderValue=0)
osum.disp_im(rr, title='Rotacija za ugao od '+str(th_deg)+' stepeni')
plt.show()

# 2.3
s = 4
# s = 0.5
# koordinatni pocetak u gornjem levom uglu slike
# xc = 0
# yc = 0
# tacka u centru slike
xc = int(np.floor(r.shape[1]/2))
yc = int(np.floor(r.shape[0]/2))
xs = np.float32(s*(x-xc)+xc)
ys = np.float32(s*(y-yc)+yc)
rs = cv2.remap(r, xs, ys, interpolation=cv2.INTER_LINEAR, borderValue=0)
osum.disp_im(rs, title='Slika sa uvelicanjem/umanjenjem '+str(1/s))
plt.show()

# 3
# 3.1
osum.disp_im(r, title='Definisati referentni region pluca za registraciju')
# potrebno je zakomentarisati svaku liniju plt.show() iznad da bi sledeca linija koda radila kako treba
refPts = plt.ginput(2)  # funkcija ocekuje koordinate 2 tacke koje unese korisnik
plt.show()
# potrebne su int vrednosti za indeksiranje
refPts1 = [int(np.round(pt)) for pt in refPts[0]]
refPts2 = [int(np.round(pt)) for pt in refPts[1]]
k1,v1 = refPts1
k2,v2 = refPts2
ref_roi = r[v1:v2+1, k1:k2+1]

osum.disp_im(ref_roi, title='Referenti ROI za registraciju')
plt.show()

# 3.2
[X, Y] = np.meshgrid(np.arange(k1, k2+1), np.arange(v1, v2+1))  # ne treba k1-1... jer ginput belezi koordinate pocevsi od 0
X = np.float32(X)
Y = np.float32(Y)
iR = cv2.remap(osum.z_norm(r), X, Y, interpolation=cv2.INTER_LINEAR, borderValue=0)

# 3.3
d = np.zeros((41, 41))
for tx in range(-20, 21):
    for ty in range(-20, 21):
        X_test = np.float32(X+tx)
        Y_test = np.float32(Y+ty)
        iT = cv2.remap(osum.z_norm(t), X_test, Y_test, interpolation=cv2.INTER_LINEAR, borderValue=0)
        d[ty+20, tx+20] = np.sum(np.abs(iR-iT))

# 3.4
i, j = np.where(d==d.min())
dMin = d[i,j]
x_opt = j-20
y_opt = i-20

# 3.5
fig = plt.figure()
ax = plt.axes(projection='3d')
[x, y] = np.meshgrid(np.arange(-20, 21), np.arange(-20, 21))  # pomeraji po x i y-osi
ax.plot_surface(x, y, d, cmap='viridis')
plt.show()

