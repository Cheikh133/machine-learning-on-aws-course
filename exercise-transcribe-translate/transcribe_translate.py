import json
import re
import boto3
from random import choice

re_sentence = """(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"""

with open("transcribe.json") as file:
    transcribe = json.load(file)

# build array of start times
times = [item["start_time"] for item in transcribe["results"]["items"] if "start_time" in item]

translate = boto3.client('translate')
transcript = transcribe["results"]["transcripts"][0]["transcript"]
sentences = re.split(re_sentence, transcript)
word_ptr = 0
translated_arr = []

for sentence in sentences:
    #####
    # Replace this code and implement the code to translate from Brazilian Portuguese (pt-BR) to a supported language.
    #####
    # Traduction automatique du texte depuis le portugais brésilien vers l’anglais
    response = translate.translate_text(
        Text=sentence,
        SourceLanguageCode='pt',
        TargetLanguageCode='en'
    )
    translated_text = response['TranslatedText']


    translated_arr.append({ "start_time" : times[word_ptr], "translated" : translated_text})
    word_count = len(re.findall(r'\w+', sentence))
    word_ptr += word_count

print(json.dumps(translated_arr, indent=2))