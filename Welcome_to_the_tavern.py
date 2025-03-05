#REMOVE ALL COMMENTS BTW, THIS IS JUST A REMINDER :p
def Tavern ():
    def restart():
        redo = input("Would you like to play again? ")
        if redo == "yes":
            Tavern()
        else:
            print("That's alright, thank you for playing.")
    inventory = ["Dragon egg", "a pouch containing ten coins", "a healing potion", "a sword", "a badge", "your rations"]
    #possibly add more to this
    #maybe change from second peson to first?
    print("Your boots land in the soft snow as you leave the forest. The wind blows through your hair and into your face.")
    print("The brush it to the side, before stopping into front of the building before you.")
    print("It's a tavern, and an infamous one at that. It serves all kinds, no questions of your situation or identity.")
    print("Which is a benefit to you right now, the less you're known the better.")
    print("You sigh, 'let's do this' you mumble to yourself, 'first a double check'.")
    print("You take your bag off of your back, before looking inside. You check your current inevntory: ")
    print(inventory)
    #maybe add a scene or ability to examine your inventory?
    print("You sigh in relief, 'it's all there', you linger your hand over the open bag.")
    print("Even my treasure.")
    print("You look back up at the tavern before closing your bag and slinging it back onto your back.")
    print("You walk towards the tavern door before pausing...")
    print("You stare down at the doorknob, 'should I really take a small break?' you ask yourself, unsure if it's worth risking the mission for.")
    first_choice = input("Should you enter the tavern? ")
    if first_choice == "yes":
        print("You deserve a break, besides this tavern won't question you or your mission. It's the safest place you could take a break.")
        print("You grab the door knob before pushing the door open. You step inside, closing the door behind you.")
        print("The tavern is glowing a light orange from the lights. Wamrth from the fireplace helps subside the coldnes you once felt.")
        print("There are a few other travelers in the tavern but none pay you any mind.")
        print("You look over towards the counter, walking up before sitting down one on of the stools.")
        print("It only takes a moment until one of the workers is standing opposite of you on the other side of the counter.")
        print("Based on their pointed ears, they're likely an elf. They have long white hair pulled into a ponytail which rests on their shoulder, occampanied by illuminating green eyes.")
        print("They appear to be wearing the taverns uniform.")
        print("They smile warmly at you, 'good morning,' they say, 'how can I help you?'")
        print("You glance at the menu, 'i'd like a drink' you say. You'll get a meal after if you can afford it. But seeing as you've run out of bevarges, that's more of a prority to you.")
        print("They nod before handing you the drink menu, 'what kind?' they ask.")
        print("You look down at the menu, scanning it's content.")
        print("They have: hollowberry smoothie, a cold winters eve, lemon spark, ")
        #add more drinks
        second_choice = input("However, one drink catches your eyes: ")
        if second_choice == "hollowberry smoothie":
            print("The waiter nods before turning away from you to make your drink. You lean back agaisnt your seat.")
            print("You exhale, exhuastion creeps over you. It's been a long journey, but it'll hopefully come to an end in the coming weeks")
            print("You hear a clink as your drink is slid in front of you.")
            print("You nod a thank you to the waiter, 'no problem,' they assure, 'that'll be five coins'.")
            third_choice = input("What will you pay ? ")
            if third_choice == "Dragon egg":
                print("No")
            elif third_choice == "five coins":
                print("yay")
            elif third_choice == "a healing potion":
                print("yummy")
            elif third_choice == "a sword":
                print("owwy")
            elif third_choice == "a badge":
                print("wow!")
            elif third_choice == "your rations":
                print("nom nom")
            else:
                print("The waiter stares at you before sighing, 'no payment means no drink,' they slide the drink away from you and back into their hand.")
                print("You sigh before getting up, guess you aren't getting a drink today.")
                print("You decide that staying any longer would put greater risk on your mission, so you stand up before leaving the tavern.")
                print("You head back onto the road you've been following for days now.")
                print("The sooner you return the egg to your captain, the sooner you'll be able to put this war behind you.")
                print("You feel the egg in your bag rock, but you ignore it's movement. It won't hatch for a month, you've got time.")
                restart()
            #inventory = ["Dragon egg", "a pouch containing ten coins", "a healing potion", "a sword", "a badge", "your rations"]
        elif second_choice == "a cold winters eve":
            print("The waiter nods before turning away from you to make your drink. You lean back agaisnt your seat.")
            print("You exhale, exhuastion creeps over you. It's been a long journey, but it'll hopefully come to an end in the coming weeks")
            print("You hear a clink as your drink is slid in front of you.")
            print("You nod a thank you to the waiter, 'no problem,' they assure, 'that'll be ten coins'.")
            third_choice = input("What will you pay ? ")
            if third_choice == "Dragon egg":
                print("No")
            elif third_choice == "ten coins":
                print("yay")
            elif third_choice == "a healing potion":
                print("yummy")
            elif third_choice == "a sword":
                print("owwy")
            elif third_choice == "a badge":
                print("wow!")
            elif third_choice == "your rations":
                print("nom nom")
            else:
                print("The waiter stares at you before sighing, 'no payment means no drink,' they slide the drink away from you and back into their hand.")
                print("You sigh before getting up, guess you aren't getting a drink today.")
                print("You decide that staying any longer would put greater risk on your mission, so you stand up before leaving the tavern.")
                print("You head back onto the road you've been following for days now.")
                print("The sooner you return the egg to your captain, the sooner you'll be able to put this war behind you.")
                print("You feel the egg in your bag rock, but you ignore it's movement. It won't hatch for a month, you've got time.")
                restart()
        elif second_choice == "lemon spark":
            print("The waiter nods before turning away from you to make your drink. You lean back agaisnt your seat.")
            print("You exhale, exhuastion creeps over you. It's been a long journey, but it'll hopefully come to an end in the coming weeks")
            print("You hear a clink as your drink is slid in front of you.")
            print("You nod a thank you to the waiter, 'no problem,' they assure, 'that'll be fifteen coins'.")
            third_choice = input("What will you pay ? 'Note if you're paying with coins, write 'your coins' instead of a number': ")
            if third_choice == "Dragon egg":
                print("No")
            elif third_choice == "your coins":
                print("yay")
            elif third_choice == "a healing potion":
                print("yummy")
            elif third_choice == "a sword":
                print("owwy")
            elif third_choice == "a badge":
                print("wow!")
            elif third_choice == "your rations":
                print("nom nom")
            else:
                print("The waiter stares at you before sighing, 'no payment means no drink,' they slide the drink away from you and back into their hand.")
                print("You sigh before getting up, guess you aren't getting a drink today.")
                print("You decide that staying any longer would put greater risk on your mission, so you stand up before leaving the tavern.")
                print("You head back onto the road you've been following for days now.")
                print("The sooner you return the egg to your captain, the sooner you'll be able to put this war behind you.")
                print("You feel the egg in your bag rock, but you ignore it's movement. It won't hatch for a month, you've got time.")
                restart()
        else:
            print("The waiter stares at you for a moment, processesing what you said.")
            print("They chuckle to themself, 'sorry we don't serve that!' they say, 'anything else you'd like?'")
            print("You shake your head, alas that was the only thing you wanted.")
            print("They shrug, 'you can relax here if you want or order something else,' they assure before moving onto a newly arrived customer.")
            print("You decide that staying any longer would put greater risk on your mission, so you stand up before leaving the tavern.")
            print("You head back onto the road you've been following for days now.")
            print("The sooner you return the egg to your captain, the sooner you'll be able to put this war behind you.")
            print("You feel the egg in your bag rock, but you ignore it's movement. It won't hatch for a month, you've got time.")
            restart()
    elif first_choice == "no":
        print("You stare at the door before pulling your hand back, 'it isn't worth the risk' you tell yourself, turning away from the tavern.")
        print("You'll just get a drink elsewhere.")
        print("You walk away from the tavern and back onto the road you've been following for days now.")
        print("The sooner you return the egg to your captain, the sooner you'll be able to put this war behind you.")
        print("You feel the egg in your bag rock, but you ignore it's movement. It won't hatch for a month, you've got time.")
        restart()
    else:
        print("Gonna be honest with you as the narrator, that isn't really an option.")
        print("So you're gonna need to restart now..sorry")
        restart()

Tavern()