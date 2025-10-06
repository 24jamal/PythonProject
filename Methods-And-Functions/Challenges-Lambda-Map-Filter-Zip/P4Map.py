def celcius_to_fahr(temp):

    return (temp * 1.8) + 32

mytemps = map(celcius_to_fahr,[23,40,18,45])

print(list(mytemps))

