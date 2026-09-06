def smiley():
    import time
    for i in range(1,19):
        if i%2==0:
            print("  ^ ^  ")
            print("  ---  ")
            print()
            print()
            time.sleep(1)
        else:
            print("  0 0 ")
            print("   o  ")
            print()
            print()
            time.sleep(1)
