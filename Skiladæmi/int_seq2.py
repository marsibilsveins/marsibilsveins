num_int = int(input("Enter an integer: "))
even_num = 0
odd_num = 0
largest_num = 0
cum_total = 0

while num_int > 0:
    # keyrir á meðan inputtið er stærra en 0 
    cum_total += num_int
    print("Cumulative total: {}".format(cum_total))
    # finnur stærsta inputtið
    if num_int > largest_num:
        largest_num = num_int
    # finnur hvort að input-ið sé slétttala eða oddatala og bætir við summu hvers fyrir sig
    if num_int % 2 == 0:
        even_num += num_int
    else:
        odd_num += num_int
    
    num_int = int(input("Enter an integer: "))
# ef stærsta talan er stærri en 0 þá prentast stærsta slegin tala, summan af sléttum og oddatölum
if largest_num > 0:
    print("Largest number: {}".format(largest_num))
    print("Sum of even numbers: {}".format(even_num))
    print("Sum of odd numbers: {}".format(odd_num))
