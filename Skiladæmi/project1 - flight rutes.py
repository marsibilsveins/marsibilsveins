flight_altitude_str = input("Input flight altitude (ft): ")
flight_altitude_int = int(flight_altitude_str)
airspace_class_str = input("Input airspace class: ")
visability_int = int(input("Input visibility (km): "))
horizontal_int = int(input("Input horizontal cloud separation (ft): "))
vertical_int = int(input("Input vertical cloud separation (ft): "))


if (flight_altitude_int < 0 or visability_int < 0 or horizontal_int < 0 or vertical_int < 0 or (airspace_class_str != "A" and airspace_class_str != "B" and airspace_class_str != "C" and airspace_class_str != "D" and airspace_class_str != "E" and airspace_class_str != "F" and airspace_class_str != "G")):
    print("Invalid input")

else:
    vfr_bool = False

    if flight_altitude_int >= 10000:
        if airspace_class_str == "B" or airspace_class_str == "C" or airspace_class_str == "D" or airspace_class_str == "E" or airspace_class_str == "F" or airspace_class_str == "G":
            if visability_int >= 8:
                if horizontal_int >= 1500:
                    if vertical_int >= 1000:
                        vfr_bool = True


    elif flight_altitude_int < 100000 or flight_altitude_int > 3000:
        if airspace_class_str == "B" or airspace_class_str == "C" or airspace_class_str == "D" or airspace_class_str == "E" or airspace_class_str == "F" or airspace_class_str == "G":
            if visability_int >= 5:
                if horizontal_int >= 1500:
                    if vertical_int >= 1000:
                        vfr_bool = True
                

    elif flight_altitude_int <= 30000:
        if airspace_class_str == "B" or airspace_class_str == "C" or airspace_class_str == "D" or airspace_class_str == "E":
            if visability_int >= 5:
                if horizontal_int >= 1500:
                    if vertical_int >= 1000:
                        vfr_bool = True

        elif airspace_class_str == "F" or air_class_str == "G":
            if visability_int >= 5:
                vfr_bool = True

    if vfr_bool:
        print("Visual Flight Rules")
    else:
        print("Instrument Flight Rules")