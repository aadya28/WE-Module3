import pygame
import os

def get_screen_size():
    # Initialize Pygame
    pygame.init()

    # Get display information
    screen_info = pygame.display.Info()

    # Return screen width and height
    return screen_info.current_w, screen_info.current_h

system_screen_w, system_screen_h = get_screen_size()
screen_width, screen_height = system_screen_w * 0.8, system_screen_h * 0.8

def update_screen():
    pygame.display.flip()

def round_transition():
    waiting_for_return = True
    while waiting_for_return:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    waiting_for_return = False


def create_main_menu_window(screen):
    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Set up colors
    white = (255, 255, 255)

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
    # Set up fonts
    font_large = pygame.font.Font(None, 65)
    font_medium = pygame.font.Font(None, 50)

    # Set up colors
    white = (255, 255, 255)

    text = font_large.render("Let the game begin!", True, white)
    screen.blit(text, ((screen_width - text.get_width()) // 2, 100))
    vs_text = font_medium.render(f"{player1_name} vs {player2_name}", True, white)
    screen.blit(vs_text, ((screen_width - vs_text.get_width()) // 2, 200))

    update_screen()
    round_transition()


def render_round_info(screen, round_number, player1_name, p1_curr_round_points, player2_name,
                      p2_curr_round_points, round_winner):
    blur_background(screen)

    # Set up fonts
    font_large = pygame.font.Font(None, 65)
    font_medium = pygame.font.Font(None, 50)

    # Set up colors
    white = (255, 255, 255)

    round_text = font_large.render(f"Round {round_number}", True, white)
    screen.blit(round_text, ((screen_width - round_text.get_width()) // 2, 100))

    if round_winner == "Tie":
        round_result_text = font_medium.render("It's a tie!", True, white)
    else:
        round_result_text = font_medium.render(f"{round_winner} won the round!", True, white)
    screen.blit(round_result_text, ((screen_width - round_result_text.get_width()) // 2, 200))

    # Display individual scores for the round
    player1_round_score_text = font_medium.render(f"{player1_name}: {p1_curr_round_points} points", True, white)
    player2_round_score_text = font_medium.render(f"{player2_name}: {p2_curr_round_points} points", True, white)
    screen.blit(player1_round_score_text, ((screen_width - player1_round_score_text.get_width()) // 2, 300))
    screen.blit(player2_round_score_text, ((screen_width - player2_round_score_text.get_width()) // 2, 350))

    update_screen()
    round_transition()

def render_draw_pile(screen, drawn_card_name):
    # Set up fonts
    font = pygame.font.Font(None, 40)

    # Set up colors
    white = (255, 255, 255)

    # Calculate positions for draw pile and drawn card text
    draw_pile_x = screen_width * 0.05
    draw_pile_y = screen_height * 0.15

    split_card_name = drawn_card_name.split(" ")

    # Render drawn card text
    drawn_card_text = font.render(f"{drawn_card_name} is drawn", True, white)
    drawn_card_text_x = (screen_width - drawn_card_text.get_width()) // 2
    drawn_card_text_y = screen_height * 0.05
    screen.blit(drawn_card_text, (drawn_card_text_x, drawn_card_text_y))

    # Load and render the image of the drawn card
    card_image = pygame.image.load(os.path.join("images/diamonds", f"{split_card_name[0]}_of_{split_card_name[2].lower()}.png"))
    transformed_card_image = pygame.transform.scale(card_image, (120, 170))
    card_rect = pygame.Rect(draw_pile_x, draw_pile_y, 124, 174)
    pygame.draw.rect(screen, (0, 0, 0), card_rect, 3)
    # Draw the actual card image inside the border
    screen.blit(transformed_card_image, (draw_pile_x + 2, draw_pile_y + 2))

    # Update the display
    update_screen()

def render_scorecard(screen, player1_name, player2_name, player1_score, player2_score):
    # Set up colors
    white = (255, 255, 255)

    font = pygame.font.Font(None, 40)

    # Render player names and scores
    player1_text = font.render(f"{player1_name}: {player1_score}", True, white)
    player2_text = font.render(f"{player2_name}: {player2_score}", True, white)

    # Position the texts
    text_x = screen_width * 0.8
    player1_y =  screen_height * 0.2
    player2_y = player1_y + font.size(player1_name)[1] + 10

    # Blit the texts onto the screen
    screen.blit(player1_text, (text_x, player1_y))
    screen.blit(player2_text, (text_x, player2_y))

    update_screen()

def render_player_hand(screen, player_hand):
    # Set up initial position for the first card
    card_x = screen_width * 0.05
    card_y = screen_height * 0.65

    # Load card images
    card_images = {}
    card_positions = []  # List to store the position of each card

    for card in player_hand:
        card_name = f"{card.rank}_of_{card.suit.lower()}.png"
        card_image = pygame.image.load(os.path.join("images/spades", card_name))
        card_images[card] = pygame.transform.scale(card_image, (110, 160))  # Adjust size if needed

        # Store the position of the card
        card_positions.append((card_x, card_y))

        # Draw black border around the card
        card_rect = pygame.Rect(card_x, card_y, 114, 164)
        pygame.draw.rect(screen, (0, 0, 0), card_rect, 3)
        # Draw the actual card image inside the border
        screen.blit(card_images[card], (card_x + 2, card_y + 2))  # Adjust position to fit the border
        card_x += 70

    update_screen()
    return card_positions

def handle_player_input(player_hand, card_positions):
    # Loop for handling player input
    selecting_card = True
    selected_card = None
    while selecting_card:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if the mouse click is within the bounding box of any card
                for index, position in enumerate(card_positions):
                    card_x, card_y = position
                    card_rect = pygame.Rect(card_x, card_y, 70, 164)
                    if card_rect.collidepoint(mouse_x, mouse_y):
                        selected_card = player_hand[index]  # Get the corresponding card from the player_hand
                        selecting_card = False
                        break
    player_hand.remove(selected_card)
    update_screen()
    return selected_card
