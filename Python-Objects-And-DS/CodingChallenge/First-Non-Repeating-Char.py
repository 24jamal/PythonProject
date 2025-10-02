def first_non_repeating_char(str1):

    freq = {}

    for ch in str1:

        if ch in freq:
            freq[ch] += 1

        else:
            freq[ch] =1
    
    for ch in str1:

        if freq[ch] ==1:
            return ch

print(first_non_repeating_char("HelloH"))