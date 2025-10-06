# map()
# Apply function to each item
# Transformed items
# map(str.upper, names)


# Function which add 18% GST to products which maps the products proces in iterable like list and tuple

def addgst(num):
    return num+ num * 0.18

productsprices = [700,1000,300,500]

pricesaftergst = map(addgst,productsprices)

print(pricesaftergst)

pricelist = list(pricesaftergst)

print(pricelist)
