# Display the multiplication Table
# The following program displays the multiplication table (from 1 to 10) according to the user input.

num = int(input("Show the multiplication table of? "))  
# using for loop to iterate multiplication 10 times   
for i in range(1,11):  
   print(num,'x',i,'=',num*i)  

# print("%d X %d = %d"%(num,i,num*i)); 
