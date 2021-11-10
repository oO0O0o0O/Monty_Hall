import random

def main():
    # Initialize counters
    games = 0
    choose_switch = 0
    choose_stay = 0
    win_switch = 0
    win_stay = 0

    for i in range(100000):
        # Initialize game values
        first_options = [1, 2, 3]
        prize = random.choice(first_options)
        first_choice = random.choice(first_options)

        # Choose curtain to reveal
        first_options.remove(prize)
        if (first_choice in first_options):
            first_options.remove(first_choice)
        reveal = random.choice(first_options)

        # Make second choice
        second_options = [1, 2, 3]
        second_options.remove(reveal)
        second_choice = random.choice(second_options)

        # Update counters
        games += 1

        if first_choice == second_choice:
            choose_stay += 1
            if second_choice == prize:
                win_stay += 1
        else:
            choose_switch += 1
            if second_choice == prize:
                win_switch += 1
    
    print("Total games: {}".format(games))
    print("[Switch] Count: {} Wins: {} Win Rate: {:.1%}%".format(choose_switch, win_switch, win_switch/choose_switch))
    print("[Stay]   Count: {} Wins: {} Win Rate: {:.1%}%".format(choose_stay, win_stay, win_stay/choose_stay))

main()