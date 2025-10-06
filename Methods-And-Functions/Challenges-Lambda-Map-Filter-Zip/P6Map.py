#[10, 20, 30] and [5, 25, 15]


#op : [5, 5, 15]

def abs_values(a,b):

    print(a,b)
    return abs(a-b)

one = [10, 20, 30]
two = [5, 25, 15]
combined = map(abs_values,one, two)
print(list(combined))