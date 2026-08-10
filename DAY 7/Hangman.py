import random

word_list = ["python", "java", "kotlin", "javascript", "programming", "computer", "keyboard",
            "developer", "software", "internet", "database", "algorithm", "function", 
            "variable", "terminal", "github", "coding", "website", "browser", "network", 
            "server", "application", "technology", "debugging", "framework", 
            "frontend", "backend", "fullstack", "react", "mongodb"]
chosen_word = random.choice(word_list)

print("Welcome to Hangman!")
print("The word has", len(chosen_word), "letters.")

placeholder = "_" * len(chosen_word)
print(placeholder)

lives = 6

stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

while "_" in placeholder and lives > 0:

    guess = input("Guess a letter: ").lower()

    display = ""

    for l in range(len(chosen_word)):
        if chosen_word[l] == guess:
            display += guess
        else:
            display += placeholder[l]

    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess!")
        print("Lives remaining:", lives)

    placeholder = display

    print(placeholder)
    print(stages[6 - lives])

if "_" not in placeholder:
    print("🎉 You won!")
    print("The word was:", chosen_word)
else:
    print("💀 You lost!")
    print("The word was:", chosen_word)