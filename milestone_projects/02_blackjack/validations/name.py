def validate_name():
    while True:
        player_name = input("Digite o seu nome: ")
        if len(player_name) > 3 and player_name.isalpha():
            break
    return player_name