def reversetheString(s):

    i = len(s) - 1
    while i >= 0:

        yield s[i]
        i = i-1

for i in reversetheString("Hello"):
    print(i)