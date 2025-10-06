def spy_game_007(arr):

    code = [0,0,7]

    for num in arr:

        if num == code[0]:
            code.pop(0)
        
        if not code:
            return True
    return False

a1 = [1,2,4,0,0,7,5]
a2 = [1,0,2,4,0,5,7]
a3 = [1,7,2,0,4,5,0]
print(spy_game_007(a1))
print(spy_game_007(a2))
print(spy_game_007(a3))