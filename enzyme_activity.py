import cv2
import pytesseract
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Path to Tesseract executable (update if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Video file and interval
video_file = "spec.mp4"
interval_sec = 5  # capture every 5 seconds

# Open video
cap = cv2.VideoCapture(video_file)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration_sec = frame_count / fps

print(f"Video FPS: {fps}, Total frames: {frame_count}, Duration: {duration_sec:.2f}s")

data = []
current_time = 0

while current_time < duration_sec:
    frame_no = int(current_time * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert frame to grayscale for OCR
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # OCR
    text = pytesseract.image_to_string(gray)
    
    # Search for absorbance value after "Abs"
    absorbance = None
    for line in text.splitlines():
        if "Abs" in line:
            match = re.search(r'(\d\.\d{1,3})', line)
            if match:
                absorbance = float(match.group(1))
                break
    
    if absorbance is not None:
        data.append({
            "time_min": round(current_time / 60, 3),
            "Abs": absorbance
        })
        print(f"Time: {current_time}s ({current_time/60:.3f}min), Abs: {absorbance}")
    else:
        print(f"Time: {current_time}s ({current_time/60:.3f}min), Abs: Not found")
    
    current_time += interval_sec

cap.release()

# Save to Excel
df = pd.DataFrame(data)
xlsx_file = "absorbance_data.xlsx"
df.to_excel(xlsx_file, index=False)
print(f"Data saved to {xlsx_file}")

# Plot Abs vs Time
plt.figure(figsize=(8,5))
plt.plot(df["time_min"], df["Abs"], marker='o', linestyle='-')
plt.xlabel("Time (min)")
plt.ylabel("Absorbance")
plt.title("Absorbance vs Time")
plt.grid(True)
plt.tight_layout()
plt.show()

# Open Excel file automatically
os.startfile(xlsx_file)
