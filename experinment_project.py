import random


def result():
    while add_user_card < 21 and add_computer_card < 21:
        if add_user_card > add_computer_card:
            print("You win!!")
            break
        elif add_computer_card > add_user_card:
            print("Bust!")
            print("Computer wins!")
            break
        elif add_user_card == add_computer_card:
            print("Draw") 
            break      


def blackjack():
    global add_user_card
    global add_computer_card
    if add_user_card > 21 and add_computer_card > 21:
        print("Both Lose Game!")
        # exit(0)

    if add_user_card == 21:
        print("\nCongrats! You got 'BLACKJACK!'")
        print("Computer lose!\n\n\n")
    elif add_computer_card == 21:
        print("\nComputer has 'BLACKJACK!'")
        print("You lose!\n\n\n")
    elif add_user_card > 21:
        print("Computer wins the Game!")
        print("You Lose!\n\n")
    elif add_computer_card > 21:
        print("You Win!")
        print("Computer Lose!\n\n")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


while True:
    user_card = random.choices(cards, k=2)  # Get 2 random cards for the user
    computer_card = random.choices(cards, k=2)

    print(f"\n\nYour cards are {user_card}")
    print(f"Computer's cards are {computer_card}")

    add_user_card = sum(user_card)
    add_computer_card = sum(computer_card)
    print(f"\nYour score is {add_user_card}")
    print(f"computer's score is {add_computer_card}\n\n")
    blackjack()

    # another_card = input ("Do you want to hit? 'Y' or 'N': ")
    if input("Do you want to hit? 'Y' or 'N': ").lower() == 'y':
        user_card = random.choice(cards)
        print(user_card)
        add_user_card += user_card
        print(f"Your score is {add_user_card}")
        computer_card = random.choice(cards)
        print(computer_card)
        add_computer_card += computer_card
        print(f"Computers score is {add_computer_card}")
        blackjack()
    # else:
    #     result()
    #     exit(0)

    result()
    again_play = input("\n\n\n\nDo you want to play again 'Y' or 'N': ").lower()
    if again_play == 'y':
        continue
    else:
        exit(0)
