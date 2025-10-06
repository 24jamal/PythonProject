def vowel_letters(sentence):

    vowels_list = []


    for i in range(len(sentence)):

        if sentence[i] in ['a','e','i','o','u','A','E','I','O','U']:

            letter = sentence[i]
            vowels_list.append(letter)

    return vowels_list
    
sentence = "Programming is fun"

print(vowel_letters(sentence))
