'''from PIL import Image
import numpy as np

# Load image and convert to grayscale (just to be sure)
img = Image.open('/home/troy/Pictures/Screenshots/lena_gray.bmp').convert('L')
img_array = np.array(img)

# Open a file to write
with open('/home/troy/Documents/myfile4fpgaproj.txt', 'w') as f:
    for r in range(img_array.shape[1]):  # Corresponds to MATLAB's 1:512 (columns)
        for c in range(img_array.shape[0]):  # Corresponds to MATLAB's 1:512 (rows)
            f.write(f"{img_array[c, r]},")'''
            
            
# Create imageData.h from a flat text file of grayscale pixel values

input_file = "/home/troy/Downloads/imageData.h"
output_file = "/home/troy/vga_vipin_1/software/vga_vipin1/src/imageData.h"

with open(input_file, "r") as f:
    numbers = f.read().strip().split(",")

# Clean and convert to integers
numbers = [int(n.strip()) for n in numbers if n.strip().isdigit()]

with open(output_file, "w") as f:
    f.write("const unsigned char imageData[] = {\n")
    for i in range(0, len(numbers), 16):  # Group 16 values per line for readability
        line = ", ".join(map(str, numbers[i:i+16]))
        f.write(f"    {line},\n")
    f.write("};\n")
