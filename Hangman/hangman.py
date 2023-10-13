import random
from hangman_art import stages, logo
from day7.hangman_word import word_list

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_" for i in range(word_length)]

end_of_game = False

lives = 6

while not end_of_game:

    guess = str(input("Guess a letter: ")).lower()
    
    if guess in display:
        print(f"You have alread guessed {guess}.")

    for i in range(word_length):

        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives-=1
        print(f'You guessed {guess}, thats not in word. You lose a life.' )
        if lives == 0:
            end_of_game = True
            print("You lose!!")


    print(' '.join(display))
    print(stages[lives])
    print(lives)

    if not "_" in display:
        end_of_game = True
        print("You Win!!!")






