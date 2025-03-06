import random

print("Welcome to Number Guessing Game")
yesorno = input("Do you wanna start? Type 'yes' if you wish to play or 'no' to exit: ").strip().lower()

if yesorno == "yes":
    def generatenum():
        num = random.randint(1, 100)  # Generate a random number
        while True:
            try:
                choose = int(input("Choose a number between 1 and 100: "))  # Convert input to integer
                if choose == num:
                    print("Congratulations! You found the number!")
                    break
                elif choose > num:
                    print("Too high! Try again.")
                else:
                    print("Too low! Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    generatenum()
else:
    print("Maybe next time! Goodbye!")
