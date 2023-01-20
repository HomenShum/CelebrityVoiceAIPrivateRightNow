import openai

openai.api_key = "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"
model_engine = "text-davinci-002"

# Set the list of potential prompts
prompts = [
	"What is the significance of the title? Did you find it meaningful, why or why not?",
    "Would you have given the book a different title? If yes, what would your title be?",
    "What were the main themes of the book? How were those themes brought to life?",
    "What did you think of the writing style and content structure of the book?",
    "How important was the time period or the setting to the story? Did you think it was accurately portrayed?",
    "How would the book have played out differently in a different time period or setting?",
    "Which location in the book would you most like to visit and why?",
    "Were there any quotes (or passages) that stood out to you? Why?",
    "What did you like most about the book? What did you like the least?",
    "How did the book make you feel? What emotions did it evoke?",
    "Are there any books that you would compare this book to?",
    "Have you read any other books by this author? How would you compare them to this selection?",
    "What do you think the author’s goal was in writing this book? What ideas were they trying to illustrate? What message were they trying to send?",
    "What did you learn from this book?",
    "Did this book remind you of any other books that you’ve read? Describe the connection.",
    "Did your opinion of this book change as you read it? How?",
    "Would you recommend the book to a friend? How would you summarize the story if you were to recommend it?",
    "Was the book satisfying to read? Why or why not?",
    "If you could talk to the author, what burning question would you want to ask?",
    "Which character did you most relate to and why?",
    "Who was your favorite character? Why?",
    "Which character or moment prompted the strongest emotional reaction for you? Why?",
    "What motivates the actions of each of the characters in the book?",
    "Did the characters seem believable to you? Did they remind you of anyone you know?",
    "Were the characters clearly drawn and depicted?",
    "If the book were made into a movie, who would play each of the lead characters?",
    "What were the power dynamics between the characters and how did that affect their interactions?",
    "How does the way the characters see themselves differ from the way others see them?",
    "Were there times you disagreed with a character’s actions? What would you have done differently?",
    "Which character would you most like to meet in real life?",
    "What scene would you point out as the pivotal moment in the narrative? How did it make you feel?",
    "What scene resonated with you most on a personal level? (Why? How did it make you feel?)",
    "What surprised you most about the book? Why? Were there significant plot twists and turns? If so, what were they?",
    "Were there any plot twists that you loved? Hated?",
    "Did the author do a good job of organizing the plot and moving it along?",
    "What was your favorite chapter and why?",
    "What (if any) questions do you still have about the plot?",
    "How did you feel about the ending? How might you change it?",
	"How have the characters changed by the end of the book?",
	"What do you think will happen next to the main characters?",
	"Have any of your personal views changed because of this book? If so, how?",
	"At what point in the book did you have an idea what was going on? What was the key clue that gave it away?",
	"How did the author build the tension?",
	"Did the ending answer all your questions? Did you think it was believable or too farfetched?",
	"How honest do you think the author was?",
	"What aspects of the story could you most relate to?",
	"Why do you think the author chose to write their memoir?",
	"Were you rooting for the couple to get together all along? Why or why not?",
	"Did the plot make sense or were there some gaps/liberties taken to help get the couple together (or keep them apart)?",
	"What songs did you think of while reading this book?",
    "What is the significance of Viktor Frankl's experiences in the concentration camps for the main themes of the book?",
    "How does Viktor Frankl's concept of 'logotherapy' relate to his experiences in the concentration camps and the message he wants to convey in the book?",
    "What impact did Viktor Frankl's time in the concentration camps have on his personal philosophy and approach to life?",
    "What did you learn about Viktor Frankl's perspective on the human condition and the importance of meaning in life from reading the book?",
    "In what ways does Viktor Frankl's experience in the concentration camps challenge or reinforce your own beliefs about the human capacity for resilience and hope?",
    "What inspired Viktor Frankl to develop the concept of logotherapy?",
    "How did Viktor Frankl's experiences in the concentration camps influence his approach to psychology and therapy?",
    "What role did Viktor Frankl's personal beliefs and values play in his experiences in the concentration camps and his ability to survive and find meaning in those circumstances?",
    "What message do you think Viktor Frankl was trying to convey through his book about the human search for meaning and purpose in life?",
    "In what ways did Viktor Frankl's experiences in the concentration camps change his perspective on life and his own personal values?",
	"What can we learn from Viktor Frankl's experiences in the concentration camps about the role of meaning and purpose in overcoming adversity?",
    "How does Viktor Frankl's concept of logotherapy differ from other approaches to psychology and therapy?",
    "What do you think Viktor Frankl meant by the idea that 'everything can be taken from a man but one thing: the last of the human freedoms—to choose one's attitude in any given set of circumstances'?",
    "How does Viktor Frankl's concept of 'noogenic neurosis' relate to his experiences in the concentration camps and his approach to therapy?",
    "What can we learn from Viktor Frankl's experiences in the concentration camps about the importance of self-transcendence and finding meaning in life?",
    "What role did Viktor Frankl's personal values and beliefs play in his ability to survive and find meaning in the concentration camps?",
    "What can we learn from Viktor Frankl's experiences in the concentration camps about the role of suffering and adversity in human growth and development?",
    "What message does Viktor Frankl want to convey about the importance of meaning and purpose in life through his experiences in the concentration camps?",
    "How does Viktor Frankl's concept of 'existential frustration' relate to his experiences in the concentration camps and his approach to therapy?",
    "What can we learn from Viktor Frankl's experiences in the concentration camps about the role of personal responsibility and choice in finding meaning in life?",
    "How does Viktor Frankl's concept of 'the will to meaning' relate to his experiences in the concentration camps and his approach to therapy?",
    "What can we learn from Viktor Frankl's experiences in the concentration camps about the importance of finding meaning and purpose in life, even in the most difficult circumstances?",
    "What message does Viktor Frankl want to convey about the human capacity for resilience and hope through his experiences in the concentration camps?",
    "What can we learn from Viktor Frankl's experiences in the concentration camps about the role of personal values and beliefs in finding meaning in life?",
    "How does Viktor Frankl's concept of 'the meaning of life' relate to his experiences in the concentration camps and his approach to therapy?",
    "What can we learn from Viktor Frankl's experiences in the concentration camps about the importance of self-transcendence and finding meaning beyond oneself?",
    "What message does Viktor Frankl want to convey aboutthe human search for meaning and purpose in life through his experiences in the concentration camps?",
	"What can we learn from Viktor Frankl's experiences in the concentration camps about the role of suffering and adversity in finding meaning and purpose in life?",
	"How does Viktor Frankl's concept of 'the search for meaning' relate to his experiences in the concentration camps and his approach to therapy?",
	"What message does Viktor Frankl want to convey about the human capacity to find meaning and purpose in life through his experiences in the concentration camps?",
	"What can we learn from Viktor Frankl's experiences in the concentration camps about the role of personal values and beliefs in overcoming adversity?",
	"How does Viktor Frankl's concept of 'the human quest for meaning' relate to his experiences in the concentration camps and his approach to therapy?",
	"What message does Viktor Frankl want to convey about the importance of finding meaning and purpose in life through his experiences in the concentration camps?",
]

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
        n=3,
        stop=None,
        temperature=0.5,
    )

    # Loop over the completions
    for choice in completions.choices:
        # Get the completion text
        completion = choice.text

        # Add the prompt-completion pair to the list
        pairs.append((prompt, completion))

# Create a list of dictionaries in the required format
data = [{"prompt": prompt, "completion": completion} for prompt, completion in pairs]

# Open the text file for writing
print("Writing to text file...")
with open("C:/Users/hshum/OneDrive/Desktop/Python/ChatGPT/qna_data.txt", "w", encoding="utf-8") as f:
    # Iterate over the elements in the list
    for item in data:
        # Write each element to the text file, with a newline character after each one
        f.write(str(item) + "\n")

print("Done!")