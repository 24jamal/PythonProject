#Names: ['A', 'B', 'C'], Marks: [55, 35, 80]

def filterfunc(marks):

    if marks[1] >= 40:
        return True

def mapfunc(filtered):

    if (100 >filtered >= 80):
        return 'A'
    elif(79 > filtered >= 60):
        return 'B'
    elif(59 > filtered >= 40):
        return 'C'
    else:
        return 'F'

names =['A', 'B', 'C']
marks = [55, 35, 80]

zipped = zip(names, marks)

filtered = filter(filterfunc, zipped)

maplist = map(lambda x : (x[0] , mapfunc(x[1])), filtered)

print(list(maplist))

