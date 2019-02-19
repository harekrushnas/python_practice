#The program will first randomly generate a number unknown to the user. The user needs to guess what that number is.
# Reference link : https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
import random
#from colorama import*


ran = random.randint(0,1000)
#len1=len(str(abs(ran)))
#print(ran,len1)
below_ran=random.randint(ran-5,ran)
above_ran=random.randint(ran,ran+5)
#print(ran)

print('Guess the number is in range of : ',below_ran,' and ',above_ran)
print('Provied your number below line and you have 3 chances in your hand ')

print('--------------------------------------------------------------------')


for i in range(3):
    user_number = input(('PLEASE ENTER YOUR NUMBER :'))
    #print (i)
    if ran == int(user_number):
        print('Congrats....your guess is correct....NUMBER=', ran)
        break
    else:
        if i == 2:
            print('Ohh...U missed all the chances....thanks for playing the game... ')
        else:
            #print('Ohhh....Your guess is incorrect.......don\'t worry you have ',Fore.RED + 2-i +Style.RESET_ALL , 'chance left')
            print('Ohhh....Your guess is incorrect.......don\'t worry you have ', 2 - i ,'chance left')











