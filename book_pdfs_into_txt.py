from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import nltk

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        resource_manager = PDFResourceManager()
        string_io = StringIO()
        converter = TextConverter(resource_manager, string_io, laparams=LAParams())
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        for page in PDFPage.get_pages(f):
            page_interpreter.process_page(page)
        text = string_io.getvalue()
        converter.close()
        string_io.close()
        return text

# extract the text from the PDF file
text = extract_text_from_pdf(r'C:\Users\hshum\OneDrive\Desktop\Python\ChatGPT\the-autobiography-of-nelson-mandela.pdf')

# Split the text into sentences
sentences = nltk.sent_tokenize(text)

# Find the starting and ending sentences
start = "APART FROM LIFE, a strong constitution, and an abiding connection to the Thembu royal house, the only thing my father bestowed upon me at birth was a name, Rolihlahla."
end = "But I can rest only for a moment, for with freedom come responsibilities, and I dare not linger, for my long walk is not yet ended."
start_index = -1
end_index = -1

# Find the starting and ending indexes
for i, sentence in enumerate(sentences):
    if start in sentence:
        start_index = i
    if end in sentence:
        end_index = i
        break

# Extract the text between the starting and ending sentences
extracted_text = '\n'.join(sentences[start_index:end_index+1])

# print the extracted text
print(extracted_text)

# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/the-autobiography-of-nelson-mandela.txt", "w", encoding="utf-8") as f:
    # Write the extracted text to the text file
    f.write(extracted_text)

print("Done!")
