import pygame
import cards

def get_screen_size():
    # Initialize Pygame
    pygame.init()

    # Get display information
    screen_info = pygame.display.Info()

    # Return screen width and height
    return screen_info.current_w, screen_info.current_h

def update_screen():
    pygame.display.flip()

def create_player_window(screen):
    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Set up colors
    white = (255, 255, 255)
    green = (0, 153, 76)  # Adjusted to green color

    # Get screen dimensions
    screen_width, screen_height = get_screen_size()

    # Calculate positions for text and input fields
    text_x = screen_width * 0.27
    text_y = screen_height * 0.25
    input_box_x = screen_width * 0.4
    input_box_y = screen_height * 0.4
    input_width = screen_width * 0.3

    # Set up text surfaces
    greeting_text = font.render("Welcome to Diamonds! Please enter players!", True, (245, 206, 11))
    player1_text = font.render("Player 1:", True, white)
    player2_text = font.render("Player 2:", True, white)

    # Create input fields
    player1_input_rect = pygame.Rect(input_box_x, input_box_y, input_width, 50)
    player2_input_rect = pygame.Rect(input_box_x, input_box_y + 100, input_width, 50)
    player1_input = ""
    player2_input = ""

    # Main loop for player input window
    inputting = True
    while inputting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inputting = False
                elif event.key == pygame.K_BACKSPACE:
                    if player1_input_rect.collidepoint(pygame.mouse.get_pos()):
                        player1_input = player1_input[:-1]
                    elif player2_input_rect.collidepoint(pygame.mouse.get_pos()):
                        player2_input = player2_input[:-1]
                else:
                    if player1_input_rect.collidepoint(pygame.mouse.get_pos()):
                        player1_input += event.unicode
                    elif player2_input_rect.collidepoint(pygame.mouse.get_pos()):
                        player2_input += event.unicode

        # Fill the screen with a background color
        screen.fill(green)  # Changed to green color

        # Draw text surfaces
        screen.blit(greeting_text, (text_x, text_y))
        screen.blit(player1_text, (input_box_x - player1_text.get_width() - 50, input_box_y + 10))
        screen.blit(player2_text, (input_box_x - player2_text.get_width() - 50, input_box_y + 110))

        # Draw input fields
        pygame.draw.rect(screen, white, player1_input_rect, 2)
        pygame.draw.rect(screen, white, player2_input_rect, 2)

        # Displaying the input text entered by the players onto the screen within their respective input fields.
        screen.blit(font.render(player1_input, True, white), (player1_input_rect.x + 5, player1_input_rect.y + 5))
        screen.blit(font.render(player2_input, True, white), (player2_input_rect.x + 5, player2_input_rect.y + 5))

        update_screen()

    return player1_input, player2_input

def blur_background(screen):
    green = (0, 153, 76)
    # Clear the screen with a blurred green background
    blurred_background = pygame.Surface(screen.get_size())
    blurred_background.fill(green)
    blurred_background.set_alpha(200)  # Set transparency
    screen.blit(blurred_background, (0, 0))

def render_game_start(screen, player1_name, player2_name):
    blur_background(screen)

    screen_width, screen_height = get_screen_size()
    # Set up fonts
    font_large = pygame.font.Font(None, 72)
    font_medium = pygame.font.Font(None, 36)

    # Set up colors
    white = (255, 255, 255)

    text = font_large.render("Let the game begin!", True, white)
    screen.blit(text, ((screen_width - text.get_width()) // 2, 100))
    vs_text = font_medium.render(f"{player1_name} vs {player2_name}", True, white)
    screen.blit(vs_text, ((screen.get_width() - vs_text.get_width()) // 2, 200))

    update_screen()

def render_game_round(screen, player1_name, player2_name, round_number, player1_score, player2_score, round_winner, round_points):
    blur_background(screen)

    screen_width, screen_height = get_screen_size()
    # Set up fonts
    font_large = pygame.font.Font(None, 72)
    font_medium = pygame.font.Font(None, 36)

    # Set up colors
    white = (255, 255, 255)
    green = (0, 153, 76)
    black = (0, 0, 0)

    round_text = font_large.render(f"Round {round_number}", True, white)
    screen.blit(round_text, ((screen.get_width() - round_text.get_width()) // 2, 100))
    score_text = font_medium.render(f"{player1_name}: {player1_score}   {player2_name}: {player2_score}", True, white)
    screen.blit(score_text, ((screen.get_width() - score_text.get_width()) // 2, 200))
    round_result_text = font_medium.render(f"{round_winner} won {round_points} points!", True, white)
    screen.blit(round_result_text, ((screen.get_width() - round_result_text.get_width()) // 2, 300))

    update_screen()
