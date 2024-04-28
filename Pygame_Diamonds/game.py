import pygame
import ui

pygame.init()
screen_w, screen_h = ui.get_screen_size()
win = pygame.display.set_mode((screen_w * 0.8, screen_h * 0.8))
pygame.display.set_caption("Diamonds Game")


def main():
    player1_name, player2_name = ui.create_player_window(win)
    print("Player 1:", player1_name)
    print("Player 2:", player2_name)

if __name__ == "__main__":
    main()
