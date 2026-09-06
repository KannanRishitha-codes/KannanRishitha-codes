import random
sign = ['rock','paper','scissor']
computer_choice = random.choice(sign)
guess = input('enter a choice among[rock,paper,scissor]):')
if guess == computer_choice:
    print('IT IS A DRAW')
elif guess == 'rock':
    if computer_choice == 'paper':
        print('OOPS YOU LOSE')
    else:
        print('WOW YOU WON!!!')
elif guess == 'scissor':
    if computer_choice == 'paper':
        print('WOW YOU WON!!!')
    else:
        print('OOPS YOU LOSE')
elif guess == 'paper':
    if computer_choice=='rock':
        print('WOW YOU WON!!!')
    else:
        print('OOPS YOU LOSE')
else:
    print('PLEASE CHECK YOUR SPELLING')
