import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
'''
# postavljanje foldera u kom se nalazi zeljeni modul (slika_3d.py) na python path
import sys
sys.path.append('putanja do foldera')
'''
import slika_3d

im = slika_3d.imread_3d('01006_t1_cma.img', '01006_t1_cma.hdr')
im = im.astype(np.uint8)

# 3.1
fig, ax = plt.subplots(1, 3)
# kada se tek otvori GUI bice prikazan presek im[0, :, :]
im_objz = ax[0].imshow(im[0, :, :], cmap='gray', vmin=im.min(), vmax=im.max())
ax[0].axis('off')
ax[0].set_title('z presek')

# 3.2
# osa na kojoj ce se nalaziti slajder
ax_sldz = plt.axes([0.1, 0.03, 0.2, 0.03])  # [left, bottom, width, height]
sldz = Slider(ax_sldz, 'z', valmin=0, valmax=im.shape[0]-1, valinit=0, valstep=1)

# kada se tek otvori GUI bice prikazan presek im[0, :, :]
im_objx = ax[1].imshow(im[:, 30, :], cmap='gray', vmin=im.min(), vmax=im.max())
ax[1].axis('off')
ax[1].set_title('x presek')

# 3.2
# osa na kojoj ce se nalaziti slajder
ax_sldx = plt.axes([0.4, 0.03, 0.2, 0.03])  # [left, bottom, width, height]
sldx = Slider(ax_sldx, 'x', valmin=0, valmax=im.shape[1]-1, valinit=0, valstep=1)

# kada se tek otvori GUI bice prikazan presek im[0, :, :]
im_objy = ax[2].imshow(im[:, :, 15], cmap='gray', vmin=im.min(), vmax=im.max())
ax[2].axis('off')
ax[2].set_title('y presek')

# 3.2
# osa na kojoj ce se nalaziti slajder
ax_sldy = plt.axes([0.7, 0.03, 0.2, 0.03])  # [left, bottom, width, height]
sldy = Slider(ax_sldy, 'y', valmin=0, valmax=im.shape[2]-1, valinit=0, valstep=1)

# 3.3
def update_z(val):
    # vrednost sa slajdera
    z = sldz.val
    # azuriranje slike
    img = im[z, :, :]
    im_objz.set_data(img)
    fig.canvas.draw_idle()



# na promenu vrednosti slajdera pozvati callback
sldz.on_changed(update_z)

def update_x(val):
    # vrednost sa slajdera
    x = sldx.val
    # azuriranje slike
    img = im[:, x, :]
    im_objx.set_data(img)
    fig.canvas.draw_idle()


# na promenu vrednosti slajdera pozvati callback
sldx.on_changed(update_x)
# plt.show()


def update_y(val):
    # vrednost sa slajdera
    y = sldy.val
    # azuriranje slike
    img = im[:, :, y]
    im_objy.set_data(img)
    fig.canvas.draw_idle()


# na promenu vrednosti slajdera pozvati callback
sldy.on_changed(update_y)
plt.show()
