num = int(input("Input a number: "))
counter = 0         # fyrsta tala er 0

while counter < num:
    print(counter, end= " ")
    counter += 1
    if counter == 5:
        break
else:
    print("Done")

