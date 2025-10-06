def product(num):

    return num[0] * num[1]

def filterfunc(num):

    if num > 20:
        return True

a =[1,2,3,4]
b =[5,6,7,8]

zipped = zip(a,b)
products = map(product,zipped)
filtered = filter(filterfunc, products)

print(list(filtered))