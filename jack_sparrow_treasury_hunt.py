def look_rooms(room_choice_look):
    print()

    if room_choice_look == "treasury":  # Treasury
        print("\nYou are now looking in the secret Treasury Room. One of these objects will allow you to be the wealthiest pirate of the sea.")
        #TODO: display image of the room (without the ghost <- this is a surpise)
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
    
    if room_choice_go == "captain":  # Captain
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
            print("You typed the object wrong and did not take any of the objects.")
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
            print("You typed the object wrong and did not take any of the objects.")
            
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
            print("You typed the object wrong and did not take any of the objects.")
    else:
        print("There is something wrong here")
    print("!!! SOMETHING HAPPENS!!!!")
    print("You feel something touching your back! A ghost hand drags you through the door, it locks immediately and you now stand in front of the locked door. Shivering!")
    print("!!!!")
    return inventory

def go_east(position):
    position[1] += 1
    return position

def go_west(position):
    position[1] -= 1
    return position

def go_north(position):
    position[0] += 1
    return position

def go_south(position):
    position[0] -= 1
    return position

def go_in_treasury_room(inventory):
    print("You enter the treasury room and suddenly you stand face to face with a ghost pirate.")
    print("The door closes behind you and locks.")
    print('"ARR, Aren`t you Jack Sparrow? You came on board the wrong boat to plunder! Nobody ever got my treasure!"')
    print("\n")
    print("The ghost pirate does not hesitate long and attacks you with his sabre.")
    print("You evade the first hit.")
    
    useless_fighting_items = ["a spear", "a sabre", "a gun", "a cannon"]
    for inventar_object in inventory:
        if inventar_object in useless_fighting_items:
            inventar_object = inventar_object.replace("a ", "")
            print(f"You quickly go through your inventory and find the {inventar_object}.")
            print("You try to attack the ghost with your weapon, but to your surprise you can not hurt the ghost.")
            
    print("You go through the whole inventory again.")
    ghost_is_dead = False
    for inventar_object in inventory:
        if inventar_object == "a wand":
            print("You figured, that the wand you picked started to glow in blue.")
            print("You take it out of your inventory and poke the ghost...")
            print("\n")
            print('"Nooooooooo!!! You found the magic wand! The only weapon that can defeat me!"')
            print("\n")
            print("The ghost disappears.")
            ghost_is_dead = True
            
    if ghost_is_dead == True:
        print("Since the ghost disappears you now have finally access to the whole treasury room. But since you can not carry a lot, you need to decide for one specific treasure.")
        print("Choose wisely, what do you take?")
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
            print("You did not take any object from the treasury room, since you typed the object wrongly.")
        print("\n")
        print("You successfully plundered the BluePearl pirate ship. You can finally leave the ship. Let's see how good you performed...")
    else:
        print("The ghost attacks you again. But since you are focussed on your inventory, you can not evade the attack.")
        print("The attack does not miss its target.")
        print("\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!YOU DIED!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!GAME OVER!!!!!!!!!!!!!!!")
        print("\n")
        print("\n")
        print("Since you died, you loose all the objects in your inventory. I bet you can imagine how many points you get for your inventory...")
        inventory = []
    return inventory

