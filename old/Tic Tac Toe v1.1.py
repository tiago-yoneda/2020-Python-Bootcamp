#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Check if the players are ready to start the game
def ready_check ():

    ready = False
    while not ready:
        yn = input ("Are you ready to play?(Y/N) :").upper()
    
        if yn not in ["Y", "N"]:
            print("Sorry, I didn't understand that, please choose Y or N.")
    
        if yn == "Y":
            ready = True       
          
    return ready  


###Player 1 will choose if he'll be X or O
def choose_xo():
    done = False

    while not done:
        player1 = input("Player 1, please choose 'X' or 'O': ").upper()
        
        if player1 not in ["X", "O"]:
            print("Invalid option. Please choose 'X' or 'O'")
            
        if player1 == "X":
            player2 = "O"
            done = True
            
        if player1 == "O":
            player2 = "X"
            done = True
    return (player1,player2)


###Simple board display, it uses a dictionary to show the moves
def display_board(plays):
    lines = "_ _ _|_ _ _|_ _ _"
    colums = "     |     |     "
    
    print(colums)
    print(f'  {plays["7"]}  |  {plays["8"]}  |  {plays["9"]}  ')
    print(lines)
    print(colums)
    print(f'  {plays["4"]}  |  {plays["5"]}  |  {plays["6"]}  ')
    print(lines)
    print(colums)
    print(f'  {plays["1"]}  |  {plays["2"]}  |  {plays["3"]}  ')
    print(colums)
    
    
### Confirmation to play again
def keep_playing():
    done = False
    while not done:
        answer = input ("Would you like to keep playing? (Y/N): " ).upper()
    
        if answer not in ["Y", "N"]:
            print("Sorry, I didn't get that.")
        
        if answer == "Y":
            return True
        
        if answer == "N":
            return False
        
        
### Will input the player move on the board, and check if the spot is already taken
def plays(moves,player,idx):
    done = False
    
    while not done:
        chosen = input ("Choose a place to play: ")

        if chosen not in ['1','2','3','4','5','6','7','8','9']:
            print ("Choose a spot from 1 to 9.")
            continue 
        if moves [chosen] != " ":
            print ("Please choose an empty spot to play.")
            continue  
        moves [chosen] = player[idx]
        done = True
    
    
###Check if there's a winner
def check_win(moves):
    won = False
    row1 = (moves['1'],moves['2'],moves['3'])
    row2 = (moves['4'],moves['5'],moves['6'])
    row3 = (moves['7'],moves['8'],moves['9'])
    colum1 = (moves['1'],moves['4'],moves['7'])
    colum2 = (moves['2'],moves['5'],moves['8'])
    colum3 = (moves['3'],moves['6'],moves['9'])
    diag1 = (moves['1'],moves['5'],moves['9'])
    diag2 = (moves['3'],moves['5'],moves['7'])
    
    check = (set(row1),set(row2),set(row3),set(colum1),set(colum2),set(colum3),set(diag1), set(diag2))
    ### Will make sets of the rows, colums and diagonals and check if there's a winner    
    for item in check:
        if " " not in item and len(item) == 1:
            won = True

            
    return won



from IPython.display import clear_output
game_over = False




start = False
while not start:
    start = ready_check()

one_more = True
while one_more:
    clear_output(wait = True)
    print("Welcome to my game of Tic Tac Toe.")

    print("Please choose your moves according to the following model:")

    ###Numbered board to show where the players can play
    display_board({"1":'1',"2":'2',"3":'3',"4":'4',"5":'5',"6":'6',"7":'7',"8":'8',"9":'9'})

    
    player = choose_xo()
    
    ###Used to alternate between players
    idx = 0
    
    game_over = False
    moves = {"1":' ',"2":' ',"3":' ',"4":' ',"5":' ',"6":' ',"7":' ',"8":' ',"9":' '}



    while not game_over:
    
        print(f'It is now {player[idx]} turn')
        clear_output(wait=True)
        plays(moves,player,idx)
        display_board(moves)
    
        game_over = check_win(moves)
        if game_over:
            print (f'Congratulations, {player[idx]} won!')
            break
        if " " not in moves.values():
            print("End of the game, it's a TIE")
            game_over = True
            
        idx += 1 
        idx = idx%2

    one_more = keep_playing()


# In[ ]:




