# Automatic Enzyme Activity Measurement Tool

This Python script automatically extracts absorbance values from a **spectrophotometer video** recorded using a phone camera, generates a `.xlsx` table, and plots **Absorbance vs Time**.

---

## Features

- Converts a video into frames at regular intervals (default: every 5 seconds).  
- Uses **OCR (Tesseract)** to detect the `"Abs"` text and extract the absorbance value (up to 3 decimals).  
- Calculates the time in **minutes** based on video duration.  
- Saves the data into `absorbance_data.xlsx` in the same folder as the script.  
- Automatically plots **Abs vs Time**.  
- Opens the Excel file automatically after processing.

---

## Requirements

- Python 3.x  
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to your system PATH.  
- Python packages:
  - `opencv-python`
  - `pytesseract`
  - `pandas`
  - `matplotlib`

Install Python packages via pip:

```
pip install opencv-python pytesseract pandas matplotlib
```

---

## How to Use

1. **Download the script** from:

[enzyme_activity.py](https://github.com/j-unayed/Automatic-Enzyme-Activity-Measurement-Tool/releases/download/enzyme_activity/enzyme_activity.py)

2. **Place your video** (e.g., `spec.mp4`) in the same folder as the script.

3. **Run the script**:

```
python enzyme_activity.py
```

4. The script will:
   - Process the video every 5 seconds.  
   - Extract absorbance values dynamically from each frame using OCR.  
   - Save the results in `absorbance_data.xlsx`.  
   - Plot **Absorbance vs Time**.  
   - Automatically open the Excel file.

---

## Notes

- The script works best if the video shows `"Abs"` and its value clearly.  
- Camera movement is supported, but ensure `"Abs"` is visible in most frames.  
- Adjust the frame interval in the script by changing:

```
interval_sec = 5
```

to record more or fewer data points.

---

## Example Output

| time_min | Abs   |
|----------|-------|
| 0.000    | 0.652 |
| 0.083    | 0.659 |
| 0.167    | 0.661 |
| ...      | ...   |

The generated plot will show **Absorbance vs Time (minutes)**.

---

## License

This tool is provided **as-is** under [MIT License](LICENSE) and is free to use for research and educational purposes.
