print('''
 .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Y0u are at a cross road. Where do you want to go? Type 'left' or 'right'")
dir = input().lower()
if dir == "right":
    print("You fell into a hole. Game Over.")
elif dir == "left":
    print("You come to a lake. There is an island in the middle of the lake. Type 'wait' or 'swim' to cross the lake.")
    ip = input().lower()
    if ip == "swim":
        print("Attacked by trout. Game Over.")
    elif ip == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        door = input().lower()
        if door == "red":
            print("It's a room full of fire.\n Game Over.")
        elif door == "blue":
            print("You enter a room of beasts.\\n Game Over.")
        elif door == "yellow":
            print("You found the treasure! \nYou Win!")
        else:
            print("You chose a door that doesn't exist.\n Game Over.")