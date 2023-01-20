import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import re

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Open the file and read in the text
with open('C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/the-autobiography-of-nelson-mandela.txt', 'r', encoding="utf-8") as f:
    text = f.read()

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Initialize lists to store the prompts and completion pairs
prompts = []
pairs = []

#iterate through the sentences
for sentence in sentences:
    # check if the sentence contain personal information and remove if it does
    if re.search(r"\b(name|address|phone|email|birthdate)\b", sentence):
        continue
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    #lemmatize words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    #create a prompt by adding special marker to signal that the prompt is an question
    prompts.append("Q: "+" ".join(lemmatized_words) + " ")
    # generate the prompt-completion pairs
    pairs.append((prompts[-1], " ".join(words)))

# shuffle the pairs
import random
random.shuffle(pairs)

# use a fraction of the pairs for fine-tuning 
num_of_training_examples = int(len(pairs) * 0.8)

# split the pairs into training and validation sets
training_pairs = pairs[:num_of_training_examples]
validation_pairs = pairs[num_of_training_examples:]

# use the HuggingFace's transformers library to fine-tune a pre-trained GPT-2 model
import transformers

# load a pre-trained GPT-2 model
model = transformers.GPT2ForCausalLM.from_pretrained("gpt2")

# define the fine-tuning parameters
num_of_epochs = 3
batch_size = 2

# use the training pairs to fine-tune the model
training_args = {"overwrite_output_dir": True,
                 "num_train_epochs": num_of_epochs,
                 "per_device_train_batch_size": batch_size}
transformers.Trainer.from_argparse_args(training_args).train(model, training_pairs)

# evaluate the model on the validation set
from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# convert the validation pairs to input-target format
inputs, targets = zip(*validation_pairs)
encoded_inputs = tokenizer(inputs, return_tensors="pt", padding=True)
encoded_targets = tokenizer(targets, return_tensors="pt", padding=True)

# generate the model's outputs
outputs = model(**encoded_inputs)

# evaluate the performance using the GPT-2 loss
from transformers import GPT2Loss
loss = GPT2Loss()
evaluation_loss = loss(outputs[0], encoded_targets[0])
print(f"Evaluation loss: {evaluation_loss}")

# evaluate the performance using the perplexity metric
from transformers import GPT2ForCausalLM, GPT2Tokenizer
model = GPT2ForCausalLM.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
from transformers import TextGenerationPipeline
pipeline = TextGenerationPipeline(model=model, tokenizer=tokenizer)
perplexity = pipeline.evaluate_perplexity(validation_pairs)
print(f"Evaluation perplexity: {perplexity}")
