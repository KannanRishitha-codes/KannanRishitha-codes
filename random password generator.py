import random
length = int(input('enter the length of the password:'))
sign=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','@','!','?','*','&','$']
password = "".join(random.choice(sign) for _ in range(length))
print(password)
