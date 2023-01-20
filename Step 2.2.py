import openai

# Set up the OpenAI API client
openai.api_key = "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"

prompts = []

# Open the text file and read its contents
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_questions_filtered_2.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

# Iterate through the lines of the file
for line in lines:
    # Use the OpenAI API to generate a question from the line
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Convert the following sentence into a proper question: {line}",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Get the generated question from the API response
    question = response['choices'][0]['text']
    print(question)

    # Add the question to the prompts list
    prompts.append(f'"{question}",')

# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/VFMSFMprompts_GPT_questions.txt", "w", encoding="utf-8") as f:
    # Write the prompts to the text file in the format of a Python list
    f.write('prompts = [\n')
    for prompt in prompts:
        f.write(f'    {prompt}\n')
    f.write(']\n')

print("Done!")