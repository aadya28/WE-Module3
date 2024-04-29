import pygame
import ui
import cards
import strategies

# Define constants for scene identifiers
MAIN_MENU = 0
GAMEPLAY = 1
GAME_OVER = 2

GREEN = (0, 153, 76)

# Initialize Pygame and set up the window
pygame.init()
system_screen_w, system_screen_h = ui.get_screen_size()
screen_w, screen_h = system_screen_w * 0.8, system_screen_h * 0.8
window = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Diamonds Game")

# Initialize the clock
clock = pygame.time.Clock()

def main():
    current_scene = MAIN_MENU  # Start with the main menu scene
    player1_name = "Computer"
    player2_name = "Computer"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if current_scene == MAIN_MENU:
            window.fill(GREEN)
            player1_name, player2_name = handle_main_menu()
            current_scene = GAMEPLAY
        if current_scene == GAMEPLAY:
            window.fill(GREEN)
            handle_gameplay(player1_name, player2_name)
            current_scene = GAME_OVER
        if current_scene == GAME_OVER:
            window.fill(GREEN)
            handle_game_over()
            running = False

        pygame.display.flip()
    pygame.quit()


def handle_main_menu():
    player1_name, player2_name = "a", "b"
        # ui.create_main_menu_window(screen_w, screen_h))
    print("Player 1:", player1_name)
    print("Player 2:", player2_name)
    return player1_name, player2_name


def handle_gameplay(player1_name, player2_name):
    player1_score = 0
    player2_score = 0
    ui.render_game_start(window, player1_name, player2_name)

    # game starts
    round_number = 1
    diamonds = cards.Suit("diamonds")
    draw_pile = diamonds.create_suit()
    diamonds.shuffle_deck(draw_pile)

    while round_number < 14:
        window.fill(GREEN)

        drawn_card = draw_pile.pop()
        drawn_card_name = str(drawn_card)
        round_points = drawn_card.value
        ui.render_draw_pile(window, drawn_card_name)
        ui.render_scorecard(window, player1_name, player2_name, player1_score, player2_score)

        # Player and computer make their bids
        player1_bid = cards.Card("Spades", "10", "10")  # Placeholder, replace with actual player bid
        player2_bid = cards.Card("Hearts", "J", "11")  # Placeholder, replace with actual computer bid

        # Calculate points and determine the winner of the round
        p1_curr_round_points, p2_curr_round_points, winner = strategies.calculate_points(
            player1_name, player1_bid, player2_name, player2_bid, round_points)

        # Update scores
        player1_score += p1_curr_round_points
        player2_score += p2_curr_round_points

        ui.render_round_info(window, round_number, player1_name, p1_curr_round_points, player2_name, p2_curr_round_points, winner)
        round_number += 1


def handle_game_over():
    print("game over")


if __name__ == "__main__":
    main()
