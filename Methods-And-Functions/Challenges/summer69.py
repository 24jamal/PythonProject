def summer69(nums):

    total = 0
    inSkip = False

    for num in nums:
        if inSkip:

            if (num == 9):
                inSkip = False
            continue
            
        if num == 6:
            inSkip = True
            continue

        total = total + num

    return total






arr = [2,3,4,5]
a1 = [1, 3, 5]
a2 = [4, 5, 6, 7, 8, 9]
a3 = [2, 1, 6, 9, 11]

print(summer69(arr))
print(summer69(a1))
print(summer69(a2))
print(summer69(a3))