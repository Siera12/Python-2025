import random

def roll_dice():
    """Roll two dice and return their values."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def play_game():
    print("Welcome to the Dice Roll Game!")
    print("Players take turns rolling two dice. The highest score wins!")

    # Get player names
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    # Number of rounds
    rounds = int(input("Enter the number of rounds to play: "))

    # Scores
    score1 = 0
    score2 = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")

        # Player 1's turn
        input(f"{player1}, press Enter to roll the dice...")
        die1, die2 = roll_dice()
        round_score = die1 + die2
        print(f"{player1} rolled {die1} and {die2}. Total: {round_score}")
        score1 += round_score

        # Player 2's turn
        input(f"{player2}, press Enter to roll the dice...")
        die1, die2 = roll_dice()
        round_score = die1 + die2
        print(f"{player2} rolled {die1} and {die2}. Total: {round_score}")
        score2 += round_score

    # Final scores
    print("\nGame Over!")
    print(f"{player1}'s total score: {score1}")
    print(f"{player2}'s total score: {score2}")

    # Determine the winner
    if score1 > score2:
        print(f"{player1} wins!")
    elif score2 > score1:
        print(f"{player2} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
