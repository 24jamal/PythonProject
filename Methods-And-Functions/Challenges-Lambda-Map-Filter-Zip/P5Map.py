def length_of_words(word):

    return len(word)

words = ["Earth", "Sun","Moon"]

combined = map(length_of_words, words)

print(list(combined))

