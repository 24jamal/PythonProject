#Two lists: [1,2,3,4] and [5,6,7,8]

def multiply(a,b):

    multipliedlist = []
    for x, y in zip(a,b):

        num = x* y

        multipliedlist.append(num)

    return multipliedlist

def filterfunction(num):
        if num > 20:
            return True


a =[1,2,3,4]
b =[5,6,7,8]

multiplylist = multiply(a,b)
print(list(multiplylist))
filteredlist = filter(filterfunction, multiplylist)

print(list(filteredlist))