import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    secret = random.randint(1, 20)
    guesses = 0
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    while True:
        guess = int(input("Take a guess\n"))
        guesses += 1
        if guess == secret:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
        elif guess < secret:
            print('Your guess is too low')
        else:
            print('Your guess is too high')

if __name__ == "__main__":
    guess_the_number()