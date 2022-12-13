from random import shuffle


def juggle(word):
    anagram = list(word)
    shuffle(anagram)
    return "".join(anagram)


words = ["mango", "pears", "orange", "banana"]
anagrams = []

##using for loop
for word in words:
    anagrams.append(juggle(word))
    print(anagrams)


## using map method
print(map((juggle, words)))


## using comprehension
print([juggle(word) for word in words])
