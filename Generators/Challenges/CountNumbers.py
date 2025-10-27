def count_numbers(n):

    count = 1

    while count < n:

        yield count

        count = count +1

for i in count_numbers(10):

    print(i)