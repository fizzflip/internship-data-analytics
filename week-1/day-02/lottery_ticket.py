# FLOW OF PROGRAM
#   - User inputs a lottery number
#   - Program outputs if the user wins the lottery

lottery_winners = [256, 3456, 346, 34, 436, 23, 523, 235]
user_lottery_number = int(input("Lottery Ticket Number: "))
if user_lottery_number in lottery_winners:
    print(f"Lottery winner: {user_lottery_number}")
else:
    print("You lost all your money, fish!")
