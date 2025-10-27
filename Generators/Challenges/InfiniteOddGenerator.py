import itertools

def infiniteodd():

    count = 1

    while True:

        if (count %2 != 0):
            yield count
        count = count +2


mylist = list(itertools.islice(infiniteodd(), 5))
print(mylist)
# Output: [1, 3, 5, 7, 9]
