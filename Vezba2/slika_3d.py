import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# 2.1
def imread_3d(img_path, hdr_path):
    f_img = open(img_path, 'rb')
    f_hdr = open(hdr_path, 'rb')

    img = np.fromfile(f_img, np.dtype('uint16'))
    f_hdr.seek(40)  # postavljanje pointera na zeljenu lokaciju
    hdr = np.fromfile(f_hdr, np.dtype('uint16'))

    ndims = hdr[0]
    im_dims = hdr[1:ndims + 1]
    image = img.reshape(im_dims)

    f_img.close()
    f_hdr.close()

    return image


# 3.4
def imshow_slice(img, ax, ndims):
    im_obj = []
    sl_d = []
    for dim in range(ndims):
        # promenljive koje je potrebno definisati u zavisnosti od dimenzije
        if dim == 0:
            # pocetni prikaz za presek po z-osi
            image = img[0, :, :]
            dim_str = 'z'
            # udaljenost slajdera od leve ivice
            axs_l = 0.1
        elif dim == 1:
            # pocetni prikaz za presek po x-osi
            image = img[:, 0, :]
            # slika je 'izvrnuta' po x dimenziji pa je treba ispraviti
            image = np.flipud(image)
            dim_str = 'x'
            # udaljenost slajdera od leve ivice
            axs_l = 0.4
        elif dim == 2:
            # pocetni prikaz za presek po y-osi
            image = img[:, :, 0]
            # slika je 'izvrnuta' po y dimenziji pa je treba ispraviti
            image = np.flipud(image)
            # udaljenost slajdera od leve ivice
            dim_str = 'y'
            axs_l = 0.7

        im_obj_dim = ax[dim].imshow(image, cmap='gray', vmin=img.min(), vmax=img.max())
        im_obj.append(im_obj_dim)
        ax[dim].set_title(dim_str+' presek')
        ax[dim].axis('off')
        ax_d = plt.axes([axs_l, 0.02, 0.2, 0.03])
        sl_d_dim = Slider(ax_d, dim_str, valmin=0, valmax=img.shape[dim] - 1, valinit=0, valstep=1)
        sl_d.append(sl_d_dim)

    return im_obj, sl_d


# 4.1
def koordinate(im, dim):
    c = 1
    # prolaz kroz svaki presek dimenzije dim
    for i in range(im.shape[dim]):
        if dim == 0:
            tmp = im[i, :, :]
        elif dim == 1:
            tmp = im[:, i, :]
        elif dim == 2:
            tmp = im[:, :, i]

        # ukoliko ima makar jedan piksel cija vrednost nije 0 - detektovan sadrzaj slike;
        if tmp.any() and c == 1:
            pocetak = i
            c = 2  # da se ne prebrise koordinata pocetka u sledecoj iteraciji

        # krajnja koordinata se trazi samo ako je vec pronadjen pocetak (c==2)
        if not tmp.any() and c == 2:
            kraj = i-1  # poslednja koordinata na kojoj se nalazio sadrzaj
            break

    return pocetak, kraj




