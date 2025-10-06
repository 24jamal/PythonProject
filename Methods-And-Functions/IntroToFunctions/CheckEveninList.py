def check_even_in_list(mylist):

    for a in mylist:

        if a %2 == 0:
            return True
    
    return False

a = [1,5,3,1]
print(check_even_in_list(a))