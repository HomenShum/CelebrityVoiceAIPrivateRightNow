# open the first file in read mode
with open(r'C:\Users\hshum\OneDrive\Desktop\Python\ChatGPT\oprah_nelson_mandela_PNP.txt', 'r', encoding='utf-8') as f:
    # read the contents of the file
    print("reading file1 content...")
    file1_contents = f.read()

# open the second file in read mode
with open(r'C:\Users\hshum\OneDrive\Desktop\Python\ChatGPT\king_nelson_mandela_PNP.txt', 'r', encoding='utf-8') as f:
    # read the contents of the file
    print("reading file2 content...")
    file2_contents = f.read()

# open the second file in read mode
with open(r'C:\Users\hshum\OneDrive\Desktop\Python\ChatGPT\mandela_autobiography_pcp.txt', 'r', encoding='utf-8') as f:
    # read the contents of the file
    print("reading file3 content...")
    file3_contents = f.read()

# concatenate the contents of the two files
result_contents = file1_contents + file2_contents

# open the result file in write mode
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/nelson_mandela_PCPs.txt', 'w', encoding='utf-8') as f:
    # write the concatenated contents to the file
    print("writing combined content to result file...")
    f.write(result_contents)

print("Done!")
