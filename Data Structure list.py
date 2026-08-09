#Data Structure(list - find most common words
words=['black','green','black','pink','black','white','black','python','white','black','orange','pink','pink','red','red','teal','orange','pink','black','pink','green','teal','teal','green','teal','white','orange','orange','red']
from collections import Counter
word_counts=Counter(words)
print(word_counts)
top_three=word_counts.most_common(3)
print(top_three)