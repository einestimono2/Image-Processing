import cv2
import numpy as np

# Đọc ảnh từ file
image_path = 'images/binary/original.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh có được đọc thành công hay không
if image is None:
    print("Không thể đọc ảnh. Đảm bảo đường dẫn ảnh là chính xác.")
else:
    # In ma trận dữ liệu
    print("Ma trận dữ liệu của ảnh:")
    print(image)

    # In kích thước của ảnh
    print("\nKích thước ảnh:", image.shape)

    # Hiển thị ảnh (chỉ để kiểm tra)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
