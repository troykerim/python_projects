import os
import cv2

def get_video_duration_seconds(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    cap.release()

    if fps <= 0:
        raise RuntimeError(f"Invalid FPS for video: {video_path}")

    return frame_count / fps


def total_mp4_duration(folder_path):
    total_seconds = 0
    video_files = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".mp4"):
                video_files += 1
                video_path = os.path.join(root, file)
                duration = get_video_duration_seconds(video_path)
                total_seconds += duration

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return video_files, hours, minutes, seconds


if __name__ == "__main__":
    folder_path = ""

    count, h, m, s = total_mp4_duration(folder_path)

    print(f"Number of .mp4 files: {count} for this path {folder_path}")
    print(f"Total duration of all files is: {h} hours, {m} minutes, {s} seconds")
