dictionary = {"Barby": ["Plastic", 120, 50], "Car": ["Metal, Plastic", 110, 100], "Lego": ["Plastic", 2000, 20]}
total_price = 0
a = 1
while True:
    print("1. View description")
    print("2. View price")
    print("3. View count")
    print("4. All information")
    print("5. Purchase")
    print("6. End program")

    choice = int(input("Select menu item: "))

    if choice == 1:
        for key, value in dictionary.items():
            print(key, ":", value[0])
    elif choice == 2:
        for key, value in dictionary.items():
            print(key, ":", value[1])
    elif choice == 3:
        for key, value in dictionary.items():
            print(key, ":", value[2])
    elif choice == 4:
        for key, value in dictionary.items():
            print(key, ":", value[0], ";", value[1], ";", value[2])
    elif choice == 5:
        while True:
            print("1. Purchase a toy")
            print("2. Close")

            choice_1 = int(input("Select a menu item: "))

            if choice_1 == 1:
                toy = input("Enter a toy: ")
                if (toy in dictionary.keys()) == 0:
                    print("Wrong input!")
                else:
                    amount = int(input("Enter a count: "))
                    for key, value in dictionary.items():
                        if key == toy and value[2] > amount > 0:
                            value[2] -= amount
                            all_price = amount * value[1]
                            total_price += all_price
                            print(key, ":", value[0], ";", value[1], ";", value[2])
                            print("Total cost: ", total_price)
                            a = 1
                            break
                        else:
                            a = 0

                    if a == 0:
                        print("Wrong input!")
            elif choice_1 == 2:
                break
            else:
                print("Wrong input!!!")
    elif choice == 6:
        print("Good luck!!!")
        break
    else:
        print("Wrong input!!!")
