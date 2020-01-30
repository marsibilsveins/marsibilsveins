a_str = input("Enter value for A: ") # Do not change this line
b_str = input("Enter value for B: ") # Do not change this line

a_int = int(a_str)
b_int = int(b_str)

# Fill in the missing code below
if a_int == 0 and b_int == 0:
    s_bool = 0
    c_bool = 0

elif a_int == 1 and b_int == 0:
    s_bool = 1
    c_bool = 0

elif a_int == 0 and b_int == 1:
    s_bool = 1
    c_bool = 0

else:
    s_bool = 0
    c_bool = 1

print('S={}, C={}'.format(s_bool, c_bool)) # Do not change this line