import openai
import os

openai.api_key = "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"
model_engine = "text-curie-001"

# Set the path to the text file containing the prompts
prompts_file = "C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_GPT_questions.txt"

# Read the prompts from the text file
with open(prompts_file, "r") as f:
    prompts = f.read().splitlines()

# Create an empty list to store the prompt-completion pairs
pairs = []

# Loop over the prompts
print("Generating completions for prompts...")
for prompt in prompts:
    # Generate completions for the prompt
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3,
    )

    # Loop over the completions
    for choice in completions.choices:
        # Get the completion text
        completion = choice.text
        print(completion)

        # Add the prompt-completion pair to the list
        pairs.append((prompt, completion))

# Create a list of dictionaries in the required format
data = [{"prompt": prompt, "completion": completion} for prompt, completion in pairs]

# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_GPT_PCP.txt", "w", encoding="utf-8") as f:
    # Iterate over the elements in the list
    for item in data:
        # Write each element to the text file, with a newline character after each one
        f.write(str(item) + "\n")

print("Done!")