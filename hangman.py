import random
import time
last_pic = '''
+----+
 0   |
/|\  |
/ \  |
=======
'''
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()
def display_board(wrongGuesses, correctGuesses, secret ):
    print('H A N G M A N')
    print()
    print("MissedLetters: ", end=' ')
    for ch in wrongGuesses:
        print(ch, end='')
    print()
    dashes = '_' * len(secret)
    for i in range(len(secret)):
        if secret[i] in correctGuesses:
            dashes = dashes[:i] + secret[i] + dashes[i +1:]
    for i in dashes:
        print(i, end=' ')

def get_guess(already_guessed):
    print('Guess a letter. Give it a try! ')
    guess = input().lower()
    if len(guess) != 1:
        print("Enter a sinhle letter: ")
    elif guess in already_guessed:
        print("you have already tried this letter, so make an another choice")
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a LETTER.')
    else:
        return guess

def play_again():
    ans = input("Want to play again ? Yes or no").lower()
    if ans == "yes":
        return True
    else:
        return False

print('H A N G M A N')
print()
print("Guess the secret word, You have 10 Chances")
wrong_guesses = ''
correct_guesses = ''
game_is_over = False
secret = random.choice(words)
print(secret)
turns = 10

while turns > 0:
    display_board(wrong_guesses,correct_guesses,secret)
    guess = get_guess(wrong_guesses + correct_guesses)
    if guess == None:
        continue
    if guess in secret:
        print("You have a correct guess!")
        correct_guesses = correct_guesses + guess
        found_all = True
        for i in range(len(secret)):
            if secret[i] not in correct_guesses:
                found_all = False
                break
        if found_all:
            print('Yes! The secret word is "' + secret +
                  '"! You have won!')
            game_is_over =True

    else:
        turns = turns -1
        wrong_guesses = wrong_guesses + guess
        print('Not the right guess! you have chances', turns, 'left! ')
        if turns == 0:
            print('You have run out of guesses!', '\n', 'After ', len(wrong_guesses), 'chances' )
            print(last_pic)
            print("The secret was ", secret)
            game_is_over = True

    if game_is_over:
        if play_again():
            print('H A N G M A N')
            print()
            print("Guess the secret word, You have 10 Chances")
            wrong_guesses = ''
            correct_guesses = ''
            game_is_over = False
            secret = random.choice(words)
            print(secret)
            turns = 10
        else:
            break



