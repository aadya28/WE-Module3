import pygame
import ui
import cards

# Define constants for scene identifiers
MAIN_MENU = 0
GAMEPLAY = 1
GAME_OVER = 2

GREEN = (0, 153, 76)

# Initialize Pygame and set up the window
pygame.init()
screen_w, screen_h = ui.get_screen_size()
win = pygame.display.set_mode((screen_w * 0.8, screen_h * 0.8))
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
            win.fill(GREEN)
            player1_name, player2_name = handle_main_menu()
            current_scene = GAMEPLAY
        if current_scene == GAMEPLAY:
            win.fill(GREEN)
            handle_gameplay(player1_name, player2_name)
            current_scene = GAME_OVER
        if current_scene == GAME_OVER:
            win.fill(GREEN)
            handle_game_over()
            running = False

        # Update the display
        pygame.display.flip()
    pygame.quit()


def handle_main_menu():
    player1_name, player2_name = "a", "b"
        # ui.create_main_menu_window(win))
    print("Player 1:", player1_name)
    print("Player 2:", player2_name)
    return player1_name, player2_name


def handle_gameplay(player1_name, player2_name):
    player1_score = 0
    player2_score = 0
    ui.render_game_start(win, player1_name, player2_name)

    # game starts
    round_number = 1
    diamonds = cards.Suit("diamonds")
    draw_pile = diamonds.create_suit()
    diamonds.shuffle_deck(draw_pile)

    while round_number < 14:
        win.fill(GREEN)

        drawn_card = draw_pile.pop()
        drawn_card_name = str(drawn_card)
        round_points = drawn_card.value
        ui.render_draw_pile(win, drawn_card_name)
        ui.render_game_round(win, player1_name, player2_name, round_number, player1_score, player2_score, player2_name, round_points)
        round_number += 1


def handle_game_over():
    print("game over")


if __name__ == "__main__":
    main()
