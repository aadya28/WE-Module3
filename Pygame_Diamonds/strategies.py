import cards

# Function to calculate points and determine the winner of the round
def calculate_points(player1, player1_bid, player2, player2_bid, round_points):
    winner = "Tie"
    player1_value = int(player1_bid.value)
    player2_value = int(player2_bid.value)

    auction_value = int(round_points)
    if player1_value > player2_value:
        print("Player 1 wins the round!")
        winner = player1
        player1_points = auction_value
        player2_points = 0
    elif player2_value > player1_value:
        print("Player 2 wins the round!")
        winner = player2
        player1_points = 0
        player2_points = auction_value
    else:
        print("It's a tie! Both players share the points.")
        player1_points = auction_value // 2
        player2_points = auction_value // 2

    return player1_points, player2_points, winner
