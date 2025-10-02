a = "An apple a day keeps doctor away"

mylist = a.split()
print(mylist)

b = [x for x in mylist if len(x) %2 == 0 ]

c = ["even!" if len(x) %2 == 0 else "odd!" for x in mylist]
print(c)


