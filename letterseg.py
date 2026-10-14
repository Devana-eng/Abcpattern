for r in range(5):
    for c in range(4):
        if r==0 or r==4 or c==0 or c==3:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end="")


    for c in range(4):
        if r==0 or r==2 or r==4 or c==0:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end="")


    for c in range(6):
        if (r == c and r <= 2) or (r + c == 4 and r <= 2):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end="")




    for c in range(5):
        if r == 0 or r == 2 or c == 0 or c == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ", end="")


    
    for c in range(4):
        if c==0 or c==3 or r==c:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end="")


    
    for c in range(5):
        if r == 0 or r == 2 or c == 0 or c == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
