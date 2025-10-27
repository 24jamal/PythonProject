def reversethestring(s):

    i = len(s) - 1
    yield s[::-1]
    i = i-1

for i in reversethestring("jamal"):
    print(i)