def look_rooms(room_choice_look):
    print()

    if room_choice_look == "treasury":  # Treasury
        print("\nYou are now looking in the secret Treasury Room. One of these objects will allow you to be the wealthiest pirate of the sea.")
        #TODO: display image of the room
        return
    elif room_choice_look == "captain":  # Captain
        print("\nYou are now looking at a beautiful Captain Cabin. One of these objects would allow you to be the most respected captain of the sea.")
        #TODO: display image of the room
        return
    elif room_choice_look == "sea":  # Sea
        print("\nYou are now facing the sea, the sky is blue, the weather is nice and you are hungry. You will need to start fishing soon.")
        #TODO: display image of the room
        return
    elif room_choice_look == "armory":  # Armory
        print("\nYou are now looking at a fully equipped armory room. One of these objects would allow you to be the strongest pirate of the sea.")
        #TODO: display image of the room
        return
    else:
        print("\nYou should try to start from the beginning!")
        return
    
def go_rooms(room_choice_go, inventory):
    room_object = ""
    
    if room_choice_go == "treasury":  # Treasury
        print("\nYou are now in the Treasury Room. Which of these valuable objects do you desire the most? These objects are displayed in front of you, you can choose only one: ")
        print("1. A Parrot")
        print("2. Gold Coins")
        print("3. A Treasury Map")
        print("4. A barrel Rum")

        room_object = input("Please enter the object you want to place in the inventory (no caps): ").lower().strip()
        if room_object == "a parrot":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a parrot")
        elif room_object == "gold coins":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("gold coins")
        elif room_object == "a treasury map":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a treasury map")
        elif room_object == "a barrel rum":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a barrel rum")
        else:
            print("Please type in the name of the object again.")

    elif room_choice_go == "captain":  # Captain
        print("\nYou are now in the Captain’s Cabin. Which object would allow you to be the most respected Captain? These objects are displayed in front of you, you can choose only one: ")
        print("1. A Candle")
        print("2. A Feather-pen")
        print("3. An Eye-Patch")
        print("4. A Princess ")

        room_object = input("Please enter the object you want to place in the inventory (no caps): ").lower().strip()
        if room_object == "a candle":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a candle")
        elif room_object == "a feather-pen":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a feather-pen")
        elif room_object == "an eye-patch":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("an eye-patch")
        elif room_object == "a princess":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a princess")
        else:
            print("Please type in the name of the object again.")

    elif room_choice_go == "sea":  # Sea
        print("\nYou are now in the Sea Room. You are hungry and you need to fish to survive. These objects are displayed in front of you, you can choose only one:")
        print("1. A fishing line")
        print("2. A net")
        print("3. A spear")
        print("4. A fish disguise")

        room_object = input("Please enter the object you want to place in the inventory (no caps): ").lower().strip()
        if room_object == "a fishing line":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a fishing line")
        elif room_object == "a net":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a net")
        elif room_object == "a spear":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a spear")
        elif room_object == "a fish disguise":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a fish disguise")
        else:
            print("Please type in the name of the object again.")

    elif room_choice_go == "armory":  # Armory
        print("\nYou are now in the Armory Room. Which object would be more valuable in a fight? These objects are displayed in front of you, you can choose only one:")
        print("1. A Sabre")
        print("2. A Gun")
        print("3. A Cannon")
        print("4. A Wand")

        room_object = input("Please enter the object you want to place in the inventory (no caps): ").lower().strip()
        if room_object == "a sabre":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a sabre")
        elif room_object == "a gun":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a gun")
        elif room_object == "a cannon":
            print(f"You have placed {room_object} in your inventory.")
            inventory.append("a cannon")
        elif room_object == "a wand":
            print(f"You have placed", room_object, "in your inventory.")
            inventory.append("a wand")
        else:
            print("Please type in the name of the object again.")
    else:
        print("There is something wrong here")
    return inventory

def object_score(inventory):
    score = 0
    for object_inventory in inventory:
        if object_inventory == "a parrot":  # treasury
            score = score + 1
        if object_inventory == "gold coins":
            score = score + 2
        if object_inventory == "a treasury map":
            score = score + 3
        if object_inventory == "a barrel rum":
            score = score + 0
        if object_inventory == "a candle":  # captain
            score = score + 1
        if object_inventory == "a feather-pen":
            score = score + 2
        if object_inventory == "an eye-patch":
            score = score + 3
        if object_inventory == "a princess":
            score = score + 0
        if object_inventory == "a fishing line":  # sea
            score = score + 1
        if object_inventory == "a net":
            score = score + 2
        if object_inventory == "a spear":
            score = score + 3
        if object_inventory == "a fish disguise":
            score = score + 0
        if object_inventory == "a sabre":  # armory
            score = score + 1
        if object_inventory == "a gun":
            score = score + 2
        if object_inventory == "a cannon":
            score = score + 3
        if object_inventory == "a wand":
            score = score + 0
    print(f"Your total score based on the objects in your inventory is: {score} !!!")
    

    
def main():
    inventory = []
    print("\nWelcome, your name is Jack Sparrow and you just found the BluePearl pirate ship.")
    print("Your mission is to explore the ship and retrieve the most valuable objects in each room to be the most respected pirate of the Sea. ")

    user_command = input("Do you want to 'Look' or 'Go'  to the next room?").lower().strip()

    inventory = []
    
    # TODO: while loop for enter to exit
    if user_command == "look":
        room_choice_look = input("Which room do you want to go to (type in the name in small caps): 'Treasury','Captain','Sea','Armory'?").lower().strip()
        look_rooms(room_choice_look)

    elif user_command == "go":
        room_choice_go = input("Which room do you want to go to (type in the name in small caps): 'Treasury','Captain','Sea','Armory'?").lower().strip()
        inventory = go_rooms(room_choice_go, inventory)
    else:
        print("We might need a more intelligent user for this game. ")

    object_score(inventory)


if __name__ == "__main__":
    main()