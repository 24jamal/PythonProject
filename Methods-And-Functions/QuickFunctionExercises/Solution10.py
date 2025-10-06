def myfunc(string):

    out = []

    for i in range(len(string)):

        if i % 2 == 0:

            out.append(string[i].lower())

        else :
            out.append(string[i].upper())

    return ''.join(out)

print(myfunc("friends"))