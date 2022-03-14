def calculate_street(street):
    print("Divie: ", street/2)
    print("Modulus: ", street % 2 == 0)
    if (street % 2) == 0:
        print("Eastbound")
    else:
        print("Westbound")

calculate_street(11)