age_int = int(input("Enter your age: "))

if 0 <= age_int <= 34:
    print("Young")
elif 35 <= age_int <= 50:
    print("Mature")
elif 51 <= age_int <= 69:
    print("Middle-aged")
elif 70<= age_int:
    print("Old")
else:
    print("Invalid age")