import random

print("""\nWelcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.\n""")

print("""Please select the difficulty level: 
      1. Easy (10 chances)
      2. Medium (5 chances)
      3. Hard (3 chances)\n""")

dif_level = int(input("Enter your choice : "))

num_comp = random.randint(1, 100)

i = 0

if(dif_level == 1):
    print("\nGreat! You have selected the Easy difficulty level.")
    print("Let's start the game!\n")
    num_user = int(input("Enter Your Guess : "))
    if (num_comp == num_user):
        print("\nCongratulations! You guessed the correct number in the first attempt")
    while(num_user!= num_comp):
        i+=1
        if(i > 10):
            print("\nYou Lost :(")
            print(f"The number was {num_comp}")
            break
        if (num_user> num_comp):
            print(f"\nIncorrect! The number is less than {num_user}")
            num_user = int(input("Enter your guess: "))
            if (num_comp == num_user):
                print(f"\nCongratulations! You guessed the correct number in {i} attempts")
                break
        elif (num_user< num_comp):
            print(f"\nIncorrect! The number is more than {num_user}")
            num_user = int(input("Enter your guess: "))
            if (num_comp == num_user):
                print(f"\nCongratulations! You guessed the correct number in {i} attempts")
                break

if(dif_level == 2):
    print("\nGreat! You have selected the Medium difficulty level.")
    print("Let's start the game!\n")
    num_user = int(input("Enter Your Guess : "))
    if (num_comp == num_user):
        print("\nCongratulations! You guessed the correct number in the first attempt")
    while(num_user!= num_comp):
        i+=1
        if(i > 5):
            print("\nYou Lost :(")
            print(f"The number was {num_comp}")
            break
        if (num_user> num_comp):
            print(f"\nIncorrect! The number is less than {num_user}")
            num_user = int(input("Enter your guess: "))
            if (num_comp == num_user):
                print(f"\nCongratulations! You guessed the correct number in {i} attempts")
                break
        elif (num_user< num_comp):
            print(f"\nIncorrect! The number is more than {num_user}")
            num_user = int(input("Enter your guess: "))
            if (num_comp == num_user):
                print(f"\nCongratulations! You guessed the correct number in {i} attempts")
                break

if(dif_level == 3):
    print("\nGreat! You have selected the Hard difficulty level.")
    print("Let's start the game!\n")
    num_user = int(input("Enter Your Guess : "))
    if (num_comp == num_user):
        print("\nCongratulations! You guessed the correct number in the first attempt")
    while(num_user!= num_comp):
        i+=1
        if(i > 3):
            print("\nYou Lost :(")
            print(f"The number was {num_comp}")
            break
        if (num_user> num_comp):
            print(f"\nIncorrect! The number is less than {num_user}")
            num_user = int(input("Enter your guess: "))
            if (num_comp == num_user):
                print(f"\nCongratulations! You guessed the correct number in {i} attempts")
                break
        elif (num_user< num_comp):
            print(f"\nIncorrect! The number is more than {num_user}")
            num_user = int(input("Enter your guess: "))
            if (num_comp == num_user):
                print(f"\nCongratulations! You guessed the correct number in {i} attempts")
                break
