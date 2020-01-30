value = int(input("First: "))
step = int(input("Second: "))

the_sum = 0
max_sum = 100

while the_sum < max_sum:
    print(value, end=" ")
    the_sum += value
    value += step

print()
print("Sum of series:", the_sum)