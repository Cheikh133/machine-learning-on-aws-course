import glob
import boto3
import json
import csv
import sys

# Initialize an array to collect extracted values for each image
csv_array = []

# Create an Amazon Textract client
client = boto3.client('textract')

# Loop through all JPEG files in the 'raw_images' directory
for filename in glob.glob('raw_images/*.jpg'):
    csv_row = {}  # Dictionary to store extracted values for the current image

    print(f"Processing: {filename}")  # Display which file is being processed

    # Open the image file in binary mode
    with open(filename, 'rb') as fd:
        file_bytes = fd.read()

    # Call Amazon Textract's analyze_document API with custom queries
    response = client.analyze_document(
        Document={'Bytes': file_bytes},
        FeatureTypes=["QUERIES"],
        QueriesConfig={
            'Queries': [
                {'Text': 'What is the response id', 'Alias': 'ResponseId'},
                {'Text': 'What are the notes?', 'Alias': 'Notes'},
            ]
        }
    )

    # Loop through all blocks returned in the response
    for block in response["Blocks"]:
        # Look for blocks of type 'QUERY' (i.e., the query definitions)
        if block["BlockType"] == "QUERY":
            # Get the alias of the query (e.g., 'ResponseId' or 'Notes')
            query_alias = block["Query"]["Alias"]

            # Find the ID of the corresponding answer block
            answer_id = next(rel["Ids"] for rel in block["Relationships"] if rel['Type'] == "ANSWER")[0]

            # Retrieve the text of the answer block using its ID
            answer_text = next(b for b in response["Blocks"] if b["Id"] == answer_id)["Text"]

            # Store the answer text in the current CSV row under the query alias
            csv_row[query_alias] = answer_text

    # Append the filled CSV row to the output array
    csv_array.append(csv_row)

# Initialize a CSV writer that outputs to the console (stdout)
writer = csv.DictWriter(sys.stdout, fieldnames=["ResponseId", "Notes"], dialect='excel')

# Write the CSV header row
writer.writeheader()

# Write all extracted rows to the CSV output
for row in csv_array:
    writer.writerow(row)
