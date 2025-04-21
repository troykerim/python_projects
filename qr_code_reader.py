import sys
import cv2 
def decode_qr_code(file_path):
    image = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    if vertices_array is not None:
        print(f"URL: {data}")
        return data 
    else: 
        print("No QR code found.")
        return "" 
#if __name__ == "__main__":
 #   print("Usage: python3 qr_code_reader.py <file_path>")
#    sys.exit(1)
    
# file_path = sys.argv[1]
file_path = input("Enter path: ")
url = decode_qr_code(file_path)