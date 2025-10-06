names = ['Kane','Justin','Michael']

scores = [70,87,55]

for name, score in zip(names, scores):

    print(f"{name} scored {score}")


combined = zip(names,scores)
mylist = list(combined)

print(mylist)

#Once we interate the iterate iterable like zip it will get exhausted , so we need to convert the zip object to list using list function
for i,n in mylist:
    print(i, n)

