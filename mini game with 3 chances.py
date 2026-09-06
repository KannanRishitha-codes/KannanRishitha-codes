secret_num = 777
print('WELCOME TO GUESSING THE NUMBER GAME')
print('HITNT:It is a three digit number bw 770 and 780')
for chance in range(3):
    guess = int(input('enter a number:'))
    if guess == secret_num:
        print('BRAVO!!! its right')
        break
    else:
        print('oops!! its wrong')
print('your chance is over')
