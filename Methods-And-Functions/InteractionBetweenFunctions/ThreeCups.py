import random
def checkguess(mixedlist, guess):

    if (mixedlist[guess] == 'O'):
        print("Youre Correct")
    else:

        print("Youre not correct")
        print(mixedlist)

def shuffle_list(a):
    mylist = random.shuffle(a)
    return mylist

def playerguess():

    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Enter the number 1,2 or 3")
    
    return int(guess)


mylist = ['*','O',"*"]
random.shuffle(mylist)
print(type(mylist), mylist)
#guess = playerguess()
checkguess(mylist,playerguess())