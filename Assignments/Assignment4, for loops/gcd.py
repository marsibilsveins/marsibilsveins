m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

gcd = 1

for i in range(1, m+1):
    if m%i == 0 and n%i == 0:
        gcd = i

print(gcd)


#for i in range (2,(n+1) and(m+1)): # getur verið 1 líka 1/1