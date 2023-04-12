"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""
text = input("Text: ")
sorted_text = sorted(text.split(" "))
count_occurrences = {word: sorted_text.count(word) for word in sorted_text}
for word in count_occurrences:
    print(word, ":", count_occurrences[word])
