import random

def game(number, number2):
    hidden_number = random.randint(number, number2)
    guess = None
    while guess != hidden_number:
        guess = int(input(f'Guess a hidden number within a range of {number} and {number2}.'))
        if guess > hidden_number:
            print('Your number is high. Try again!')
        elif guess < hidden_number:
            print('Your number is low. Try again!')
    print(f'Genius! You have guessed correctly! The hidden number is {hidden_number}.')


n = input('Give a number from 1 to 10: ')
n2 = input('Give a number from 11 to 20: ')

try:
    game(int(n), int(n2))
except ValueError:
    print('Input Error! Input a number in a numeric form only.')
