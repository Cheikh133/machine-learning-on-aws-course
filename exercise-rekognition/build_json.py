import glob
import boto3
import json

# Initialize the Amazon Rekognition client using default AWS credentials and region
client = boto3.client('rekognition')

# This list will store the results for each image
combined = []

# Loop through all JPEG files in the public/photos directory
for filename in glob.glob('public/photos/*.jpeg'):
    # Open the image file in binary mode
    with open(filename, 'rb') as fd:
        # Call Rekognition's detect_labels API to get labels for the image
        response = client.detect_labels(Image={'Bytes': fd.read()})
        
        # Prepare a dictionary entry for this image
        entry = {
            "Filename": filename.replace("public/", "")  # Clean the file path
        }

        # Directly assign the labels returned by Rekognition to the entry
        entry["Labels"] = response["Labels"]

        # Add the entry to the combined list
        combined.append(entry)

# Output the combined data in pretty-printed JSON format
print(json.dumps(combined, indent=2))

