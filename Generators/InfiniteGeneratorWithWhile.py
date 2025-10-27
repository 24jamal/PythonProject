def infinite_counter():
    count = 1
    while True:
        yield count
        count += 1

infinite_counter()

for i in infinite_counter():
    print(i)