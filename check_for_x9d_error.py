# Open the text file for reading
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/Joined_PCPs.txt", "r", encoding="utf-8") as f:
    # Try to read the contents of the file
    try:
        contents = f.read()
        print("Reading the text file...")
    # Catch the UnicodeDecodeError exception
    except UnicodeDecodeError:
        print("There was an error while reading the text file.")
