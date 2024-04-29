import os
import pygame

import constants


def get_screen_size():
    pygame.init()
    screen_info = pygame.display.Info()
    return screen_info.current_w, screen_info.current_h


def update_screen():
    pygame.display.flip()


def transition_window():
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
    # Calculate positions for text and input fields
    text_x = constants.SCREEN_W * 0.22
    text_y = constants.screen_h * 0.3
    input_box_x = constants.SCREEN_W * 0.4
    input_box_y = constants.screen_h * 0.4
    input_width = constants.SCREEN_W * 0.3

    # Set up text surfaces
    greeting_text = constants.FONT_MEDIUM.render("Welcome to Diamonds! Please enter players!", True, constants.GOLDEN)
    player1_text = constants.FONT_SMALL.render("Player 1:", True, constants.WHITE)
    player2_text = constants.FONT_SMALL.render("Player 2:", True, constants.WHITE)

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
        pygame.draw.rect(screen, constants.WHITE, player1_input_rect, 2)
        pygame.draw.rect(screen, constants.WHITE, player2_input_rect, 2)

        # Displaying the input text entered by the players onto the screen within their respective input fields.
        screen.blit(constants.FONT_SMALL.render(player1_input, True, constants.WHITE),
                    (player1_input_rect.x + 5, player1_input_rect.y + 5))
        screen.blit(constants.FONT_SMALL.render(player2_input, True, constants.WHITE),
                    (player2_input_rect.x + 5, player2_input_rect.y + 5))

        pygame.display.flip()

    return player1_input, player2_input


def blur_background(screen):
    # Clear the screen with a blurred green background
    blurred_background = pygame.Surface(screen.get_size())
    blurred_background.fill(constants.GREEN)
    blurred_background.set_alpha(200)  # Set transparency
    screen.blit(blurred_background, (0, 0))


