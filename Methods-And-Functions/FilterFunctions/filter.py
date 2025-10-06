# filter()
# Keep only items that meet condition
# Filtered items
# filter(lambda x: x>0, nums)

def filterexpensiveprices(price):

    #which True or False then only filter() function in python works
    return price > 1000

productsprices = [1200,200,300,20000,400,50]

expensiveitems = filter(filterexpensiveprices,productsprices)
listexpensiveitems = list(expensiveitems)
print(listexpensiveitems)

#Problem2 

#Finding speed cars in Dict 

def fast_cars(item):

    return item[1] > 300

cars = {"Mercedes-AMG": 360,"Toyota": 380 ,"Ford Fiesta" : 200, "Porsche" : 320}

speedcars = filter(fast_cars, cars.items())

mylist = list(speedcars)

print(mylist)

print(list(zip(mylist)))