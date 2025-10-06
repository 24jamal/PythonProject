def check_pangram(sentence):

    cleaned = sentence.replace(" ","").lower()
    print(f"cleanded is :: {cleaned}")
    alphas = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for ch in cleaned:
        if ch in alphas:
            count = count +1
    
    if count >= 26:
        print("pangram")
    else:
        print("Not pangram")

check_pangram("google")
check_pangram("The quick brown fox jumps over the lazy dog")