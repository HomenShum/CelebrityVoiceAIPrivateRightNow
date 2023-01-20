import nltk
import re
from nltk.tokenize import sent_tokenize

# Open the text file and read its contents
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_questions.txt', 'r', encoding="utf-8") as f:
    contents = f.read()

# Split the contents into a list of sentences
sentences = sent_tokenize(contents)

# List to store the filtered sentences
filtered_sentences = []

# Iterate through the sentences
for sentence in sentences:
    # Count the number of spaces in the sentence
    num_spaces = len(re.findall(r'\s', sentence))
    
    # Check the number of spaces in the sentence
    if num_spaces < 3:
        # If the sentence has fewer than 3 spaces, skip it
        continue
    # Add the sentence to the list of filtered sentences
    filtered_sentences.append(sentence)

# Open the text file for writing
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_questions_filtered.txt', 'w', encoding="utf-8") as f:
    # Write the sentences to the text file
    for sentence in sentences:
        f.write(sentence + '\n')