def render_game_start(screen, player1_name, player2_name):
    text = constants.FONT_LARGE.render("Let the game begin!", True, constants.GOLDEN)
    screen.blit(text, ((constants.SCREEN_W - text.get_width()) // 2, 100))
    vs_text = constants.FONT_MEDIUM.render(f"{player1_name} vs {player2_name}", True, constants.WHITE)
    screen.blit(vs_text, ((constants.SCREEN_W - vs_text.get_width()) // 2, 200))

    update_screen()
    transition_window()


def render_draw_pile(screen, drawn_card_name):
    # Calculate positions for draw pile and drawn card text
    draw_pile_x = constants.SCREEN_W * 0.1
    draw_pile_y = constants.screen_h * 0.15

    split_card_name = drawn_card_name.split(" ")

    # Render drawn card text
    drawn_card_text = constants.FONT_MEDIUM.render(f"{drawn_card_name} is drawn", True, constants.WHITE)
    drawn_card_text_x = (constants.SCREEN_W - drawn_card_text.get_width()) // 2
    drawn_card_text_y = constants.screen_h * 0.05
    screen.blit(drawn_card_text, (drawn_card_text_x, drawn_card_text_y))

    # Load and render the image of the drawn card
    card_image = pygame.image.load(
        os.path.join("images/diamonds", f"{split_card_name[0]}_of_{split_card_name[2].lower()}.png"))
    transformed_card_image = pygame.transform.scale(card_image, (120, 170))
    card_rect = pygame.Rect(draw_pile_x, draw_pile_y, 124, 174)
    pygame.draw.rect(screen, constants.GREY, card_rect, 3)
    # Draw the actual card image inside the border
    screen.blit(transformed_card_image, (draw_pile_x + 2, draw_pile_y + 2))

    # Update the display
    update_screen()


def render_scorecard(screen, player1_name, player2_name, player1_score, player2_score):
    # Render player names and scores
    player1_text = constants.FONT_SMALL.render(f"{player1_name}: {player1_score}", True, constants.WHITE)
    player2_text = constants.FONT_SMALL.render(f"{player2_name}: {player2_score}", True, constants.WHITE)

    # Position the texts
    text_x = constants.SCREEN_W * 0.8
    player1_y = constants.screen_h * 0.2
    player2_y = player1_y + constants.FONT_SMALL.size(player1_name)[1] + 10

    # Blit the texts onto the screen
    screen.blit(player1_text, (text_x, player1_y))
    screen.blit(player2_text, (text_x, player2_y))

    update_screen()


def render_player_hand(screen, player_hand):
    # Set up initial position for the first card
    card_x = constants.SCREEN_W * 0.075
    card_y = constants.screen_h * 0.65

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
        pygame.draw.rect(screen, constants.GREY, card_rect, 3)
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


def render_round_info(screen, round_number, player1_name, player1_bid, p1_curr_round_points,
                      player2_name, player2_bid, p2_curr_round_points, round_winner):
    blur_background(screen)

    round_text = constants.FONT_LARGE.render(f"Round {round_number}. Bids Revealed!", True, constants.GOLDEN)
    screen.blit(round_text, ((constants.SCREEN_W - round_text.get_width()) // 2, 100))

    if round_winner == "Tie":
        round_result_text = constants.FONT_MEDIUM.render("It's a tie!", True, constants.WHITE)
    else:
        round_result_text = constants.FONT_MEDIUM.render(f"{round_winner} won the round!", True, constants.WHITE)
    screen.blit(round_result_text, ((constants.SCREEN_W - round_result_text.get_width()) // 2, 200))

    # Display bids
    player1_bid_text = constants.FONT_MEDIUM.render(f"{player1_name}'s bid: {player1_bid}", True, constants.WHITE)
    player2_bid_text = constants.FONT_MEDIUM.render(f"{player2_name}'s bid: {player2_bid}", True, constants.WHITE)
    screen.blit(player1_bid_text, ((constants.SCREEN_W - player1_bid_text.get_width()) // 2, 400))
    screen.blit(player2_bid_text, ((constants.SCREEN_W - player2_bid_text.get_width()) // 2, 450))

    # Display individual scores for the round
    player1_round_score_text = constants.FONT_MEDIUM.render(f"{player1_name}: {p1_curr_round_points} points", True,
                                                            constants.WHITE)
    player2_round_score_text = constants.FONT_MEDIUM.render(f"{player2_name}: {p2_curr_round_points} points", True,
                                                            constants.WHITE)
    screen.blit(player1_round_score_text, ((constants.SCREEN_W - player1_round_score_text.get_width()) // 2, 300))
    screen.blit(player2_round_score_text, ((constants.SCREEN_W - player2_round_score_text.get_width()) // 2, 350))

    update_screen()
    transition_window()


def render_game_over(screen, player1_name, player1_score, player2_name, player2_score):
    blur_background(screen)

    # Determine the winner of the game
    if player1_score > player2_score:
        winner_text = f"{player1_name} wins the game!"
    elif player1_score < player2_score:
        winner_text = f"{player2_name} wins the game!"
    else:
        winner_text = "It's a tie!"

    # Display winner and final scores
    winner_text_surface = constants.FONT_LARGE.render(winner_text, True, constants.GOLDEN)
    screen.blit(winner_text_surface, ((constants.SCREEN_W - winner_text_surface.get_width()) // 2, 100))

    player1_score_text = constants.FONT_MEDIUM.render(f"{player1_name}: {player1_score} points", True, constants.WHITE)
    player2_score_text = constants.FONT_MEDIUM.render(f"{player2_name}: {player2_score} points", True, constants.WHITE)
    screen.blit(player1_score_text, ((constants.SCREEN_W - player1_score_text.get_width()) // 2, 250))
    screen.blit(player2_score_text, ((constants.SCREEN_W - player2_score_text.get_width()) // 2, 300))

    update_screen()
    transition_window()
