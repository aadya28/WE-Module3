import pygame
import ui

pygame.init()
screen_w, screen_h = ui.get_screen_size()
win = pygame.display.set_mode((screen_w * 0.8, screen_h * 0.8))
pygame.display.set_caption("Diamonds Game")


def main():
    # Initialize the clock
    clock = pygame.time.Clock()

    player1_name, player2_name = ui.create_player_window(win)
    print("Player 1:", player1_name)
    print("Player 2:", player2_name)

    player1_score = 0
    player2_score = 0
    ui.render_game_start(win, player1_name, player2_name)

    # game starts
    round = 0
    while round < 3:
        ui.render_game_round(win, player1_name, player2_name, round, player1_score, player2_score, player2_name, 10)
        waiting_for_return = True
        while waiting_for_return:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting_for_return = False

        round += 1
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
