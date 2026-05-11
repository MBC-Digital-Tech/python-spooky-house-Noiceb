import random
print ("The aim of this game is to escape the spooky house.")

scary_sounds = ["a creaky door","a whisper","a loud bang","footsteps behind you"]

print("You enter a spooky house. It's dark and silent... except for", random.choice(scary_sounds))
print("You see two doors: one RED and one BLUE.")

choice1 = input("Which door do you choose? (red/blue) ").lower()

if choice1 == "red":
    print("The red door creaks open... You see a dusty staircase and a dark hallway.")
    choice2 = input("Do you go UP the stairs or into the HALLWAY? (up/hallway) ").lower()
    if choice2 == "up":
        print("You reach the attic and find a window. You escape! Yay!")
    elif choice2 == "hallway":
        print("The hallway leads to a locked door... Suddenly, you hear footsteps behind you. BOO! GAME OVER!")
    else:
        print("invalid choice you idiot, restart")
elif choice1 == "blue":
    print("You find a bottle of mystery liquid sitting upon a small table")
    choice3 = input("Do you drink it, yes/no?")
    if choice3 == "no":
        print("Good Choice, you escape home through a trapdoor hidden under the table and live")
    elif choice3 == "yes":
        print("The taste is delightful, but you feel a strange burn on your insides")
        choice4 = input("Take another sip? yes/no?")
        if choice4 == "yes":
            print("Your drinking acid, your internal organs dissolve and you cease to live")
        elif choice4 == "no":
            print("You escape home through a trapdoor hidden under the table and try not to think about it, turns out you drank acid which fataly damaged your internal organs, you die.")
        else:
            print("invalid choice, restart")

else:
    print("invalid choice, you die now restart")
   
