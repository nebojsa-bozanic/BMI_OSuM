import math
import cv2

# 1.1
def gaussian(n=5, sigma=1):

    x = range(-int(n/2), int(n/2)+1)
    # raspakivanje liste
    x_osa = [*x]
    # prolazak kroz svaki element liste
    f = [1/(sigma*math.sqrt(2*math.pi))*math.exp(-float(el)**2/(2*sigma**2)) for el in x]

    return f, x_osa


# 2.6
def im_norm(im):
    im_n = (im-im.min())/(im.max()-im.min())
    return im_n


# 4.2
def im_pyr_decomp(im, N):
    # Funkcija pravi Gausovu i Laplasovu piramidu od N nivoa od slike im
    GPyr = []
    LPyr = []
    for i in range(N):
        GPyr.append(im)
        g = cv2.pyrDown(im, borderType=cv2.BORDER_REPLICATE)
        l = im - cv2.pyrUp(g, cv2.BORDER_REPLICATE)
        LPyr.append(l)
        im = g
    Res = im
    return LPyr, GPyr, Res


# 4.4
def im_pyr_recon(LPyr, Res):
    # Funkcija rekonstruise sliku na osnovu Laplasove piramide i reziduala

    # dubina razlaganja
    N = len(LPyr)
    for i in range(N, 0, -1):
        Res = cv2.pyrUp(Res, cv2.BORDER_REFLECT)+LPyr[i-1]

    im_rec = Res
    return im_rec
