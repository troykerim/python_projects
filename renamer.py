import os
import shutil

def rename_images(input_folder, output_folder, start_count=1, prefix=""):
    """
    Rename all images from input_folder and copy them to output_folder.

    Parameters:
        input_folder (str): Path to the source images.
        output_folder (str): Path where renamed images will be saved.
        start_count (int): Starting number for renaming.
        prefix (str): Name prefix before the image number.
    """

    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get all image files sorted alphabetically
    valid_exts = (".jpg", ".jpeg", ".png")
    files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(valid_exts)])

    if not files:
        print("No image files found in input folder.")
        return

    print(f"Found {len(files)} images. Starting rename at count {start_count}.\n")

    counter = start_count

    for file in files:
        file_ext = os.path.splitext(file)[1]  # Keep original file extension
        new_name = f"{prefix}{counter:03d}{file_ext}" 
        src_path = os.path.join(input_folder, file)
        dst_path = os.path.join(output_folder, new_name)

        shutil.copy2(src_path, dst_path)  # copy while preserving metadata
        print(f"Copied: {file} → {new_name}")

        counter += 1

    print(f"\nAll files renamed and saved to: {output_folder}")


if __name__ == "__main__":
    
    input_dir = ""    
    output_dir = ""       
    start_count = 1               

    rename_images(input_dir, output_dir, start_count=start_count)