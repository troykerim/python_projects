import os
import shutil

# Define fixed paths
INPUT_PATH = "/home/troy/internvl-nrp-proj/dataset"
OUTPUT_PATH = "/home/troy/internvl-nrp-proj/test_images"

def move_files():
    subfolders = ["images", "labels"]

    for subfolder in subfolders:
        src_folder = os.path.join(INPUT_PATH, subfolder)
        dst_folder = os.path.join(OUTPUT_PATH, subfolder)
        os.makedirs(dst_folder, exist_ok=True)

        # List and sort files in each subfolder
        files = sorted([f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))])

        # Take the last 20 files
        last_20_files = files[-20:]

        # Move each file
        for file in last_20_files:
            src = os.path.join(src_folder, file)
            dst = os.path.join(dst_folder, file)
            shutil.move(src, dst)

        print(f"Moved last 20 files from '{src_folder}' to '{dst_folder}'")

    print("\nDone! Last 20 .jpg and .txt files were moved into test_images/ and removed from dataset/.")


if __name__ == "__main__":
    move_files()
