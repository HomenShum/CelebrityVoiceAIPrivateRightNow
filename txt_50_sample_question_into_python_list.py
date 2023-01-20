# Read the contents of the text file into a string
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/mandela_50_sample_questions.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split the text into lines
lines = text.split("\n")

# Initialize an empty list to store the questions
questions = []

# Iterate through the lines
for line in lines:
    # Add the line to the questions list
    questions.append(line[3:])

# Print the questions
print(questions)

# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/mandela_50_sample_questions_list.txt", "w", encoding="utf-8") as f:
    # Iterate over the elements in the questions list
    for item in questions:
        # Write each element to the text file, with a newline character after each one
        f.write(str(item) + "\n")

print("Done!")