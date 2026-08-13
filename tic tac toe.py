import random



def display_board():
        print(board[0], '|', board[1], '|', board[2])
        print('----------')
        print(board[3], '|', board[4], '|', board[5])
        print('----------')
        print(board[6], '|', board[7], '|', board[8])

def get_player_move():
    while True:
        player_move = int(input('Pick a number'))
        if player_move >= 1 and player_move <= 9:
            if board[player_move -1].isdigit():
                return player_move 
            else:
                print('That spot is already taken')
        else:
            print ('Please enter a number between 1 and 9')


def computer_move():
    available_spots = []
    for spot in board:
        if spot.isdigit():
            available_spots.append(spot)

    chosen = random.choice(available_spots)
    return int (chosen)

winning_combinations =[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

def check_winner():
    for combination in winning_combinations:
        a = combination [0]
        b = combination [1]
        c = combination [2]
        if board [a] == board[b] ==board[c] and board[a].isdigit()== False:
            return True
    return False

def check_tie():
    tie = True
    for spot in board:
        if spot.isdigit():
            tie = False
    return tie 


while True:
    try:
        target_score = int(input('First to how many wins?: '))
        if target_score >= 1:
            break
        else:
            print('Please enter a number greater than 0')
    except ValueError:
        print('That is not a valid number, try again')
player_score = 0
computer_score = 0

while True:
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board()

    while True:
        player_move = get_player_move()
        board[player_move - 1]= 'X'
        print(f'You placed {player_move}')
        display_board()

        if check_winner():
            print ('You win')
            player_score += 1
            break
        if check_tie():
            print('It is a tie')
            break

        computer_choice = computer_move()
        board[computer_choice - 1]= 'O'
        print (f'Computer placed {computer_choice}')
        display_board()

        if check_winner():
            print ('Computer win')
            computer_score +=1 
            break
        if check_tie():
            print('It is a tie')
            break

    print(f'SCORE: You - {player_score}  Computer - {computer_score}')

    if player_score == target_score:
        print('You won the match!')
        break
    if computer_score == target_score:
        print('Computer won the match!')
        break



