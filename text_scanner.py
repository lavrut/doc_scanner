name = input("Enter file name: ")

with open(name, 'r') as document:
    word_counts = {}
    for line in document:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

most_common_word = max(word_counts, key=word_counts.get)
most_common_word_count = word_counts[most_common_word]

print(f"The most common word in the document is '{most_common_word}'.")
print(f"It appears {most_common_word_count} times.")
