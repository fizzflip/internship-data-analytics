# User has 3 chances to guess the number

w_num = 7
chances = 3
won = False

for i in range(chances):
    user_number = int(input("Guess the number: "))
    if user_number == w_num:
        print("You win!")
        won = True
    elif user_number > w_num:
        print("Too high!")
    elif user_number < w_num:
        print("Too low!")

if not won:
    print("Computer wins!")