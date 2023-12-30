import random as rd
import hangman_draws

word_list = ["amanda", "amandinha", "fofinha", "lindeza", "gatinha", "sapeca", "florzinha"]
chosen_word = rd.choice(word_list)
lives = 6

display = ["_" for letter in chosen_word]
print(hangman_draws.logo)

while "_" in display and lives > 0:
    guess = input("\nAdivinhe uma letra: ").lower()
    if guess in display:
        print("\nVocê já escolheu essa letra!\n")
    for i, letter in enumerate(chosen_word):
        if guess == letter:
            display[i] = letter
    if guess not in chosen_word:
        lives -= 1
        print(hangman_draws.stages[lives])
    print(display) 

if lives == 0:
    print("Você perdeu!")
else:
    print("Você ganhou!")