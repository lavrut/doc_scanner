name = input('Enter file: ')
document = open(name, 'r')
counts = dict()

for line in document:
    words = line.split()
    for word in words:
      counts[word] = counts.get(word, 0) + 1
            
word_freq= None
common_word = None
for word, count in list(counts.items()):
    if word_freq is None or count > word_freq:
        common_word = word
        word_freq = count
        
print("The most common word in the document is:", common_word + ".")
print("The word occurs", word_freq, "times.")


