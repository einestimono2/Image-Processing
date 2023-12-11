import cv2
import numpy as np
import matplotlib.pyplot as plt


def fft(img):
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * \
        np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    # plt.subplot(121), plt.imshow(img, cmap='gray')
    # plt.title(' Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    # plt.title(' Image Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    # plt.show()
    return magnitude_spectrum


def show_io_fft(input_image, output_image):
    plt.figure("Magnitude Spectrum")

    if type(output_image) != str:
        plt.subplot(221), plt.imshow(input_image, cmap='gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(222), plt.imshow(fft(input_image), cmap='gray')
        plt.title('Input Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.subplot(223), plt.imshow(output_image, cmap='gray')
        plt.title('Result Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(224), plt.imshow(
            fft(output_image), cmap='gray')
        plt.title('Result Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    else:
        plt.subplot(121), plt.imshow(input_image, cmap='gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(fft(input_image), cmap='gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.show()


def gaussian_filter(img):
    output_image = cv2.GaussianBlur(img, (5, 5), 0)
    result_path = 'images/result.png'
    cv2.imwrite(result_path, output_image)
    return (result_path, output_image)


def median_filter(img):
    output_image = cv2.medianBlur(img, 5)
    result_path = 'images/result.png'
    cv2.imwrite(result_path, output_image)
    return (result_path, output_image)
