#info początkowe o grze
#-----------------------

#Zmienne do gry:
#n - wybrana przez gracza litera
#passwd - hasło do odgadnięcia przez gracza
#unpasswd - zakryte hasło gry, litery zmienione na gwiazdki
#counter - licznik odmierzający błędne litery, jeśli counter>=7, to gracz przegrywa

#Stars appearnig

listPasswd = list("Zbigniew Wodecki")
strUnpasswd = ''.join(["*" if item.isalpha() else ' ' for item in listPasswd])

"""
print(''.join(listPasswd))
print(strUnpasswd)
print(list(strUnpasswd))


listUnpasswd = list(unpasswd)
n = input("Enter a letter: ")
for num, item in enumerate(passwd):
    if n==item:
"""