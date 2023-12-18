import random
import pygame
import time

pygame.init()
sound_file = "file.wav"
pygame.mixer.init()
sound = pygame.mixer.Sound(sound_file)

def choose_word(level):
    easy_words = ["lion", "cat", "tiger", "monkey"]
    medium_words = ["python", "Microsoft", "Javascipt", "coding"]
    hard_words = ["intelligence", "algorithm", "Character", "framework"]

    if level == "easy":
        return random.choice(easy_words)
    elif level == "medium":
        return random.choice(medium_words)
    elif level == "hard":
        return random.choice(hard_words)
    else:
        print("Invalid level. Choosing a word from the easy level.")
        return random.choice(easy_words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 5
    guessed_letters = []
    attempts = 0

    level = input("Choose a level (easy, medium, hard): ").lower()
    word_to_guess = choose_word(level)

    print("Welcome to Hangman Game!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            left_attempts = max_attempts - attempts
            print("Incorrect guess. Attempts left:", left_attempts)
        else:
            print("Good guess!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            
            print("Congratulations! You guessed the word:", word_to_guess)
            print("*******************************")
            sound.play()
            time.sleep(sound.get_length())
            if (left_attempts == max_attempts):
                print("Out of 100 your score is 100")
            else:
                Fraction_score =left_attempts/max_attempts
                score = Fraction_score * 100
                print("Out of 100 your score is",score)
                break

    if "_" in current_display:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
