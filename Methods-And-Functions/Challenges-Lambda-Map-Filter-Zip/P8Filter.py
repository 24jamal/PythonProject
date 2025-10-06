def passing_marks(marks):

    if marks >= 40:
        return True

    else:
        return False
    

marklist = [35, 45, 60, 20, 50,40]
filtered_list = filter(passing_marks,marklist)

print(list(filtered_list))