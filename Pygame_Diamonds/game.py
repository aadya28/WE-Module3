import random
import pygame
import os

pygame.display.init()

# Get the size of the screen
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Calculate the window size to leave space for the toolbar and buttons
window_width = int(screen_width * 0.9)  # Adjust as needed
window_height = int(screen_height * 0.9)  # Adjust as needed

# Set the display mode to a window slightly smaller than the screen size
win = pygame.display.set_mode((window_width, window_height))
win.fill((0, 130, 0))

# Sets the game name
pygame.display.set_caption("Diamonds Game")


# Define the dimensions of the frame
card_frame_width = 150
card_frame_height = 200

class Suit:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit_name):
        self.cards = self.create_suit_cards(suit_name)
        self.suit_name = suit_name

    def shuffle_suit(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def create_suit_cards(self, suit_name):
        suit_cards = [Card(rank, index + 2, suit_name) for index, rank in enumerate(self.RANKS)]
        return suit_cards


class Card:
    def __init__(self, rank, bidding_value, suit):
        self.rank = rank
        self.bidding_value = bidding_value
        self.suit = suit

def display_card_image(card_path, pos_left, pos_top):
    card_image = pygame.image.load(card_path)
    transformed_image = pygame.transform.scale(card_image, (card_frame_width, card_frame_height))
    win.blit(transformed_image, (pos_left, pos_top))

# Create a suit of cards
diamonds = Suit("spades")
diamonds.shuffle_suit()

# Counter for rounds
rounds = 0

# Define the position and size of the draw pile: Rect(left, top, width, height) -> Rect
draw_pile = pygame.Rect(100, 100, 150, 200)

# Main game loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the left mouse button is clicked within the draw pile area
            if event.button == 1 and draw_pile.collidepoint(event.pos):
                # Display one card from the draw pile
                if rounds < 13 and len(diamonds.cards) > 0:
                    card = diamonds.draw_card()
                    print(f"Round {rounds + 1}: {card.rank} of {diamonds.suit_name}")
                    card_path = os.path.join('images', card.suit.lower(), f"{card.rank}_of_{card.suit.lower()}.png")
                    display_card_image(card_path, 350, 100)
                    rounds += 1
                else:
                    run = False

    # Draw the draw pile
    pygame.draw.rect(win, (255, 255, 255), draw_pile)
    card_path = os.path.join('images', "card_back.png")
    display_card_image(card_path, 100, 100)
    pygame.display.update()

pygame.display.quit()
