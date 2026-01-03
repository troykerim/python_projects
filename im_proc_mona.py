import cv2
import numpy as np
import time

def show_image(window_name, image, duration=3):
    cv2.imshow(window_name, image)
    cv2.waitKey(duration * 1000)

def shift_channel_dynamic(image, channel, duration=6):
    h, w, _ = image.shape
    shifted_image = image.copy()
    start_time = time.time()
    while time.time() - start_time < duration:
        shift_x = np.random.randint(-30, 30)
        shift_y = np.random.randint(-30, 30)
        translation_matrix = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
        shifted_image[:, :, channel] = cv2.warpAffine(image[:, :, channel], translation_matrix, (w, h))
        cv2.imshow("Video", shifted_image)
        cv2.waitKey(100)

def shift_all_channels_dynamic(image, duration=6):
    h, w, _ = image.shape
    start_time = time.time()
    while time.time() - start_time < duration:
        shifted_image = image.copy()
        for c in range(3):
            shift_x = np.random.randint(-30, 30)
            shift_y = np.random.randint(-30, 30)
            translation_matrix = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
            shifted_image[:, :, c] = cv2.warpAffine(image[:, :, c], translation_matrix, (w, h))
        cv2.imshow("Video", shifted_image)
        cv2.waitKey(100)

def main(image_path):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    aspect_ratio = w / h
    new_h = 500
    new_w = int(new_h * aspect_ratio)
    image = cv2.resize(image, (new_w, new_h))  # Resize while keeping aspect ratio
    cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    # Dynamically shift individual channels in the original RGB image
    shift_channel_dynamic(image, 2, 6)  # Shift R dynamically
    shift_channel_dynamic(image, 0, 6)  # Shift B dynamically
    shift_channel_dynamic(image, 1, 6)  # Shift G dynamically
    
    # Shift all channels dynamically
    shift_all_channels_dynamic(image, 6)
    
    # Create single channel images
    r_image = np.zeros_like(image)
    g_image = np.zeros_like(image)
    b_image = np.zeros_like(image)
    
    r_image[:, :, 2] = image[:, :, 2]  # Red channel
    g_image[:, :, 1] = image[:, :, 1]  # Green channel
    b_image[:, :, 0] = image[:, :, 0]  # Blue channel
    
    # Show each channel separately
    show_image("Video", r_image, 5)
    show_image("Video", g_image, 5)
    show_image("Video", b_image, 5)
    
    # Show original image
    show_image("Video", image, 5)
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "/home/troy/Downloads/Mona_Lisa.jpg"  # Change this to the path of your image
    main(image_path)