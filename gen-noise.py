import cv2
import numpy as np
from matplotlib import pyplot as plt


def add_gaussian_noise(image, mean=0, sigma=25):
    """
    Thêm nhiễu Gauss vào ảnh.
    """
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy = np.clip(image + gauss.reshape(row, col), 0, 255)
    return noisy.astype(np.uint8)


def add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    """
    Thêm nhiễu muối và tiêu vào ảnh.
    """
    noisy = np.copy(image)
    total_pixels = image.size

    # Thêm nhiễu muối
    num_salt = np.ceil(salt_prob * total_pixels)
    salt_coords = [np.random.randint(0, i - 1, int(num_salt))
                   for i in image.shape]
    noisy[salt_coords[0], salt_coords[1]] = 255

    # Thêm nhiễu tiêu
    num_pepper = np.ceil(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(
        0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[pepper_coords[0], pepper_coords[1]] = 0

    return noisy.astype(np.uint8)


def generate_random_binary_image(size=(256, 256), threshold=0.5):
    """
    Tạo ảnh nhị phân ngẫu nhiên.
    """
    random_binary_image = np.random.rand(*size) < threshold
    random_binary_image = random_binary_image.astype(np.uint8) * 255
    return random_binary_image


# Tạo ảnh nhị phân
image_size = (256, 256)
binary_image = generate_random_binary_image()

# Thêm nhiễu Gauss
noisy_gaussian_image = add_gaussian_noise(binary_image)

# Thêm nhiễu muối và tiêu
noisy_salt_and_pepper_image = add_salt_and_pepper_noise(binary_image)

# Hiển thị và lưu ảnh
plt.subplot(131), plt.imshow(
    binary_image, cmap='gray'), plt.title('Original Image')
plt.subplot(132), plt.imshow(noisy_gaussian_image,
                             cmap='gray'), plt.title('Noisy Gaussian Image')
plt.subplot(133), plt.imshow(noisy_salt_and_pepper_image,
                             cmap='gray'), plt.title('Noisy Salt and Pepper Image')

plt.show()

# Lưu ảnh
cv2.imwrite('images/binary/original.png', binary_image)
cv2.imwrite('images/binary/gauss-noise.png', noisy_gaussian_image)
cv2.imwrite('images/binary/salt-pepper-noise.png',
            noisy_salt_and_pepper_image)
