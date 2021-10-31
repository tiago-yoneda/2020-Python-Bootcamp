def print_grid(array = ["1","2","3","4","5","6","7","8","9"]):
    simple_separator = f'{"":7}|{"":7}|{"":7}'
    big_separator = f'{"":_^7}|{"":_^7}|{"":_^7}\n{simple_separator}'
    print(simple_separator)
    print(f"{array[6]:^7}|{array[7]:^7}|{array[8]:^7}")
    print(big_separator)
    print(f"{array[3]:^7}|{array[4]:^7}|{array[5]:^7}")
    print(big_separator)
    print(f"{array[0]:^7}|{array[1]:^7}|{array[2]:^7}")
    print(simple_separator)

def checa_velha(array):
    if not "" in array:
        return True

def checa_vitoria(array, jogador_atual):
    jogador = ['x', 'o']
    rows = [array[0:3],array[3:6],array[6:]]
    columns = [array[0::3],array[1::3], array[2::3]]
    diagonals = [[array[0],array[4],array[8]],[array[2],array[4],array[6]]]
    all_options = rows + columns + diagonals
    for item in all_options:
        if not "" in item:
            if jogador_atual == 0:
                if not jogador[1] in item:
                    return True
            elif jogador_atual == 1:
                if not jogador[0] in item:
                    return True
    return False

def tic_tac_toe_round():
    print("Vamos começar a partida")
    players = ['x','o']
    jogador_atual = 0
    done = False
    while True:
        player_1 = input("Player 1, por favor escolha 'x' ou 'o': ")
        if player_1 in ['x', 'o']:
            if player_1 == 'x':
                jogador_atual = 0
            else:
                jogador_atual = 1
            break
    start_array = [""] * 9
    print('Para as próximas jogadas por favor escolha a posição como no modelo abaixo:')
    print_grid()
    while not done:
        #Jogar
        while True:
            jogada = input(f"Jogador {jogador_atual + 1}, escolha onde quer jogar: ")
            if not (jogada.isdigit() and int(jogada) in range(1,10) and start_array[int(jogada) - 1] == ""):
                print("Jogada Invalida")
            else:
                start_array[int(jogada) - 1] = players[jogador_atual]
                print_grid(start_array)
                if checa_vitoria(start_array, jogador_atual):
                    done = True
                    break
                jogador_atual = 0 if jogador_atual == 1 else 1
                break
        if checa_velha(start_array):
            print("Deu velha")
            done = True
    print(f"Fim de jogo, o ganhador foi o jogador {jogador_atual + 1}")

def tic_tac_toe():
    next_round = True
    while next_round:
        tic_tac_toe_round()
        while True:
            go_another_round = input("Continuar ? (S)im ou (N)ão? ")
            if go_another_round in ["S", "N"]:
                if go_another_round == "N":
                    next_round = False
                break


tic_tac_toe()