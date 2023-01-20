prompts = []

# Open the text file and read its contents
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

# Iterate through the lines of the file
for line in lines:
    # Modify the line into a question by adding a question mark at the end and capitalizing the first letter
    question = line.strip() + '?'
    question = question.capitalize()
    
    # Add the question to the prompts list
    prompts.append(question)

print(prompts)

# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_questions.txt", "w", encoding="utf-8") as f:
    # Write the prompts to the text file
    f.write(str(prompts))

print("Done!")