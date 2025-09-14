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

```bash
pip install opencv-python pytesseract pandas matplotlib
