# DICE ROLLING GAME
# 
# import random

# def roll_die():
#     roll = random.randint(1, 6)
#     return roll

# target_score = int(input('First to win how many?: '))

# player_score= 0
# computer_score = 0
# while True:
#     while True:
#         try:
#             player = int(input('Enter a number;'))
#             if player >=1 and player <=6:
#                 break
#             else:
#                 print('Please enter a number between 1 and 6.')
#         except ValueError:
#             print('This is not a valid number, try again.')
#     computer_roll = roll_die()
#     print (f'You played {player} ,Computer played {computer_roll}')
#     if player > computer_roll:
#         print('You win !!')
#         player_score += 1
#     elif computer_roll > player:
#         print('You lose, Computer wins!!')
#         computer_score += 1
#     else:
#         print('Its a tie! Try Again.')
    
#     print (f' SCORE: You- {player_score}  Computer-{computer_score}')

#     if player_score == target_score:
#         print('You won the match!')
#         break
#     if computer_score == target_score:
#         print('Computer wins the match!!')
#         break
    
#     play_again = input('Play again? (YES NO)').strip().upper()
#     if play_again == 'NO':
#         break








