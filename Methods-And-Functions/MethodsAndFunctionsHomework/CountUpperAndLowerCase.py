def count_upperandlower(sentence):
    
    uppercount = 0
    lowercount = 0
    for i in range(len(sentence)):

        if sentence[i].isupper():
            uppercount = uppercount +1
        elif sentence[i].islower():
            lowercount = lowercount + 1
        else:
            pass
    print(f"UpperCount : {uppercount} || LowerCount : {lowercount}")
    return uppercount , lowercount

sentence= "Hello Mr. Rogers, how are you this fine Tuesday?"
count_upperandlower(sentence)




    


sentence = "Hello Mr. Rogers, how are you this fine Tuesday?"
