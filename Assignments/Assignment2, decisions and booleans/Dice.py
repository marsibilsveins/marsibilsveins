d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

# Fill in the missing code below

sum = d1 + d2

if (d1 <= 6) and (d2 <= 6)and (d1 > 0) and (d2 > 0):
    if(sum == 2):
        print("Snake eyes")
    elif(sum == 12):
        print("Dozen")
    else:
        print(sum)
else:
    print("Invalid input")