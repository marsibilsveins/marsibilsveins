#from fractions import Fraction

num_float = float(input("Input a decimal: ")) # Do not change this line

counter = 1
fraction_found = False

while counter <= 100: 
    if num_float  == (1/counter):
        fraction_found = True
        break
    counter += 1

if fraction_found:
    print("The fraction is 1/{}.".format(counter))
else:
    print("Fraction not found!")