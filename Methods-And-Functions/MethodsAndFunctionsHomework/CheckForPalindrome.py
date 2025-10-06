def check_for_palindrome(sentence):

    palindrome = ""
    cleaned = sentence.replace(' ',"").lower()
    print(f"cleaned {cleaned}")
    for ch in cleaned:

        palindrome = ch + palindrome
    
    print(f"{cleaned} :: {palindrome}")
    return cleaned == palindrome

print(check_for_palindrome("malayalam"))

print(check_for_palindrome("Hello"))
print(check_for_palindrome("nurses run"))