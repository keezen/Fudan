# python: 2.7
# encoding: utf-8

import numpy as np
import struct
import matplotlib.pyplot as plt
import pickle


def read_image(path):
    """Read images from mnist files."""

    # read binary data
    with open(path, 'rb') as f:
        buf = f.read()

    # read header info
    offset = 0
    fmt_header = '>IIII'
    magic, n_images, n_rows, n_cols = \
        struct.unpack_from(fmt_header, buf, offset)
    print 'magic number: %d, number of images:%d, image size: %dx%d' \
        % (magic, n_images, n_rows, n_cols)
    offset += struct.calcsize(fmt_header)

    # read images
    image_size = n_rows * n_cols
    fmt_img = '>' + str(image_size) + 'B'
    imgs = np.empty(shape=(n_images, image_size), dtype=np.int32)
    for i in range(n_images):
        img = struct.unpack_from(fmt_img, buf, offset)
        imgs[i] = np.array(img)
        offset += struct.calcsize(fmt_img)

    return imgs


if __name__ == '__main__':
    # read mnist images
    path = u'train-images-idx3-ubyte'
    imgs = read_image(path)  # 60000x784
    imgs = np.reshape(imgs, (-1, 28, 28))  # 60000x28x28
    imgs_bin = np.copy(imgs)
    imgs_bin[imgs_bin >= 1] = 1
    print 'mnist:', imgs.shape

    # show images
    # print imgs[0]
    # # print imgs_bin[0]
    # for i in range(9):
    #     plt.subplot(3, 3, i + 1)
    #     # plt.imshow(imgs[i], cmap='binary')
    #     plt.imshow(imgs_bin[i], cmap='binary')
    # plt.show()

    # save images
    np.save('mnist.npy', imgs)
    np.save('mnist_bin.npy', imgs_bin)
    # with open('mnist_bin.pkl', 'wb') as f:
    #     pickle.dump(imgs_bin.tolist(), f)
