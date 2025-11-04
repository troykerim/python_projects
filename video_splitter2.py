import cv2
import os

def extract_frames_from_videos(input_folder, output_folder, interval_seconds=1, expected_width=1920, expected_height=1080):
    """
    Extract 1 frame per second from each .mp4 or .mov video in input_folder.
    Save all frames into a single output_folder with unique filenames.
    Displays and checks each video's resolution.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Collect all video files in the input folder
    valid_exts = (".mp4", ".mov")
    video_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(valid_exts)])

    if not video_files:
        print("No video clips found in input folder.")
        return

    print(f"Found {len(video_files)} video clips in {input_folder}\n")

    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        print(f"Processing: {video_file}")

        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            print(f"  Could not open {video_file}. Skipping.")
            continue

        # --- Get video properties ---
        fps = video.get(cv2.CAP_PROP_FPS)
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps if fps > 0 else 0
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_interval = int(fps * interval_seconds)

        print(f"  FPS: {fps:.2f}, Duration: {duration:.2f}s, Resolution: {width}x{height}")

        # --- Sanity check for resolution ---
        if width != expected_width or height != expected_height:
            print(f"  WARNING: Resolution mismatch! Expected {expected_width}x{expected_height}")
            print(f"  Skipping {video_file} to prevent inconsistent image sizes.\n")
            video.release()
            continue

        frame_idx = 0
        saved_count = 0
        base_name = os.path.splitext(video_file)[0]

        while True:
            ret, frame = video.read()
            if not ret:
                break

            # Save one frame every N frames
            if frame_idx % frame_interval == 0:
                image_name = f"{base_name}_frame_{saved_count+1:03d}.jpg"
                image_path = os.path.join(output_folder, image_name)
                cv2.imwrite(image_path, frame)
                print(f"    Saved: {image_name}")
                saved_count += 1

            frame_idx += 1

        video.release()
        print(f"  Extracted {saved_count} frames from {video_file}\n")

    print(f"Done. All extracted frames saved in: {output_folder}")


if __name__ == "__main__":
    input_dir = "" 
    output_dir = ""             
    extract_frames_from_videos(input_dir, output_dir, interval_seconds=1, expected_width=1920, expected_height=1080)
