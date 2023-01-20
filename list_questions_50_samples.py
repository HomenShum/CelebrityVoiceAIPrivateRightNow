# Read in the text file containing the questions
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/mandela_50_sample_questions.txt', 'r') as f:
    text = f.read()

# Split the text by newline characters to get a list of individual questions
questions = text.split('\n')

# Remove any empty strings from the list of questions
questions = [q for q in questions if q]

# Print the list of questions
print(questions)
