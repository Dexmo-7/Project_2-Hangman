#info początkowe o grze
#-----------------------

#Zmienne do gry:
#n - wybrana przez gracza litera
#passwd - hasło do odgadnięcia przez gracza
#unpasswd - zakryte hasło gry, litery zmienione na gwiazdki
#counter - licznik odmierzający błędne litery, jeśli counter>=7, to gracz przegrywa

passwd = list("Zbigniew Wodecki")
unpasswd = ''.join(["*" if item.isalpha() else ' ' for item in passwd])
unpasswd=(" ").join(unpasswd)
print(''.join(passwd))
print(unpasswd)
