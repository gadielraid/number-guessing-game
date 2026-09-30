import random
answer = "yes"
while answer == "yes":
    secret_number = random.randint(1, 100)
    count = 0
    your_guess = 0
    while your_guess != secret_number:
        valid = False
        while not valid:
            your_guess = input("Guess a number from 1 to 100: ")
            try:
                your_guess = int(your_guess)
                if your_guess < 1 or your_guess > 100:
                    print("That is not valid input. Please enter an integer from 1 to 100.")
                else:
                    valid = True
            except ValueError:  
                print("That is not valid input. Please enter an integer from 1 to 100.")        
        count = count + 1
        print("Attempt:", count)
        if your_guess < secret_number:
            print("Too low!")       
        elif your_guess > secret_number:
            print("Too high!")         
    print("You guessed it!", "Attempts:", count)
    valid = False
    while not valid:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer == "yes" or answer == "no":
            valid = True
        else:
            print("That is not a valid input. Please enter 'yes' or 'no'.") 