import itertools

def infinitecyle(mylist):

    while True:

        for item in mylist:
            yield item
        
mylist = ['A','B','C','D']
print(list(itertools.islice(infinitecyle(mylist),7)))