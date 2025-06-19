# Machine Learning on AWS – Exercises

This repository contains all practical exercises completed during the [Machine Learning on AWS](https://www.coursera.org/learn/machine-learning-on-aws/) course. Each exercise integrates AWS services using Python and the Boto3 SDK.

---

## Exercise 1: Amazon Rekognition – Image Label Detection

This application analyzes `.jpeg` images (located in `public/photos/`) using Amazon Rekognition and generates a `data.json` file (saved in `build/data.json`) used by a web interface to filter and display labels.

### Technologies

- AWS Rekognition
- Boto3 (Python SDK)
- JSON processing
- Local HTTP server

### How It Works

1. The script `build_json.py` scans the `public/photos/` directory for JPEG images.
2. Each image is sent to Amazon Rekognition using `detect_labels`.
3. Detected labels and confidence scores are saved to `build/data.json`.
4. A local web interface (`build/index.html`) loads the JSON and displays images with their labels.

### Run Locally

```bash
# Install dependencies
pip install boto3

# Generate data.json using Rekognition
python build_json.py > build/data.json

# Launch local web server
python -m http.server 8080 -d build
```

Then open `http://localhost:8080` in your browser.

### Preview

The screenshot below shows the application running locally. On the left, images from `public/photos/` are displayed. When hovering over an image, the detected labels (returned by Amazon Rekognition) appear on the right panel.

![Amazon Rekognition Web App](./assets/exercise1_screenshot.png)

---

## Upcoming Exercises

- Exercise 2: Amazon Textract – Document Text Extraction  
- Exercise 3: Amazon Transcribe & Translate – Audio Processing  

(To be updated upon completion)

---

## Requirements

- Python 3.x  
- AWS CLI configured (`aws configure`)  

