import numpy as np
import slika_3d
import matplotlib.pyplot as plt


def main():

    # 2.2
    im = slika_3d.imread_3d('/Users/aleksandra/Desktop/vezba2/01006_t1_cma.img', '/Users/aleksandra/Desktop/vezba2/01006_t1_cma.hdr')
    im = im.astype(np.uint8)

    # 2.3
    z = 100
    im_z = im[z, :, :]
    plt.figure(1)
    plt.imshow(im_z, cmap='gray', vmin=im_z.min(), vmax=im_z.max())
    plt.axis('off')
    plt.show()

# 3.5
    def update_z(val):
        z = sl_d[0].val
        img = im[z, :, :]
        im_obj[0].set_data(img)
        fig.canvas.draw_idle()

    def update_x(val):
        x = sl_d[1].val
        img = im[:, x, :]
        img = np.flipud(img)
        im_obj[1].set_data(img)
        fig.canvas.draw_idle()

    def update_y(val):
        y = sl_d[2].val
        img = im[:, :, y]
        img = np.flipud(img)
        im_obj[2].set_data(img)
        fig.canvas.draw_idle()

    # 3.6
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2)
    ax_z = fig.add_subplot(gs[0, 0])
    ax_x = fig.add_subplot(gs[1, 0])
    ax_y = fig.add_subplot(gs[:, 1])  # y presek zauzima celu desnu kolonu
    # plt.subplots_adjust(bottom=0.1) # ukoliko je potrebno pomeriti subplot-ove od donje ivice
    ax = [ax_z, ax_x, ax_y]
    im_obj, sl_d = slika_3d.imshow_slice(im, ax, len(im.shape))
    sl_d[0].on_changed(update_z)
    sl_d[1].on_changed(update_x)
    sl_d[2].on_changed(update_y)
    plt.show()

    # 4.1
    z1, z2 = slika_3d.koordinate(im, 0)
    x1, x2 = slika_3d.koordinate(im, 1)
    y1, y2 = slika_3d.koordinate(im, 2)

    return z1, z2, x1, x2, y1, y2


if __name__ == '__main__':
    # ovaj deo koda ce se izvrsiti ukoliko se skripta poziva direktno, a ne ucitava u negde kao modul
    z1, z2, x1, x2, y1, y2 = main()
