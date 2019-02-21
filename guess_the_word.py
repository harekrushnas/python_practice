
import random

f=open('word_list.txt','r')
f1=open('word_list.txt','r')

cnt=0
cnt_1=0

for i in f:
    cnt=cnt+1
ran = random.randint(1,cnt)


for i in f1:
    cnt_1=cnt_1+1

    if ran==cnt_1+1:
        word=i
        break



#print(word)
lnth=len(word)-1
#guess_word=[]
guess_word=''
org_word=''
for i in range(lnth):
    if i%2==0:
        guess_word += word[i]
        #guess_word+=word[i]+'_'
    else:
        guess_word +='_'


for i in range(lnth):
    org_word+=word[i]



#print(guess_word)

print('Hi... Friend.. Welcome to the Word guess game....')
print('Lets Begine.....Best of luck...')
print('Hints: \n The Word length is: ',lnth,'\n The word structure is :',guess_word)
print('You have 3 chances to guess...')
#print(word)

for i in range(3):
    user_word = input('PLEASE ENTER YOUR WORD :')

    if org_word == user_word:
        print('Congrats....your guess is correct....')
        break
    else:
        if i == 2:

            print(' Ohh...U missed all the chances....','\n You Lose the game',
                  '\n thanks for playing the game... ')

            chk_word=input('Do you want to see the Actual Word ? Y/N :')
            if chk_word=='Y' or chk_word=='y':
                print ('The actual word is : ',org_word)
            else:
                print('Thank u...')

        else:
            #print('Ohhh....Your guess is incorrect.......don\'t worry you have ',Fore.RED + 2-i +Style.RESET_ALL , 'chance left')
            print('Ohhh....Your guess is incorrect.......don\'t worry you have ', 2 - i ,'chance left')



