import random
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


def choose_computer_bid(computer_hand, player_hand, drawn_card):
    # bid_card1 = random_bidding(computer_hand)
    # bid_card2 = same_rank_bidding(computer_hand, drawn_card)
    bid_card3 = strategy2(computer_hand, player_hand, drawn_card)
    # computer_hand.remove(bid_card1)
    # computer_hand.remove(bid_card2)
    computer_hand.remove(bid_card3)
    return bid_card3


# Function for the bidding strategy 1: Random Selection
def random_bidding(computer_hand):
    return random.choice(computer_hand)


# Function for the bidding strategy 1: Same Rank Selection
def same_rank_bidding(computer_hand, drawn_card):
    rank = drawn_card.rank

    for card in computer_hand:
        if card.rank == rank:
            return card

    return None

def strategy2(computer_hand, player_hand, drawn_card):
    """
    Determines the computer's bidding strategy based on the drawn card and the opponent's hand.

    Args:
        computer_hand (list of Card objects): The computer's hand of cards.
        player_hand (list of Card objects): The opponent's hand of cards.
        drawn_card (Card object): The card drawn from the draw pile.

    Returns:
        Card object: The computer's bid card.

    Strategy:
    - If the drawn card's rank is between 2 and Jack (inclusive), the computer attempts to bid a card with the same rank as the drawn card.
      If no such card is found in the computer's hand, it bids the highest card it has.
    - If the drawn card's rank is Queen, King, or Ace, the computer compares the highest card in its hand with the highest card in the opponent's hand.
      If the opponent's highest card is higher, the computer bids its lowest card. Otherwise, it bids the next higher rank card from the opponent's highest card.

    """
    drawn_rank = drawn_card.rank  # Rank of drawn card
    if cards.RANKS.index(drawn_rank) < 10:  # Considering ranks 2 to Jack for lower ranking cards
        # Bid a card with the same rank as the drawn card, if available
        bid_card = same_rank_bidding(computer_hand, drawn_card)
        if bid_card is None:
            # If no card with the same rank is found, bid the highest card you have
            bid_card = computer_hand[-1]
    else:
        # Determine the highest card in each player's hand
        opponent_max_rank = player_hand[-1].rank
        computer_max_rank = computer_hand[-1].rank

        # Bid the lowest card if opponent's highest card is higher
        if cards.RANKS.index(opponent_max_rank) >= cards.RANKS.index(computer_max_rank):
            bid_card = computer_hand[0]
        else:
            # Find the next higher rank from this index in computer's hand
            bid_card = next((rank for rank in computer_hand
                             if cards.RANKS.index(rank) >
                             cards.RANKS.index(opponent_max_rank)), None)

    print("Computer bids:", bid_card)
    return bid_card
