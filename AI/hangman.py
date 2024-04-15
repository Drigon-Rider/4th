import random

def choose_word():
    words = ["train","bus","car","humain","cow","dog","teacher","computer","book","phonecover"]
    return random.choice(words)

def get_guess():
    return input("Guess a letter: ").lower()

def check_guess(word, guessed_letters, guess):
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        return False

    guessed_letters.append(guess)

    if guess not in word:
        print("Incorrect guess.")
        return False

    return True

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = get_guess()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if not check_guess(word_to_guess, guessed_letters, guess):
            attempts += 1
            print("Attempts left:", max_attempts - attempts)

        displayed = display_word(word_to_guess, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if attempts == max_attempts:
            print("Sorry, you ran out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()


    


