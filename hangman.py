#Informations about the game
#-----------------------
#Variables:
#n - letter which is choose by a Gamer
#passwd - password which is guess by a Gamer
#unpasswd - hidden password which is cover by stars
#counter - main counter, when Gamer has more than 6 then lost
#innerCounter - counter which show Gamer chose good letter, if not the main counter will be increased
#game_set - when game_set is False, game is over (bad or good way)

#imported modules
import random
from gallows import gallows
from passwdsLists import listWithSingers
from passwdsLists import listWithCountries

#Starting conditions
game_con = True
counter = 0

while game_con:
    game_set = True
    #Some text to make the game more interactive
    print("Hello! Choose game mode:")
    print("1. Singers")
    print("2. Countries")
    print("3. EXIT")
    
    remote_control = input()
    
    #Taking the passwd from list and display it
    if remote_control == "1":
        listPasswd = list(random.choice(listWithSingers).upper())
        print("You choose mode: Singers!\n")
    elif remote_control == "2":
        listPasswd = list(random.choice(listWithCountries).upper())
        print("You choose mode: Countries!\n")
    elif remote_control == "3":
        game_con = False
        print("Bye!\n")
    else:
        print("Try again...\n")
        game_set = False
        #by default
        listPasswd = list(random.choice(listWithSingers).upper())
    #Stars appearing
    strUnpasswd = ''.join(["*" if item.isalpha() else ' ' for item in listPasswd])
    
    while game_set & game_con:     
        #Checking loop for condition if n==letter_from_passwd
        listUnpasswd = list(strUnpasswd)
        n = input("Enter a letter: ").upper()
        innerCounter = 0
        for num, item in enumerate(listPasswd):
            if n==item:
                listUnpasswd[num] = listPasswd[num]
                innerCounter += 1

        strUnpasswd = ''.join(listUnpasswd)
        print(strUnpasswd)
    
        #Confirmation that gamer choose good letter, if not then increase the counter
        if innerCounter == 0:
            #print(f"Damn, you made {counter}/8 bad decision...")
            print(gallows[counter])
            counter += 1
    
        #Checking if counter is lower than 8, if not then game is over
        if counter == 8:
            game_set = False
            print("\n----------------\n")
            #print(gallows[-1])
            print("Oh no! You lost!")
            print("\n----------------\n")
            
        if "*" not in listUnpasswd:
            game_set = False
            print("\n------------------------\n")
            print("Congratulation! You won!")
            print("\n------------------------\n")
    