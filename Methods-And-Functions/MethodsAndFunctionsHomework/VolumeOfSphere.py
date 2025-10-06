def vol_of_sphere(r):

    vol = (4/3) * 3.14 * (r * r *r)
    return vol


print(vol_of_sphere(3))

def check_in_range(num):

    if (num >= 2 and num <= 7):

        print("Number is in range")
    else:
        print("Not in range")
    
check_in_range(2)