# Machine Learning on AWS – Exercises

This repository contains all practical exercises completed during the [Machine Learning on AWS](https://www.coursera.org/learn/machine-learning-on-aws/) course. Each exercise integrates AWS services using Python and the Boto3 SDK.

---

## AWS CLI Setup

```bash
# Install the AWS CLI (Windows)
winget install --id Amazon.AWSCLI

# Configure your credentials
aws configure
```

Provide your AWS Access Key, Secret Access Key, default region (e.g. `us-west-2`), and output format (e.g. `json`).

---

## Exercise 1: Amazon Rekognition – Image Label Detection

This application analyzes `.jpeg` images (located in `public/photos/`) using Amazon Rekognition and generates a `data.json` file (saved in `build/data.json`) used by a web interface to filter and display labels.

### Technologies

- AWS Rekognition
- Boto3 (AWS SDK for Python)
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

![Amazon Rekognition Web App](./assets/1.png)

---

## Exercise 2: Amazon Textract – Document Text Extraction

This application extracts structured text from handwritten forms using Amazon Textract and custom queries.

### Technologies

- AWS Textract
- Boto3 (Python SDK)
- Query-based document parsing
- CSV output

### How It Works

1. The script `main.py` scans all `.jpg` files in `raw_images/`.
2. It sends each image to Textract with two queries: `"What is the response id"` and `"What are the notes?"`.
3. The answers are extracted from `response["Blocks"]` and saved as rows.
4. The result is displayed in standard CSV format.

### Run Locally

```bash
# Execute the script
python main.py
```

### Preview

The screenshot below shows the terminal output, including extracted `ResponseId` and `Notes` fields from each handwritten review.

![Amazon Textract Output](./assets/2.png)

---

## Exercise 3: Amazon Comprehend – Sentiment Analysis

This application uses Amazon Comprehend to analyze the sentiment of each review in the `movies.csv` file generated in Exercise 2.

### Technologies

- AWS Comprehend
- Boto3 (AWS SDK for Python)
- Sentiment detection
- CSV parsing

### How It Works

1. The script `main.py` reads the `movies.csv` file.
2. It extracts the `Notes` column (the movie reviews).
3. It sends the list of reviews to `batch_detect_sentiment` from Amazon Comprehend.
4. The API returns a sentiment (e.g., POSITIVE, NEGATIVE) for each review.
5. The sentiment is displayed next to its corresponding review in the terminal.

### Run Locally

```bash
# Execute the script
python main.py
```

### Preview

The screenshot below shows the terminal output with sentiment detected for each review.

![Amazon Comprehend Output](./assets/3.png)

---

## Upcoming Exercises

- Exercise 4: Amazon Transcribe & Translate – Audio Processing  

(To be updated upon completion)

---

## Requirements

- Python 3.x  
- AWS CLI configured (`aws configure`)  
- AWS account
