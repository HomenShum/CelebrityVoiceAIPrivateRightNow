import openai

# Set up the GPT-3 language model
openai.api_key = "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"
model_engine = "text-davinci-003"

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

# Read in the transcript of an interview with Nelson Mandela
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/the-autobiography-of-nelson-mandela.txt', 'r', encoding='utf-8') as f:
    transcript = f.read()

# Split the transcript into lines
t_lines = transcript.split("\n")

# Initialize a list to store the prompt-completion pairs
prompt_completion_pairs = []

# Iterate through the questions
print("Generating completions for prompts...")
for question in questions:
    # Generate completions for the prompt
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=f"{t_lines} {question}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.2,
    )    

    # Loop over the completions
    for choice in completions.choices:
        # Get the completion text
        completion = choice.text

        # Add the prompt-completion pair to the list
        prompt_completion_pairs.append((prompt, completion))

# Create a list of dictionaries in the required format
data = [{"prompt": prompt, "completion": completion} for prompt, completion in pairs]

# Print the list of prompt-completion pairs
print(data)
# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/mandela_PCP.txt", "w", encoding="utf-8") as f:
    # Iterate over the elements in the list
    for item in data:
        # Write each element to the text file, with a newline character after each one
        f.write(str(item) + "\n")

print("Done!")