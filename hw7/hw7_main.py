# Name & uwnetid: Youngwon Kim & 1724787

import imageio
import matplotlib.pyplot as plt
import numpy as np


def invert_colors(image):
    '''
    Returns the image that has inverted colors from an original image.
    The inverted image consists of a numpy array.

    Takes a color image as an argument.
    '''
    result = np.zeros(image.shape, dtype=int)
    a = np.zeros(image.shape)+255
    result[:, :, 0] = a[:, :, 0]-image[:, :, 0]
    result[:, :, 1] = a[:, :, 1]-image[:, :, 1]
    result[:, :, 2] = a[:, :, 2]-image[:, :, 2]
    return result


def blur(image, patch_size):
    '''
    Returns a blurred image using the patch size.
    The blurred image consists of a numpy array of integer.

    Takes a gray-scale image and patch size as arguments.
    '''
    size = patch_size
    x, y = image.shape
    xx, yy = x - size + 1, y - size + 1
    patch_means = np.zeros((xx, yy))
    for i in range(xx):
        for j in range(yy):
            patch_means[i, j] = image[i: i+size, j: j+size].mean()
    return patch_means.astype(np.uint8)


def template_match(big_image, small_image):
    '''
    Returns a two dimensional (gray-scale) array containing the similarity
    between big and small (template) images.
    The array is a numpy array of floats.

    Takes a large and small gray-scale images as arguments.
    '''
    smallx, smally = small_image.shape
    bigx, bigy = big_image.shape
    xstop = bigx - smallx + 1
    ystop = bigy - smally + 1
    result = np.zeros((xstop, ystop))
    for x in range(xstop):
        for y in range(ystop):
            curr = big_image[x:x+smallx, y:y+smally]
            curr_mean = big_image[x:x+smallx, y:y+smally].mean()
            tem = small_image
            tem_mean = small_image.mean()
            result[x, y] = np.sum((curr-curr_mean)*(tem-tem_mean))
    return result


# finx_xy and plot_result are functions created by instructors.


def find_xy(result):
    """
    Given the result of template_match, finds the position (x, y) with
    the highest similarity.
    """
    ij = np.unravel_index(np.argmax(result), result.shape)
    return ij[::-1]


def plot_result(image, template, result):
    """
    Given an image, a template, and the result of
    template_match(image, template), makes a plot showing the result
    of the match.
    """
    x, y = find_xy(result)

    plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 2)
    ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('template')

    ax2.imshow(image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    template_height,  template_width = template.shape
    rect = plt.Rectangle((x, y), template_width, template_height,
                         edgecolor='r', facecolor='none')
    ax2.add_patch(rect)

    ax3.imshow(result)
    ax3.set_axis_off()
    ax3.set_title('`match_template`\nresult')
    # highlight matched region
    ax3.autoscale(False)
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none',
             markersize=10)
    plt.show()


def main():
    puppy = imageio.imread('images/puppy.png')
    gray_puppy = imageio.imread('images/gray_puppy.png')
    coins = imageio.imread('images/coins.png')
    invert_colors(puppy)
    blur(gray_puppy, 10)
    blur(gray_puppy, 30)
    template = template_match(coins, coins[170:220, 75:130])
    result = find_xy(coins[170:220, 75:130])
    plot_result(coins, template, result)


if __name__ == '__main__':
    main()