def do_action(action_name, position, sea_closed, captains_closed, armory_closed, inventory, game_over):
    if action_name == "go north":
        position = go_north(position)
    elif action_name == "go south":
        position = go_south(position)
    elif action_name == "go west":
        position = go_west(position)
    elif action_name == "go east":
        position = go_east(position)
        
    # Sea room
    elif action_name == "go into the sea room":
        print("You enter the sea room")
        sea_closed = True
        inventory = go_rooms("sea", inventory)
    elif action_name == "look into the sea room":
        print("You look into the sea room")
        look_rooms("sea")
        
    # Armory room
    elif action_name == "go into the armory room":
        print("You enter the armory room")
        armory_closed = True
        inventory = go_rooms("armory", inventory)
    elif action_name == "look into the armory room":
        print("You look into the armory room")
        look_rooms("armory")
        
    # Captains room
    elif action_name == "go into the captains room":
        print("You enter the captains room")
        captains_closed = True
        inventory = go_rooms("captain", inventory)
    elif action_name == "look into the captains room":
        print("You look into the captains room")
        look_rooms("captain")
        
    # Treasury room
    elif action_name == "go into the treasury room":
        print("You enter the treasury room")
        inventory = go_in_treasury_room(inventory)
        game_over = True
    elif action_name == "look into the treasury room":
        look_rooms("treasury")
        
    elif action_name == "leave the ship":
        print("You are done with exploring the ship.")
        print("The game is over. Let's see how many points you get for your inventory...")
        game_over = True
    else:
        print("Your entry was incorrect, please choose an action again")
    return position, sea_closed, captains_closed, armory_closed, inventory, game_over

def possible_actions(position, sea_closed, captains_closed, armory_closed, inventory, game_over):
    if position == [0,0]:
        print("""Possible Actions: 
                Go east\n
                Leave the ship""")
    elif position == [0,1]:
        print("""Possible Actions: \n
              Go north\n
              Go west\n
              Go south""")
    elif position == [1,1]:
        print("""Possible Actions: \n
              Go east\n
              Go south""")
    # Sea room
    elif position == [1,2] and sea_closed == False:
        print("""Possible Actions: \n
              Look into the sea room\n
              Go into the sea room\n
              Go east\n
              Go west""")
    elif position == [1,2] and sea_closed == True:
        print("""Possible Actions: \n
              Go east\n
              Go west""")
    elif position == [1,3]:
        print("""Possible Actions: \n
              Go east\n
              Go west\n
              Go south""")
    elif position == [1,4]:
        print("""Possible Actions: \n
              Go west""")
    elif position == [0,3] and armory_closed == False:
        print("""Possible Actions: \n
              Look into the armory room\n
              Go into the armory room\n
              Go north""")
    elif position == [0,3] and armory_closed == True:
        print("""Possible Actions: \n
              Go north""")
    elif position == [-1,1]:
        print("""Possible Actions: \n
              Go east\n
              Go north""")
    elif position == [-1,2]:
        print("""Possible Actions: \n
              Go south\n
              Go west""")
    elif position == [-2,2] and captains_closed == False:
        print("""Possible Actions: \n
              Look into the captains room\n
              Go into the captains room\n
              Go north\n
              Go east""")
    elif position == [-2,2] and captains_closed == True:
        print("""Possible Actions: \n
              Go north\n
              Go east""")
    elif position == [-2,3]:
        print("""Possible Actions: \n
              Go west\n
              Go east""")
    elif position == [-2,4]:
        print("""Possible Actions: \n
              Look into the treasury room\n
              Go into the treasury room\n
              Go west\n""")
    action_name = input("What do you want to do?").lower().strip()
    print(f"Action chosen: {action_name}")
    position, sea_closed, captains_closed, armory_closed, inventory, game_over = do_action(action_name, position, sea_closed, captains_closed, armory_closed, inventory, game_over)
    return position, sea_closed, captains_closed, armory_closed, inventory, game_over

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
    position = [0,0]
    sea_closed = False
    captains_closed = False
    armory_closed = False
    
    inventory = []
    
    game_over = False
    
    print("Welcome, your name is Jack Sparrow and you just found the BluePearl pirate ship.")
    print("Your mission is to explore the ship and retrieve the most valuable objects in each room to be the most respected pirate of the Sea. ")
    print("\n")
    print("\n")
    
    while not game_over:
        position, sea_closed, captains_closed, armory_closed, inventory, game_over = possible_actions(position, sea_closed, captains_closed, armory_closed, inventory, game_over)
        print("======================\n")
    object_score(inventory)
    
if __name__ == "__main__":
    main()