# open the first file in read mode
with open(r'C:\Users\hshum\OneDrive\Desktop\Python\ChatGPT\qna_data.txt', 'r', encoding='utf-8') as f:
    # read the contents of the file
    print("reading file1 content...")
    file1_contents = f.read()

# open the second file in read mode
with open(r'C:\Users\hshum\OneDrive\Desktop\Python\ChatGPT\VFMSFMprompts_GPT_questions.txt', 'r', encoding='utf-8') as f:
    # read the contents of the file
    print("reading file2 content...")
    file2_contents = f.read()

# concatenate the contents of the two files
result_contents = file1_contents + file2_contents

# open the result file in write mode
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/Joined_PCPs.txt', 'w', encoding='utf-8') as f:
    # write the concatenated contents to the file
    print("writing combined content to result file...")
    f.write(result_contents)

print("Done!")
