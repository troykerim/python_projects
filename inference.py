#!/usr/bin/env python3
# Inference script for InternVL2.5-4B QLoRA fine-tuned model (Pascal VOC single-image demo)

import os
import torch
from transformers import AutoProcessor, AutoModel
from PIL import Image
import matplotlib.pyplot as plt
import re
import argparse

# -------------------------
# Default configuration
# -------------------------
MODEL_PATH = "/workspace/output"
IMAGE_DIR = "/workspace/test_data/test_images/images"
LABEL_DIR = "/workspace/test_data/test_images/labels"
PROMPT = (
    "Detect and label waste items in the image. "
    "Output format: 'class xmin ymin xmax ymax' (Pascal VOC format)."
)

# -------------------------
# CLI argument (optional)
# -------------------------
parser = argparse.ArgumentParser(description="InternVL2.5-4B QLoRA inference (single image)")
parser.add_argument("--image", type=str, default=None,
                    help="Specify image filename (e.g., image_001.jpg). "
                         "If not provided, uses the first file in IMAGE_DIR.")
args = parser.parse_args()

# -------------------------
# Select test image & label
# -------------------------
img_files = sorted([f for f in os.listdir(IMAGE_DIR)
                    if f.lower().endswith((".jpg", ".jpeg", ".png"))])
if not img_files:
    raise FileNotFoundError(f"No images found in {IMAGE_DIR}")

# Use parameter or default to first image
img_name = args.image if args.image else img_files[0]
img_path = os.path.join(IMAGE_DIR, img_name)

label_path = os.path.join(
    LABEL_DIR, os.path.splitext(img_name)[0] + ".txt"
)

print(f"[Init] Using image: {img_path}")
if os.path.exists(label_path):
    print(f"[Init] Found label file: {label_path}")
else:
    print("[Init] No matching label file found (continuing without it).")

# -------------------------
# Device setup
# -------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[Init] Device: {device}")

# -------------------------
# Load model & processor
# -------------------------
print(f"[Load] Loading fine-tuned model from {MODEL_PATH}")
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).to(device)
processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)
model.eval()
print("[Load] Model ready for inference.")

# -------------------------
# Pascal VOC regex (class xmin ymin xmax ymax)
# -------------------------
bbox_pattern = re.compile(r"(\w+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)")

# -------------------------
# Load image and preprocess
# -------------------------
image = Image.open(img_path).convert("RGB")
inputs = processor(text=PROMPT, images=image, return_tensors="pt").to(device)

# -------------------------
# Inference
# -------------------------
with torch.no_grad():
    if hasattr(model, "generate"):
        outputs = model.generate(**inputs, max_new_tokens=150)
        generated_text = processor.decode(outputs[0], skip_special_tokens=True)
    elif hasattr(model, "chat"):
        generated_text = model.chat(processor, PROMPT, image)
    else:
        raise RuntimeError("Model does not support generate() or chat()")

print(f"\n[Model Output]\n{generated_text}")

# -------------------------
# Parse Pascal VOC bounding boxes
# -------------------------
boxes = []
for match in bbox_pattern.findall(generated_text):
    label, xmin, ymin, xmax, ymax = match
    boxes.append((label, int(xmin), int(ymin), int(xmax), int(ymax)))

# -------------------------
# Visualization
# -------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(image)
for (label, xmin, ymin, xmax, ymax) in boxes:
    width, height = xmax - xmin, ymax - ymin
    rect = plt.Rectangle((xmin, ymin), width, height,
                         fill=False, color="red", linewidth=2)
    ax.add_patch(rect)
    ax.text(xmin, max(ymin - 5, 10), label,
            color="yellow", fontsize=10, weight="bold")
ax.axis("off")
plt.title(f"Predictions for {img_name}")
plt.show()
