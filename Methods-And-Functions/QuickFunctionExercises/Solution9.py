def myfunc(*args):

    out = []

    for num in args:
        if num %2 == 0:
            out.append(num)

    return out

print(myfunc(2,3,4,5,6))