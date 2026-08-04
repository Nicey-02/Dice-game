#  ROCK PAPER SCISSORS

# import random

# def computer_choice():
#     pick = random.choice(['Rock', 'Paper', 'Scissors'])
#     return pick

# def get_valid_guess():
#     while True:
#         guess = (input('Rock, paper, scissors? '))
#         if guess.lower() in ['rock', 'paper', 'scissors']:
#             return guess.lower()
#         else:
#             print('Please pick a valid option')


import random
player_score = 0
computer_score = 0
target_score = int(input('First to win how many?: '))

def get_choices():
    options = ['Rock', 'Paper', 'Scissors']

    while True:
        player_choice =input ('Enter a choice (Rock, Paper , Scissors): ').capitalize()
        if player_choice in options:
            break
        else:
            print('Enter a valid choice')
    
    computer_choice = random.choice (options)
    choices = {'Player': player_choice , 'Computer' : computer_choice}
    return choices

def check_win (player, computer) :
    print (f' You choose {player} , Computer choose {computer}')
    if player == computer:
        return "It's a tie !"
    elif player == 'Rock':
        if computer == 'Scissors':
            return 'Rock smashes Scissors ! You Win !'
        else:
            return 'Paper covers Rock ! You Lose.'
    elif player == 'Paper':
        if computer == 'Rock':
            return 'Paper covers Rock ! You Win !'
        else:
            return ' Scissors cuts Paper ! You Lose'
    elif player == 'Scissors':
        if computer == 'Rock':
            return 'Rock smashes Scissors! You Lose'
        else:
            return 'Scissors cuts Paper! You Win'
while True:
    choices = get_choices()
    result = check_win (choices ['Player'], choices ['Computer']) 
    print (result)

    if 'Win' in result :
        player_score +=1
    elif 'Lose' in result:
        computer_score +=1
    else:
        print('Its a tie!  Try again')

    print (f' SCORE: You- {player_score}  Computer-{computer_score}')


    if player_score == target_score:
        print('You won the match!')
        break
    if computer_score == target_score:
        print('Computer wins the match!!')
        break    

    