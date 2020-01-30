cm_str = input("Input cm: ") # do not change this line

cm_int = int(cm_str)

inch = round(cm_int / 2.54)
inches = inch % 12
feets = (inch // 12) % 3
yards = (inches // 12) // 3

print(yards, "yd. ", feets, 'ft.', inches, 'in.') # do not change this line


cm_str = input("Input cm: ") # do not change this line

cm_str_int = int(cm_str)

inch = round(cm_str_int / 2.54)
inches = inch % 12
feets = (inch // 12) % 3
yards = (inch // 12) // 3

print(yards, "yd. ", feets, 'ft.', inches, 'in.') # do not change this line