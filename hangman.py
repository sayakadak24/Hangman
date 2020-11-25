#Choosing a random word
import random
from hangman_words import word_list
chosen_word = random.choice(word_list)

# Hint to help in debugging
print("Pff, the word is", chosen_word)

#Creating an empty list:
display = []
for letter in range(chosen_word.__len__()):
    display.append("_")

from hangman_art import stages, logo
print(logo)
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #if user enters a letter they have already guessed
    if guess in display:
      print(f"You have already guessed the letter {guess}")

    for position in range(len(chosen_word)):
        second_last_display = display
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    
    print(f"{' '.join(display)}")

    #game mechanics if player guesses incorrectly    
    if guess not in chosen_word:
        lives-=1
        print(f"Oops, there is no letter {guess} in the word")
        #game over if player loses
        if lives == 0:
            end_of_game = True
            print("You lose")

    #game over if player wins
    if "_" not in display:
        end_of_game = True
        print("You Win")
    
    print(stages[lives])

