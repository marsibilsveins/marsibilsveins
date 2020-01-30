top_num = int(input("Upper number for the range: ")) # Do not change this line

for num in range(2,top_num+1):
    sum_of_divisiors = 0
    for divisior in range(1, num):
        if num % divisior == 0:
            sum_of_divisiors += divisior
    if num == sum_of_divisiors:
        print(num)

#líka í assignment4 2019 dæmi 6 önnur lausn