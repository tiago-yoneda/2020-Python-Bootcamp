#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

'''
Setting 'suits', 'ranks' and 'values' to use later
'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#Class card that has all it's attributes
class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return self.rank + " of " + self.suit

#Deck class with its atributtes
class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Dealer:
    
    def __init__(self, name):

        self.name = name
        self.all_cards = []
                
    def add_cards(self, new_cards):
        self.all_cards.append(new_cards)

class Player:

    def __init__(self, name, chips):

        self.name = name
        self.all_cards = []
        self.chips = chips
        
    def __str__(self):
        return f"{self.name} has ${self.chips} in chips."
    
    def show_hand(self):
        print(f"\n<== {self.name}'s hand ==>")
        for item in self.all_cards:
            print (item)
    def add_cards(self, new_card):
        self.all_cards.append(new_card)
            
            
def first_deal(player,dealer,deck):
    for item in range(2):
        player.add_cards(deck.all_cards.pop(0))
        dealer.add_cards(deck.all_cards.pop(0))

def player_sum(player):
    card_sum = 0
    has_ace = 0    
    
    for item in  player.all_cards:
        card_sum += item.value
        if "Ace" in item.rank:
            has_ace +=1
    while has_ace > 0:
        if card_sum > 21 :
            has_ace -= 1
            card_sum -= 10
    print(f'{player.name} has {card_sum} points.')
    
    return card_sum
        

def check_bet(player):
    bet_ok = False
    
    while not bet_ok:
        try:
            bet = int(input ("How much would you like to bet? "))
            if bet <= player.chips:
                bet_ok = True
            else:
                print('Not enough funds\n')
        except:
            print ("Please input a valid amount\n")
    return bet

def game_on():
    keep_playing = False
    again = ""
    
    while again not in ['y','n']:
        again = input ("\nPlay another round? Y/N: ").lower()
        if again not in ['y','n']:
            print("Please, choose (Y)es or (N)o.")
        if again == "y":
            keep_playing = True
        
    return keep_playing

def blackjack_game():
    keep_playing = True
    
    player_name = input ("Hi welcome, please input your name: ")
    
    dealer = Dealer('Dealer')
    player = Player(player_name,300)

    while keep_playing:
        
        round_result = blackjack_round(player, dealer)
        print (round_result[0])
        if round_result[0] == 3:
            player.chips += round_result[1]*2
        if round_result[0] == 1:
            player.chips += round_result[1]
        if round_result[0] == -1:
            player.chips -= round_result[1]
        player.all_cards = []
        dealer.all_cards = []
        
        keep_playing = game_on()
        
    print(f"\nThank you for playing! You have ${player.chips} left.")
    
    
def blackjack_round(player, dealer):
    done = False
    win = 0   
    confirmation = " "
    dealer_points = 0
    player_points = 0
    
    
    print(f"You have ${player.chips} available")
    bet = check_bet(player)
          
    new_deck = Deck()
    new_deck.shuffle()

    first_deal(player, dealer, new_deck)
    
    print("\n<== Dealer's hand ==>")
    print (dealer.all_cards[0])

    player.show_hand()

    player_points = player_sum(player)
        
    if player_points == 21:
        print ("~~BlackJack!! You Won!!~~")
        done = True
        win = 3
    
    while not done:
        while confirmation.lower() not in ['h', 's']:
            confirmation = input ("\nWould you like to (H)it or (S)tand? ")

        if confirmation == "h":
                 
            player.add_cards(new_deck.all_cards.pop(0))
            player.show_hand()
            player_points = player_sum(player)
        
            if player_points > 21:
                print ("\nYou exceeded 21 points. You lost this round.")
                win = -1
                return (win, bet)
                
            if player_points == 21:
                print("It's a blackjack!")
                done = True
            confirmation = ""
            
        if confirmation == "s":
            done = True
    
    print("\n<== Dealer's hand ==>")
    for item in dealer.all_cards:
        print (item)
        
    dealer_points = player_sum (dealer)
                    
    while dealer_points < 21 and dealer_points < player_points: 
        draw_card = new_deck.all_cards.pop(0)
        dealer.add_cards(draw_card)
        print (f"Dealer drew a {draw_card}")
        dealer_points = player_sum (dealer)
            
    if dealer_points > 21 and player_points < 21:
        print (f"~~The dealer busted! {player.name} Won!~~")
        win = 1

    if dealer_points > player_points and dealer_points <= 21 :
        print ("Dealer won this round")
        win = -1
        
    if dealer_points != player_points and player_points == 21:
        print("You won! It's a blackjack")
        win = 2
        
    if dealer_points == player_points:
        print ("\nIt's a Draw!")
        win = 0   

    return (win, bet)

blackjack_game()


# In[ ]:




