import nltk
from nltk.tokenize import word_tokenize

# Open the text file and read its contents
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_questions_filtered.txt', 'r', encoding="utf-8") as f:
    contents = f.read()

# Split the contents into a list of lines
lines = contents.split('\n')

# List to store the filtered lines
filtered_lines = []

# Iterate through the lines
for line in lines:
    # Split the line into a list of words
    words = word_tokenize(line)
    
    # Check the number of words in the line
    if len(words) < 10:
        # If the line has fewer than 4 words, skip it
        continue
    
    # Add the line to the list of filtered lines
    filtered_lines.append(line)

# Open the text file for writing
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_questions_filtered_2.txt', 'w', encoding="utf-8") as f:
    # Write the filtered lines to the text file
    for line in filtered_lines:
        f.write(line + '\n')
