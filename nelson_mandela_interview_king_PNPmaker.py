# Read the contents of the text file into a string
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/king_nelson_mandela.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split the text into lines
lines = text.split("\n")
# Initialize an empty list to store the prompt-completion pairs
prompt_completion_pairs = []

# Initialize variables to store the current prompt and completion
prompt = ""
completion = ""

# Iterate through the lines
for line in lines:
    # Check if the line is a prompt
    if line.startswith("KING: ") and ("?" in line):
        # Set the current prompt to the line
        prompt = line[6:]
    # Check if the line is a completion
    if line.startswith("MANDELA: "):
        # Set the current completion to the line
        completion = line[9:]
        # Check if the prompt is empty
        if prompt == "":
            # Add the completion to the previous prompt-completion pair
            prompt_completion_pairs[-1]["completion"] += " " + completion
        else:
            # Add a new prompt-completion pair to the list
            prompt_completion_pairs.append({
                "prompt": prompt,
                "completion": completion
            })
            # Reset the prompt and completion variables
            prompt = ""
            completion = ""


# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/king_nelson_mandela_PNP.txt", "w", encoding="utf-8") as f:
    # Iterate over the elements in the prompt_completion_pairs list
    for item in prompt_completion_pairs:
        # Write each element to the text file, with a newline character after each one
        f.write(str(item) + "\n")

print("Done!")
