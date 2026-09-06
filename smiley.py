def smiley():
    import time
    for i in range(1,19):
        if i%2==0:
            print("  $ $  ")
            print("   o   ")
            print()
            print()
            time.sleep(1)
        else:
            print("  * *  ")
            print("   #  ")
            print()
            print()
            time.sleep(1)
