def validate_bet(player):
    while True:
        bet = input("Quando você gostaria de apostar: ")
        if bet.isdigit() and int(bet) > 0:
            bet = int(bet)
            if bet < player.wallet:
                break
            else:
                print('Invalid funds')
    return bet