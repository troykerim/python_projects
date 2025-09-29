import os

def labels_to_string(txt_path):
    with open(txt_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return "\\n".join(lines)

label_folder = r""   # folder with .txt label files
output_file = r""  # new file to store results

with open(output_file, "w", encoding="utf-8") as out_f:
    for filename in os.listdir(label_folder):
        if filename.endswith(".txt"):
            txt_path = os.path.join(label_folder, filename)
            label_str = labels_to_string(txt_path)    
            image_name = filename.replace(".txt", ".jng")
            out_f.write(f"[{image_name}] {label_str}\n")

print(f"Processed all .txt files in {label_folder}")
print(f"Results saved to {output_file}")