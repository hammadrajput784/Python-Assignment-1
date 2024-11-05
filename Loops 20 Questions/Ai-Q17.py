# Write a program that continues to ask for a number until the correct number is guessed.4


correct_number = 7

while True:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")
