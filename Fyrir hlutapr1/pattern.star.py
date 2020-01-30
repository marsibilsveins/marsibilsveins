star_int = int(input("Number of stars: "))

for i in range(0, star_int):
    for j in range(0, i+1):
        print("*", end=" ")
    print()