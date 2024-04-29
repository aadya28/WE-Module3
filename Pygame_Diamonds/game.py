import pygame

import cards
import constants
import strategies
import ui

# Define constants for scene identifiers
MAIN_MENU = 0
GAMEPLAY = 1
GAME_OVER = 2

# Initialize Pygame and set up the window
pygame.init()
window = pygame.display.set_mode((constants.SCREEN_W, constants.screen_h))
pygame.display.set_caption("Diamonds Game")

# Initialize the clock
clock = pygame.time.Clock()


def main():
    current_scene = MAIN_MENU  # Start with the main menu scene
    player1_name = "Computer"
    player2_name = "Computer"
    player1_score = 0
    player2_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if current_scene == MAIN_MENU:
            window.fill(constants.GREEN)
            player1_name, player2_name = handle_main_menu()
            current_scene = GAMEPLAY
        if current_scene == GAMEPLAY:
            window.fill(constants.GREEN)
            player1_score, player2_score = handle_gameplay(player1_name, player1_score, player2_name, player2_score)
            current_scene = GAME_OVER
        if current_scene == GAME_OVER:
            window.fill(constants.GREEN)
            handle_game_over(player1_name, player1_score, player2_name, player2_score)
            running = False

        pygame.display.flip()
    pygame.quit()


def handle_main_menu():
    player1_name, player2_name = ui.create_main_menu_window(window)
    print("Player 1:", player1_name)
    print("Player 2:", player2_name)
    return player1_name, player2_name


def handle_gameplay(player1_name, player1_score, player2_name, player2_score):
    ui.render_game_start(window, player1_name, player2_name)

    # game starts
    round_number = 1
    diamonds = cards.Suit("Diamonds")
    draw_pile = diamonds.create_suit()
    diamonds.shuffle_deck(draw_pile)
    spades = cards.Suit("Spades")
    player_hand = spades.create_suit()
    hearts = cards.Suit("Hearts")
    computer_hand = hearts.create_suit()

    while round_number < 14:
        window.fill(constants.GREEN)

        drawn_card = draw_pile.pop()
        drawn_card_name = str(drawn_card)
        round_points = drawn_card.value
        ui.render_draw_pile(window, drawn_card_name)
        ui.render_scorecard(window, player1_name, player2_name, player1_score, player2_score)
        card_positions = ui.render_player_hand(window, player_hand)

        # Player and computer make their bids
        player1_bid = ui.handle_player_input(player_hand, card_positions)
        print(player1_name, ":", player1_bid)
        player2_bid = strategies.choose_computer_bid(computer_hand, player_hand, drawn_card)
        print(player2_name, ":", player2_bid)

        # Calculate points and determine the winner of the round
        p1_curr_round_points, p2_curr_round_points, winner = strategies.calculate_points(
            player1_name, player1_bid, player2_name, player2_bid, round_points)

        # Update scores
        player1_score += p1_curr_round_points
        player2_score += p2_curr_round_points

        ui.render_round_info(window, round_number, player1_name, player1_bid, p1_curr_round_points, player2_name,
                             player2_bid, p2_curr_round_points, winner)
        round_number += 1

    return player1_score, player2_score


def handle_game_over(player1_name, player1_score, player2_name, player2_score):
    ui.render_game_over(window, player1_name, player1_score, player2_name, player2_score)


if __name__ == "__main__":
    main()
