# services.py
import os
import uuid
import cv2
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
from skimage.exposure import match_histograms


# TODO (DONE): Utility functions
def hex_to_bgr(hex_color):
    # Menghilangkan '#' dari hex dan mengonversi ke RGB
    hex_color = hex_color.lstrip('#')
    # Memisahkan warna menjadi tuple (R, G, B)
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    # OpenCV menggunakan BGR, jadi kita balik urutan
    return (rgb[2], rgb[1], rgb[0])


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Save image to a folder


def save_image(image_file, upload_folder):
    file_extension = image_file.name.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    image_file_path = os.path.join(upload_folder, filename)

    with open(image_file_path, "wb") as f:
        f.write(image_file.read())

    return image_file_path

# Load image and convert to NumPy array


# Function to convert uploaded image to NumPy array
def load_image_to_numpy(image_file):
    # Reset the file pointer to the start
    image_file.seek(0)
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if img is None:
        raise ValueError(
            "Failed to decode image. Please check if the image file is valid.")
    return img


# TODO (DONE): RGB Array functions
# Get rgb array from image data
def get_rgb_array_from_image_data(image_data):
    # convert to RGB
    image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
    b, g, r = cv2.split(image_data)
    rgb_array = {"R": r.tolist(), "G": g.tolist(), "B": b.tolist()}
    return rgb_array


# TODO (DONE): Image operations
# Arithmetic operations on images
def arithmetic_operation_on_image(img, value, operation: str = "add"):
    try:
        int_value = np.uint8(value)
        if operation == "add":
            result_img = cv2.add(img, np.full(
                img.shape, int_value, dtype=np.uint8))
        elif operation == "subtract":
            result_img = cv2.subtract(img, np.full(
                img.shape, int_value, dtype=np.uint8))
        elif operation == "max":
            result_img = np.maximum(img, np.full(
                img.shape, int_value, dtype=np.uint8))
        elif operation == "min":
            result_img = np.minimum(img, np.full(
                img.shape, int_value, dtype=np.uint8))
        elif operation == "inverse":
            result_img = cv2.bitwise_not(img)
        return result_img
    except Exception as e:
        raise e

# Logical operations on images


def logical_operation_on_image(img1, img2=None, operation: str = "and"):
    try:
        if operation == "not":
            return cv2.bitwise_not(img1)
        if img2 is not None:
            if operation == "and":
                return cv2.bitwise_and(img1, img2)
            elif operation == "xor":
                return cv2.bitwise_xor(img1, img2)
    except Exception as e:
        raise e
    return img1


def resize_to_match(image1, image2):
    height, width = image1.shape[:2]
    return cv2.resize(image2, (width, height))


# TODO (DONE): Gray scale conversion

def is_gray_scale(img):
    return len(img.shape) == 2


def convert_to_gray_scale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# TODO (DONE): Histogram grayscale
def histogram_gray_scale(img):
    # Create a plot for the histogram
    if not is_gray_scale(img):
        img = convert_to_gray_scale(img)
    plt.figure(figsize=(8, 6))
    plt.hist(img.ravel(), 256, [0, 256])
    plt.title("Histogram of Grayscale Image")
    plt.xlabel("Pixel Values")
    plt.ylabel("Frequency")
    plt.grid()

    # Save plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)

    # Load image from buffer and return
    return Image.open(buf)

# TODO (DONE): Histogram RGB


def histogram_rgb(image):
    # Create a plot for the histogram
    plt.figure(figsize=(8, 6))
    for i, col in enumerate(['r', 'g', 'b']):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
    plt.title("Histogram of RGB Image")
    plt.xlabel("Pixel Values")
    plt.ylabel("Frequency")
    plt.grid()

    # Save plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)

    # Load image from buffer and return
    return Image.open(buf)


# TODO (DONE): Histogram equalization
def histogram_equalization(img):
    # apakah gambar sudah grayscale? jika ya maka lanjutkan jika tidak maka convert dulu
    if not is_gray_scale(img):
        img = convert_to_gray_scale(img)
    return cv2.equalizeHist(img)

# TODO (DONE): Histogram specification


def histogram_specification(img, ref_img):
    specified_img = match_histograms(img, ref_img, channel_axis=-1)
    return specified_img


# TODO (DONE): Operations Convolutions
def apply_convolution(image, kernel_type: str = "sharpen"):
    # define kernel
    kernel = None
    if kernel_type == "average":
        kernel = np.ones((3, 3), np.float32) / 9
    elif kernel_type == "sharpen":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    elif kernel_type == "edge_detection":
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    else:
        raise ValueError("Invalid convolution type")
    return cv2.filter2D(image, -1, kernel)


def apply_zero_padding(image, padding_size=10, color=[255, 255, 255]):
    return cv2.copyMakeBorder(image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT, value=color)


def apply_filter(image, filter_type: str = "low"):
    if filter_type == "low":
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif filter_type == "high":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)
    elif filter_type == "band":
        low_pass = cv2.GaussianBlur(image, (9, 9), 0)
        high_pass = image - low_pass
        return low_pass + high_pass
    else:
        raise ValueError("Invalid filter type")


def apply_fourier_transform(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    # Tambahkan +1 untuk mencegah log(0)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

    # Normalisasi ke rentang [0, 1]
    magnitude_spectrum = (magnitude_spectrum - np.min(magnitude_spectrum)) / \
        (np.max(magnitude_spectrum) - np.min(magnitude_spectrum))

    return magnitude_spectrum


def reduce_periodic_noise(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    rows, cols = gray.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.uint8)
    r = 30  # Radius dari mask
    mask[crow-r:crow+r, ccol-r:ccol+r] = 0
    fshift = fshift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    # return np.abs(img_back)
    # return processed_image_to_image(np.abs(img_back))
    return normalize_amplitude(np.abs(img_back))


def processed_image_to_image(processed_img):
    _, buffer = cv2.imencode('.png', processed_img)
    byte_io = BytesIO(buffer)
    return Image.open(byte_io)


def normalize_amplitude(image):
    return (image - np.min(image)) / (np.max(image) - np.min(image))


def apply_salt_and_pepper_noise(image, prob, salt_color=(255, 255, 255), pepper_color=(0, 0, 0)):
    output = np.copy(image)
    # Jika input gambar adalah grayscale, maka salt_color dan pepper_color perlu disesuaikan
    if len(output.shape) == 2:  # Grayscale image
        salt_color = salt_color[0]  # Ambil nilai channel pertama
        pepper_color = pepper_color[0]

    probs = np.random.random(output.shape[:2])
    # Terapkan noise salt
    output[probs < (prob / 2)] = salt_color
    # Terapkan noise pepper
    output[probs > 1 - (prob / 2)] = pepper_color
    return output


def remove_noise(image):
    # return processed_image_to_image(cv2.medianBlur(image, 5))
    return normalize_amplitude(cv2.medianBlur(image, 5))


def sharpen_image(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # return processed_image_to_image(cv2.filter2D(image, -1, kernel))
    return normalize_amplitude(cv2.filter2D(image, -1, kernel))
