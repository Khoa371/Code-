#tuankhoa
import random

def player_choice():
    choices = ["keo", "bua", "bao"]
    return input("Chon (keo/bua/bao): ").lower()

def computer_choice():
    choices = ["keo", "bua", "bao"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "Hoa!"
    elif (player == "keo" and computer == "bao") or (player == "bua" and computer == "keo") or (player == "bao" and computer == "búa"):
        return "Nguoi choi thang!"
    else:
        return "May thang!"

def main():
    print("Chao ban den choi keo bua bao!")

    while True:
        user_input = player_choice()
        if user_input not in ["keo", "bua", "bao"]:
            print("lua chon khong hop le. hay chon lai.")
            continue

        computer = computer_choice()
        print(f"May chon: {computer}")

        result = determine_winner(user_input, computer)
        print(result)

        play_again = input("Choi lai ? #(y/n): ").lower()
        if play_again != 'y':
            print("Cam on ban đa choi.!")
            break

if __name__ == "__main__":
    main()
