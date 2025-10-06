def blackjack(a,b,c):



    if (a ==11 or b==11 or c == 11):

        if (((a+b+c) -10) >21): 
            return "BUST"
        else:
            return (a+b+c) -10

    elif ((a+b+c) <21):
        return (a+b+c)
    
    elif ((a+b+c) > 21):

        return "BUST"
        
            

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

