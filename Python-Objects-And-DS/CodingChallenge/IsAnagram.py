def isAnagram(str1 , str2):

    if len(str1) != len(str2):
        return False
    
    mydict1 = {}
    mydict2 = {}

    for ch in str1:

        mydict1[ch] = mydict1.get(ch, 0) + 1
    
    for ch in str2:

        mydict2[ch] = mydict2.get(ch, 0) + 1

    return mydict1 == mydict2

print(isAnagram("listen","silent"))
print(isAnagram("Hello","World"))
