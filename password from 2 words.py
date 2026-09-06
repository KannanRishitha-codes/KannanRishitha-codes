#LET'S CREATE A PASSWORD BY THE LETTERS WE GET FROM MERGING TWO WORDS:
import random
str1 = input('enter a word:')
str2 = input('enter a word:')
length = int(input('enter the length of the password :'))
word = str1+ str2
new = list(word)
password = "".join(random.choice(new) for _ in range(length))
print('The new password generated from the two words : ',password)
