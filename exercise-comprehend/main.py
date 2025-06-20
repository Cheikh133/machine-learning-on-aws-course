import boto3
import csv

# Read the 'movies.csv' file and extract the "Notes" field from each row
# We manually specify the column names: 'ResponseId' and 'Notes'
with open("movies.csv", 'r') as fd:
    reader = csv.DictReader(fd, fieldnames=["ResponseId", "Notes"], dialect='excel')
    
    # Build a list of all notes (movie reviews) to be analyzed
    all_notes = [row["Notes"] for row in reader]

# Initialize the Amazon Comprehend client
client = boto3.client('comprehend')

# Call the batch_detect_sentiment API with all movie notes
# This API analyzes the sentiment of each text in the list
response = client.batch_detect_sentiment(
    TextList=all_notes,
    LanguageCode='en'  # Required language code (English in this case)
)

# Loop through each result in the response
for result in response["ResultList"]:
    index = result["Index"]  # Index of the text in the original list
    sentiment = result["Sentiment"]  # Detected sentiment (e.g., POSITIVE, NEGATIVE)

    # Print the sentiment and the corresponding movie review
    print(sentiment, all_notes[index])
