def filter_even(num):

    if num % 2 == 0:
        return True
    else:
        return False

    
nums = [1,2,3,4,5,6,7,8]

filters_evens = filter(filter_even,nums)
print(list(filters_evens))