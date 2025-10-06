# Sum of Pairs

# Two lists: [1,2,3] and [4,5,6]

# Use zip() to create a list of sums of corresponding elements


a = [1,2,3] 
b = [4,5,6]

mylist = [x+y for x,y in zip(a,b)]

def pairtotal(a,b):

    combined = zip(a,b)
    pairtotallist = []

    for x,y in combined:

        num = x+y
        pairtotallist.append(num)

    print(list(pairtotallist))

print(mylist)
pairtotal([1,2,3],[4,5,6])