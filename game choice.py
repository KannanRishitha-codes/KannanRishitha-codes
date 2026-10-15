#Let's create a program to generate the favourite game
print("LET'S CREATE A MYSTERY GAME")
print('choose an option from 1-3')
print()
print()
choice= int(input('enter your choice:'))
if choice == 1:
    print("Let's play guess the number")
    print('hint is the number is between 90 to 100')
    num = 100
    for i in range(1,6):
        guess = int(input('enter a number:'))
        if guess == num:
            print('you won')
            break
        else:
            print('you lost')
elif choice == 2:
    print()
    print("Let's print a magic word from your name")
    print()
    import random
    name = input('Enter a name:')
    length =len(name) 
    num = list(name)
    magic =  "".join(random.choice(num) for _ in range(length))
    print()
    print(" THE MAGIC WORD IS :",magic)
elif choice == 3 :
    print(" LET'S CREATE SMILEY ")
    import time
    for i in range(1,6):
        if i%2!=0:
            print('  @  @  ')
            print('  ----  ')
            print()
            print()
            time.sleep(1)
        else:
            print('  @  @  ')
            print('   \/   ')
            print()
            print()
            time.sleep(1)
else:
    print(' PLEASE CHECK YOUR OPTION ')

    
