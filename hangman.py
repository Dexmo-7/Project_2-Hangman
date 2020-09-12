#info początkowe o grze
#-----------------------

#Zmienne do gry:
#n - wybrana przez gracza litera
#passwd - hasło do odgadnięcia przez gracza
#unpasswd - zakryte hasło gry, litery zmienione na gwiazdki
#counter - licznik odmierzający błędne litery, jeśli counter>=7, to gracz przegrywa
#game_set - gdy wartość wyniesie false, gra zostaje przerwana

#Stars appearing
game_set = True
counter = 0

#Stars appearing
listPasswd = list("Zbigniew Wodecki".upper())
strUnpasswd = ''.join(["*" if item.isalpha() else ' ' for item in listPasswd])

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
        print("Congratulation! You win!")
    
    #print(strUnpasswd)
    