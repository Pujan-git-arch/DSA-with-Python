# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8

word_count = {}
with open("poem.txt","r") as f:
    for line in f:
        words = line.split() # [[This will split the line into words and return a list of words.]]
        for word in words:
            word = word.strip(",.?!;:\"()") # [[This will remove any punctuation from the word.]]
            word = word.lower() # [[This will convert the word to lowercase.]]
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

for word, count in word_count.items():  # [[This will iterate through the dictionary and print the word and its count.]] # count is used here to store the count of the word and word is used to store the word itself. # items() method is used to get the key-value pairs from the dictionary.
    print(f"'{word}': {count}") 
    
print("Data structure used: Dictionary") # [[This is the best data structure for this problem because it allows us to store key-value pairs where the key is the word and the value is the count of that word. It also allows us to easily update the count of a word if it already exists in the dictionary.]]

