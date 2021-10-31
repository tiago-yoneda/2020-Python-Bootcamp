from classes.Player import Player
from classes.Deck import Deck
from validations.name import validate_name
from validations.input import validate_input
from validations.bet import validate_bet
from validations.next_round import validate_next_round

def check_score(player):
    print(f"{player.name} tem {player.points} pontos")
    print_cards(player)

def check_game_over(player, amount):
    if player.points == 21:
        print("BLACKJACK!! Parabéns você ganhou")
        player.receive(2 * amount)
        return 1
    elif player.points > 21:
        print("BOOOM!!! Você perdeu")
        player.pay(amount)
        return -1
    else: 
        return 0

def print_cards(player):
    cards = [card.rank for card in player.cards_on_hand]
    response = "-> Com as cartas: "
    for card in cards[:len(cards) - 1]:
        response += f'{card}, '
    response += cards[-1]
    print(response)

def game_round(player):
    player.clear_hand()
    amount_bet = validate_bet(player)
    dealer = Player("Dealer")

    game_deck = Deck()

    # first round
    for _ in range(2):
        carta = game_deck.deal_one()
        player.add_card(carta)
        carta = game_deck.deal_one()
        dealer.add_card(carta)

    if not check_game_over(player, amount_bet) == 0:
        check_score(player)
        return

    print(f"#----#")
    check_score(player)
    print(f'Dealer tem {dealer.cards_on_hand[1].value} pontos')
    print(f'-> Com a carta: {dealer.cards_on_hand[1].rank}')
    print(f"#----#\n")

    # player turn
    while True:
        next_action = validate_input()
        if next_action == "P":
            print("Fim da vez do jogador")
            check_score(player)
            break
        if next_action == "H":
            carta = game_deck.deal_one()
            print(f'Você recebeu um {carta.rank}')
            player.add_card(carta)
            if not check_game_over(player, amount_bet) == 0:
                check_score(player)
                return
            check_score(player)

    #dealer turn
    print("\n# -- Vez do Dealer -- #")
    check_score(dealer)

    while dealer.points < player.points and dealer.points < 21:
        carta = game_deck.deal_one()
        print(f'Dealer recebeu um {carta.rank}')
        dealer.add_card(carta)
        check_score(dealer)

    #outcome phase
    if dealer.points > 21:
        print(f"Parabens, {player.name} ganhou!\n")
        player.receive(amount_bet)
    elif dealer.points == player.points:
        print(f"Que pena, deu empate\n")
    elif dealer.points > player.points and dealer.points <= 21 :
        print("Você perdeu\n")
        player.pay(amount_bet)

def BlackJack():
    player_name = validate_name()
    player = Player(player_name)

    while True:
        game_round(player)
        next_round = validate_next_round()
        if next_round in ["n", "no"]:
            break
        

    print("Fim de jogo")
    print(f"Você está saindo com R${player.wallet}")

BlackJack()