# NUMBER GUESSING GAME 
import random

max_attempts = 5

def generate_number ():
        number = random.randint(1, 30)
        return number


def get_valid_guess():
        while True:
            try:
                guess = int(input('Guess a number between 1 and 30: '))
                if guess >= 1 and guess <= 30:
                    return guess
                else:
                    print('Please Enter a number between 1 and 30')
            except ValueError:
                print('That is not a valid number, Try again')
while True:
    secret_number = generate_number()
    attempts_used = 0
    guess = get_valid_guess()
    attempts_used += 1 

    while guess != secret_number and attempts_used < max_attempts:
        if guess > secret_number:
            print('Too High, Guess again')
        elif guess < secret_number:
            print('Too Low, Guess again')
        else:
            print('You are a mindreader!!')
        print(f'Attempts remaining: {max_attempts-attempts_used}')

        guess = get_valid_guess()
        attempts_used += 1

    if guess == secret_number:
        print('You are a mindreader!!')
    else:
        print(f'GAME OVER!! , Secret Number is {secret_number}')

    play_again = input('Play again? (YES NO)').strip().upper()
    if play_again == 'NO':
        break