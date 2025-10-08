import random
import time

balance = 100

def head_tail():
    global balance
    user = input("Enter your choice Head or Tail: ").strip().lower()
    if user.startswith("h"):
        user = "h"
    elif user.startswith("t"):
        user = "t"
    else:
        time.sleep(1)
        print("Enter head or tail only")
        return 
    outcomes = ["h", "t"]
    rand = random.choice(outcomes)

    print("....")
    time.sleep(1)

    if rand == user:
        print("You won rupees 20...")
        balance += 20
    else:
        print("You lost rupees 20....")
        balance -= 20

    print("Your balance:", balance)
    print("-" * 30)
    time.sleep(1)


def guess_num():
    global balance
    rand = random.randint(1, 50)
    count = 0
    print("Guess the number between 1 and 50!")

    while count < 6:
        try:
            user = int(input("Enter your choice (1-50): "))

            if user == rand:
                time.sleep(1)
                print("....")
                print("You won rupees 40!")
                balance += 40
                time.sleep(1)
                break  # ✅ stop the loop if guessed correctly

            elif user > rand:
                print("Number is high.")
            else:
                print("Number is low.")

            count += 1

            if count == 6:  # only lose when all attempts are used
                time.sleep(1)
                print("You used all attempts.")
                time.sleep(1)
                print("You lost rupees 20.")
                balance -= 20
        except ValueError:
            print("Enter a valid integer.")

    print("Your balance:", balance)
    print("-" * 30)
    time.sleep(1)

def dice_roll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    global balance
    dice_sum = d1+d2
    print("Choose a option: ")
    print("1.Greater Than 7")
    print("2.Smaller Than 7")
    print("3.Exactly 7")
    try:
        user = int(input("choose 1/2/3: "))
        if dice_sum == 7 and user == 3:
            time.sleep(1)
            print(f"You won: {20*5.7}")
            balance += 20*5.7
        elif dice_sum > 7 and user == 1:
            time.sleep(1)
            print(f"You won: {20*2.3}")
            balance += 20*2.3
        elif dice_sum < 7 and user == 2:
            time.sleep(1)
            print(f"You won: {20*2.3}")
            balance += 20*2.3
        else:
            time.sleep(1)
            print(f"You lost rupees 20")
            print(f"Result was {dice_sum}")
            time.sleep(1)
            balance -=20
    except ValueError:
        print("Enter a valid integer")
    print("Your balance is: ",balance)
    print("-" * 30)
    time.sleep(1)
        


# === Main Casino Menu ===
print("="*40)
print("🎰 Welcome to Kushal's Casino 🎰")
print("You start with 100 rupees. Each bet costs 20.")
print("Try your luck and see how much you can earn!")
print("="*40)
time.sleep(2)

while True:

    print(f"\nYour Balance: {balance} rupees")
    if balance < 20:
        print("Mininmum bet amount is 20 out of balance ")
        time.sleep(1)
        break
    print("Available games:")
    print("1. Head and Tail (odd 1:1)")
    print("2. Guess the Number (6 attempts, odd 1:2)")
    print("3. Dice 2pair (odds:2.3x and 5.7x)")
    print("4. Exit")
    try:
        game_num = int(input("Choose an option: "))

        if game_num == 1:
            head_tail()
        elif game_num == 2:
            guess_num()
        elif game_num == 3:
            dice_roll()
        elif game_num == 4:
            print("Thanks for playing! See you again...")
            time.sleep(1)
            break
        else:
            print("Invalid option, try again.")
    except ValueError:
        print("Enter a valid integer.")
