from games import RockPaperScissors, NumberGuessingGame, WordScramble

gameChoice = None
while not (gameChoice == 4):
    print("Brain Cube - Mini Games")
    print("1 -> Rock Paper Scissors")
    print("2 -> Number Guessing Game")
    print("3 -> Word Scramble")
    print("4 -> Exit")

    gameChoice = int(input("Your choice: "))

    if gameChoice == 1:
        print("Welcome to Rock Paper Scissors!")
        while True:
            RockPaperScissors()
            decision = int(input("Press 1 to play again, 2 to return to the main menu: "))
            if decision == 1:
                continue
            elif decision == 2:
                break

    elif gameChoice == 2:
        print("Welcome to the Number Guessing Game! Try to guess the number between 1 and 100.")
        while True:
            NumberGuessingGame()
            decision = int(input("Press 1 to play again, 2 to return to the main menu: "))
            if decision == 1:
                continue
            elif decision == 2:
                break

    elif gameChoice == 3:
        print("Welcome to Word Scrambler!")
        while True:
            while True:
                difficultyLevel = int(input("Enter difficulty level (5 to 7): "))
                valid_choices = [5, 6, 7]
                if difficultyLevel in valid_choices:
                    break
                else:
                    print("Invalid input. Please try again.")

            WordScramble(difficultyLevel)
            decision = int(input("Press 1 to play again, 2 to return to the main menu: "))
            if decision == 1:
                continue
            elif decision == 2:
                break

print("Thanks for using our program. Have a nice day! :)")
print("...")



