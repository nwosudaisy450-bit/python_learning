secret_number = 22
guess_limit = 3
guess_count = 0
choice = 0
print('''Can you guess the number I'm thinking of?
You have 3 tries''')
while True:
 while guess_count < guess_limit:
    if guess_count == 0:
        choice = int(input('Guess: '))
    guess_count += 1
    new_limit = guess_limit - guess_count

    if choice == secret_number:
        print('You guessed the number!🎊')
        break

    if guess_count == 1 or guess_count == 2:
        print(f'You have {new_limit} more guess(es)!')
    elif guess_count == 3:
        print(f'You lost! The number was {secret_number}')
        break

    if choice > secret_number:
        print('Too high! Try going lower')
        choice = int(input('Guess: '))

    elif choice < secret_number:
        print('Too low! Try going higher')
        choice = int(input('Guess: '))