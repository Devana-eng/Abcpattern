#A
for r in range(5):
    for c in range(5):
        if r == 0 or r == 2 or c == 0 or c == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#B

for r in range(5):
    for c in range(4):
        if r==0 or r==2 or r==4 or c==0 or c==3:
            print("*", end="")
        else:
            print(" ", end="")
    print()



#C
for r in range(4):
    for c in range(4):
        if r==0 or r==3 or c==0:
            print("*", end="")
        else:
            print(" ", end="")
    print()


#D
for r in range(5):
    for c in range(4):
        if r==0 or r==4 or c==0 or c==3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#E
for r in range(5):
    for c in range(4):
        if r==0 or r==2 or r==4 or c==0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#F
for r in range(5):
    for c in range(4):
        if r==0 or r==2 or c==0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#G
for r in range(4):
    for c in range(4):
        if r == 0 or r == 3:
            print("*", end="")
        elif c == 0 :
            print("*", end="")
        elif r==2 and c>=2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


#H
for r in range(5):
    for c in range(4):
        if r==2 or c==0 or c==3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# I

for r in range(4):
    for c in range(5):
        if r==0 or r==3 or c==2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# J
for r in range(4):
    for c in range(5):
        if r==0 or c==2 or (r==3 and c<2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# K
for r in range(5):
    for c in range(4):
        if c==0 or r+c==3 or r-c==1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#L

for r in range(4):
    for c in range(4):
        if r==3 or c==0:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# M

for r in range(5):
    for c in range(5):
        if c == 0 or c == 4 or (r == c and r <= 2) or (r + c == 4 and r <= 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#N

for r in range(4):
    for c in range(4):
        if c==0 or c==3 or r==c:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#o

for r in range(4):
    for c in range(4):
        if r==0 or r==3 or c==0 or c==3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#P

for r in range(5):
    for c in range(4):
        if r==0 or r==2 or c==0 or (r<=2 and c==3):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#Q

for r in range(5):
    for c in range(6):
        if r == 0 and c < 4 or r == 4 and c < 4:
            print("*", end="")
        elif c == 0 or c == 3:
            print("*", end="")
        elif r == 4 and c == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#R

for r in range(5):
    for c in range(4):
        if r==0 or r==2 or c==0 or (r<=2 and c==3) or r-c==1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#S
for r in range(5):
    for c in range(4):
        if r==0 or r==2 or r==4 or (r==1 and c==0) or (r==3 and c==3):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#T
for r in range(4):
    for c in range(5):
        if r==0 or c==2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#U

for r in range(4):
    for c in range(4):
        if r==3 or c==0 or c==3:
            print("*", end="")
        else:
            print(" ", end="")
    print()


#V
for r in range(4):
    for c in range(7):
        if r==c or r+c==6:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#W
for r in range(4):
    for c in range(5):
        if c==0 or c==4 or (r==2 and c==1) or (r==1 and c==2) or (r==2 and c==3):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#x

for r in range(4):
    for c in range(5):
        if r==c or r+c==3:
            print("*", end="")
        else:
            print(" ", end="")
    print()


#Y


for r in range(5):
    for c in range(5):
        if (r == c and r <= 2) or (r + c == 4 and r <= 2) or (r >= 2 and c == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#Z

for r in range(4):
    for c in range(4):
        if r==0 or r==3 or r+c == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

