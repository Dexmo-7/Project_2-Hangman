#Informations about the game
#-----------------------
#Variables:
#n - letter which is choose by a Gamer
#passwd - password which is guess by a Gamer
#unpasswd - hidden password which is cover by stars
#counter - main counter, when Gamer has more than 6 then lost
#innerCounter - counter which show Gamer chose good letter, if not the main counter will be increased
#game_set - when game_set is False, game is over (bad or good way)

#Starting conditions
game_set = True
game_con = True
counter = 0

#Stars appearing
print("Polish singer")
listPasswd = list("Zbigniew Wodecki".upper())
strUnpasswd = ''.join(["*" if item.isalpha() else ' ' for item in listPasswd])
print(strUnpasswd)

while game_con:
    print(""
    while game_set:

        #Checking loop for main condition if n==letter_from_passwd
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
            counter += 1
            print(f"Damn, you made {counter}/7 bad decision...")
    
        #Checking if counter is lower than 7, if not then game is over
        if counter == 7:
            game_set = False
            print("Oh no! You lost!")
    
        if "*" not in listUnpasswd:
            game_set = False
            print("Congratulation! You won!")
    