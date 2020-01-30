num = int(input("Input a number: "))

count = 1

while count <= num:
    if num%count == 0:
        print(count)
    count += 1
