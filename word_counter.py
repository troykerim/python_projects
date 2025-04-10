from collections import Counter 

s = input("Enter a sentence: ")
words = s.lower().split()

word_count = Counter(words)

most_common_word, highest_count = word_count.most_common(1)[0]

print(f"The most frequent word is '{most_common_word}' appearing {highest_count} times.")

'''
# Alternative way of displaying the words that appear most frequent. 

highest_count = max(word_count.values())
most_common_word = [word for word, count in word_count.items() if count == highest_count]

print(f"Tte most frequent words(s): {', '.join(most_common_word)} appearing {highest_count} times.")
'''

