from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from moviepy.editor import VideoFileClip
import os

def split_video_by_scene(input_path, output_folder, threshold=27.0):
    os.makedirs(output_folder, exist_ok=True)

    # --- Scene detection phase ---
    video_manager = VideoManager([input_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))

    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list()
    video_manager.release()

    print(f"Detected {len(scene_list)} scenes.")
    for i, (start, end) in enumerate(scene_list):
        print(f"Scene {i+1}: Start={start.get_timecode()}, End={end.get_timecode()}")

    # --- Clip extraction phase ---
    video = VideoFileClip(input_path)
    for i, (start, end) in enumerate(scene_list):
        subclip = video.subclip(start.get_seconds(), end.get_seconds())
        output_path = os.path.join(output_folder, f"scene_{i+1:03d}.mov")
        subclip.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)
        print(f"Saved {output_path}")

    video.close()
    print("Scene-based splitting complete.")


if __name__ == "__main__":
    input_video = ""   
    output_dir = ""
    split_video_by_scene(input_video, output_dir, threshold=27.0)
