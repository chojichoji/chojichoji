import string
with open("pride_and_prejudice.txt") as file:
    text=file.read()

text=text.lower()
# Clean data by removing capitalisation and punctuation marks
for punctuation_marks in string.punctuation:
    text=text.replace(punctuation_marks, " ")
# Split string into a list of strings containing all the words
words=text.split()
#print(words)
# Loop through list of words to populate dictionary
word_frequencies = {}
for word in words:
    if word not in word_frequencies.keys():
        word_frequencies[word] = 1
    else:
        word_frequencies[word] = word_frequencies[word] + 1
#print(word_frequencies)
print(len(word_frequencies))
file=open("Words in Pride n Prejudice.csv", "w")
file.write("Word, Frequency\n")
for word, frequency in word_frequencies.items():
    file.write(f"{word},{frequency}\n")
    
