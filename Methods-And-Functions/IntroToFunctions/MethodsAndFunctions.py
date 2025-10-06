# Function → Independent block of reusable code (len(), print(), def ...)

# Method → Function tied to an object, called with dot notation (list.append(), str.upper())

#Function Example

def greeting(name):

    print(f"hello {name}")
    return "jolly"

print(greeting("Jamal"))


#Methods Example

word = "rise"

Capital = word.capitalize()
Allcaps = word.upper()
print(Capital,Allcaps)


