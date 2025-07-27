from random import choice, randint, shuffle

def RockPaperScissors():
    userScore = 0
    computerScore = 0

    while not (userScore >= 3 or computerScore >= 3):
        computerChoice = choice(["rock", "paper", "scissors"]).lower()

        while True:
            userChoice = input("Rock, Paper, or Scissors? (Press '0' to exit): ").lower()
            valid_choices = ["rock", "paper", "scissors", "0"]
            if userChoice in valid_choices:
                break
            else:
                print("Invalid input, please try again.")

        if userChoice == "0":
            break

        print(f"Computer's choice: {computerChoice}")

        if userChoice == computerChoice:
            print("It's a tie.")
        elif userChoice == "paper" and computerChoice == "rock":
            print("You win this round!")
            userScore += 1
        elif userChoice == "rock" and computerChoice == "scissors":
            print("You win this round!")
            userScore += 1
        elif userChoice == "scissors" and computerChoice == "paper":
            print("You win this round!")
            userScore += 1
        else:
            print("You lost this round. Computer wins.")
            computerScore += 1

        print(f"Score: You = {userScore}, Computer = {computerScore}")

    if userScore >= 3:
        print("You won the game. Congratulations!")
    else:
        print("You lost the game. Better luck next time!")


def NumberGuessingGame():
    computerNumber = randint(1, 100)
    attemptCount = 0
    userGuess = None

    while not (userGuess == computerNumber):
        attemptCount += 1
        print(f"{attemptCount}. Attempt")

        while True:
            userGuess = int(input("Enter your guess (Press '0' to exit): "))
            valid_choices = list(range(101))
            if userGuess in valid_choices:
                break
            else:
                print("Invalid input. Please try again.")

        if userGuess == 0:
            break

        if userGuess > computerNumber:
            print("Try a lower number.")
        elif userGuess < computerNumber:
            print("Try a higher number.")
        else:
            print(f"Congratulations! You found it in {attemptCount} attempts.")


def WordScramble(difficultyLevel):
    wordAttemptCount = 0

    if difficultyLevel == 5:
        easy_words = ["apple", "grape", "lemon", "table", "chair", "piano", "heart", "bread", "smile", "house", "plant", "stone", "water", "light", "river"]
        selectedWord = choice(easy_words)
    elif difficultyLevel == 6:
        medium_words = ["banana", "window", "marker", "pencil", "rocket", "planet", "father", "mother", "friend", "screen", "summer", "winter", "forest", "laptop", "galaxy"]
        selectedWord = choice(medium_words)
    elif difficultyLevel == 7:
        hard_words = ["freedom", "justice", "respect", "courage", "honesty", "backpack", "picture", "teacher", "notebook", "holiday", "library", "deserts", "animals", "emotion", "support"]
        selectedWord = choice(hard_words)

    letterList = list(selectedWord)
    shuffle(letterList)
    scrambledWord = ''.join(letterList)

    print(f"Scrambled word: {scrambledWord}")

    while not (wordAttemptCount == 3):
        wordAttemptCount += 1
        yourGuess = input("Your guess: (Press '0' to exit): ").lower()

        if yourGuess == "0":
            break

        if selectedWord == yourGuess:
            print(f"You guessed it on attempt {wordAttemptCount}. Well done!")
            break
        else:
            print(f"Incorrect. Try again ({3 - wordAttemptCount} attempts left)")
    else:
        print("You couldn't guess the word. The correct word was:", selectedWord)
