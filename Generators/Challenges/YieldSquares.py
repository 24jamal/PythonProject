def yield_squares(n):

    count =1
    while count < n:

        yield count**2
        count = count +1

for i in yield_squares(10):
    print(i)