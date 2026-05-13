import random

words = [
    "python", "computer", "keyboard", "mouse", "screen",
    "network", "internet", "server", "client", "database",
    "function", "variable", "loop", "condition", "string",
    "number", "random", "module", "package", "virtual",
    "project", "github", "terminal", "command", "window",
    "linux", "windows", "code", "debug", "compile",
    "game", "player", "level", "score", "winner",
    "banana", "orange", "apple", "grape", "melon",
    "car", "bike", "bus", "train", "plane", ]
entry = input("Choose whether you want to start Game or Exit: ")

if entry == "start":

    print("Game started")
    The_Word = list(random.choice(words))
    The_Word_2 = ["_"] * len(The_Word)
    original_word = "".join(The_Word)
    several_attempts = 10


    while several_attempts > 0 and "_" in The_Word_2:
        print("Word:", " ".join(The_Word_2))
        user_input = input("Enter a letter: ").lower()

        if len(user_input) != 1 or not user_input.isalpha():
            print("Enter a single letter!")
            continue

        found = False

        for i in range(len(The_Word)):
            if The_Word[i] == user_input:
                The_Word_2[i] = user_input
                The_Word[i] = "_"
                found = True
                break

        if found:
            print("Correct!")
        else:
            several_attempts -= 1
            print(f"Wrong! You have {several_attempts} attempts left.")

    if "_" in The_Word_2:
        print("You Lose!\n", "The word is:", original_word)
    else:
        print("You Win!\n", "The word is:", original_word)

else:
    print("Game Exited")