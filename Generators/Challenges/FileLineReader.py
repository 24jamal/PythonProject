def filereader(filename):

    with open(filename, 'r') as file:

        for line in file:
            yield line


for i in filereader("Generators/Challenges/Sample.txt"):
    print(i)