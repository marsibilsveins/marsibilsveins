can_int = int(input("Enter of cans: "))

pack_int = 6
box_int = pack_int * 4


if (can_int % box_int == 0):
    if (pack_int%box_int == 0):
        if(can_int%can_int == 0):
            print("{0} boxe(s), {0} packs, and {0} cans".format(can_int))
        else:
            print("False")
 
  

