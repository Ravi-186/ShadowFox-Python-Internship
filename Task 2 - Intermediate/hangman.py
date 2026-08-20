"""
ShadowFox Python Internship - Task 2
Hangman: Word-guessing game with visual progress and hints
"""

import random

# ============================================
# 1. Word List + Hints
# ============================================
words_with_hints = {
    "python": "A popular programming language",
    "shadowfox": "Name of this internship platform",
    "hangman": "The name of this game",
    "internship": "A temporary training program",
    "developer": "A person who writes code",
    "algorithm": "Step-by-step solution to a problem",
    "variable": "Used to store data in programming",
    "function": "A reusable block of code",
    "dictionary": "Key-value data structure in Python",
    "beautiful": "Related to a popular web scraping library"
}

# ============================================
# 2. Hangman Visual Stages (0 to 6 wrong guesses)
# ============================================
hangman_stages = [
    # 0 wrong
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    # 1 wrong
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # 2 wrong
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # 3 wrong
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # 4 wrong
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    # 5 wrong
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    # 6 wrong (Game Over)
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]


def play_hangman():
    # ----------------------------------------
    # Game Setup
    # ----------------------------------------
    word = random.choice(list(words_with_hints.keys()))
    hint = words_with_hints[word]

    guessed_letters = []          # Letters already guessed
    wrong_guesses = 0             # Number of incorrect guesses
    max_attempts = 6              # Maximum wrong guesses allowed
    hint_used = False             # Player can use hint only once

    print("\n" + "="*45)
    print("          WELCOME TO HANGMAN")
    print("="*45)
    print("Guess the word one letter at a time.")
    print("Type 'hint' to get a clue (only once).")
    print("="*45)

    # ----------------------------------------
    # Game Loop
    # ----------------------------------------
    while wrong_guesses < max_attempts:

        # Display hangman figure
        print(hangman_stages[wrong_guesses])

        # Display the word with blanks
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word: ", display_word)

        print("Guessed letters:", " ".join(guessed_letters))
        print(f"Wrong guesses left: {max_attempts - wrong_guesses}")

        # ----------------------------------------
        # User Input
        # ----------------------------------------
        guess = input("\nEnter a letter (or type 'hint'): ").lower().strip()

        # Hint feature
        if guess == "hint":
            if hint_used:
                print("You have already used your hint!")
            else:
                print(f"💡 Hint: {hint}")
                hint_used = True
            continue

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Add the letter to guessed list
        guessed_letters.append(guess)

        # ----------------------------------------
        # Check Guess
        # ----------------------------------------
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")

        # ----------------------------------------
        # Win Condition
        # ----------------------------------------
        if all(letter in guessed_letters for letter in word):
            print(hangman_stages[wrong_guesses])
            print("\n🎉 Congratulations! You guessed the word:", word.upper())
            return  # Exit the function (game won)

    # ----------------------------------------
    # Loss Condition
    # ----------------------------------------
    print(hangman_stages[wrong_guesses])
    print("\n💀 Game Over! The word was:", word.upper())


# ============================================
# Main Program with Play Again option
# ============================================
while True:
    play_hangman()

    play_again = input("\nDo you want to play again? (yes/y or no/n): ").lower().strip()

    if play_again not in ["yes", "y"]:
        print("\nThanks for playing Hangman! Goodbye 👋")
        break