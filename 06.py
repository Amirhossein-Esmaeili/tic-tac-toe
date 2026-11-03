
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 700, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

BG = (18, 22, 40)
PANEL = (30, 37, 62)
WHITE = (245, 247, 255)
GRAY = (155, 165, 190)
BLUE = (70, 170, 255)
PURPLE = (160, 100, 255)
GREEN = (70, 210, 150)
RED = (255, 100, 120)
CELL = (39, 48, 76)

title_font = pygame.font.SysFont("arial", 55, bold=True)
font = pygame.font.SysFont("arial", 30, bold=True)
small_font = pygame.font.SysFont("arial", 22)
mark_font = pygame.font.SysFont("arial", 85, bold=True)

game_state = "menu"

player1 = ""
player2 = ""

current_player = "X"
winner = None
game_over = False

board = [["" for _ in range(3)] for _ in range(3)]

CELL_SIZE = 160
BOARD_X = 110
BOARD_Y = 190

input1 = pygame.Rect(150, 300, 400, 55)
input2 = pygame.Rect(150, 410, 400, 55)

active_input = 1

name1 = ""
name2 = ""

start_button = pygame.Rect(200, 530, 300, 65)
restart_button = pygame.Rect(220, 700, 260, 40)
menu_button = pygame.Rect(220, 640, 260, 45)


def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)


def draw_button(rect, text, color):
    mouse = pygame.mouse.get_pos()

    button_color = color

    if rect.collidepoint(mouse):
        button_color = tuple(min(c + 30, 255) for c in color)

    pygame.draw.rect(screen, button_color, rect, border_radius=15)
    draw_text(text, font, WHITE, rect.centerx, rect.centery)


def draw_menu():
    screen.fill(BG)

    pygame.draw.circle(screen, (35, 55, 100), (40, 80), 100)
    pygame.draw.circle(screen, (65, 40, 110), (660, 680), 120)

    pygame.draw.rect(screen, PANEL, (90, 100, 520, 550), border_radius=30)

    draw_text("TIC TAC TOE", title_font, WHITE, WIDTH // 2, 170)

    draw_text("ENTER PLAYER NAMES", small_font, GRAY, WIDTH // 2, 240)

    draw_text("PLAYER X", font, BLUE, WIDTH // 2, 280)

    color1 = BLUE if active_input == 1 else GRAY
    pygame.draw.rect(screen, CELL, input1, border_radius=12)
    pygame.draw.rect(screen, color1, input1, 2, border_radius=12)

    draw_text(name1 if name1 else "Enter name...", small_font,
              WHITE if name1 else GRAY, WIDTH // 2, 327)

    draw_text("PLAYER O", font, PURPLE, WIDTH // 2, 390)

    color2 = PURPLE if active_input == 2 else GRAY
    pygame.draw.rect(screen, CELL, input2, border_radius=12)
    pygame.draw.rect(screen, color2, input2, 2, border_radius=12)

    draw_text(name2 if name2 else "Enter name...", small_font,
              WHITE if name2 else GRAY, WIDTH // 2, 437)

    draw_button(start_button, "START GAME", GREEN)

    draw_text("Two players - One winner!", small_font, GRAY,
              WIDTH // 2, 610)


def draw_board():
    screen.fill(BG)

    pygame.draw.circle(screen, (35, 55, 100), (40, 80), 100)
    pygame.draw.circle(screen, (65, 40, 110), (660, 680), 120)

    pygame.draw.rect(screen, PANEL, (50, 35, 600, 110),
                     border_radius=20)

    if winner:
        winner_name = player1 if winner == "X" else player2
        message = f"{winner_name} WINS!"
        color = GREEN

    elif game_over:
        message = "IT'S A DRAW!"
        color = PURPLE

    else:
        current_name = player1 if current_player == "X" else player2
        message = f"{current_name}'s TURN"
        color = BLUE if current_player == "X" else PURPLE

    draw_text(message, font, color, WIDTH // 2, 75)

    draw_text(
        f"X: {player1}     |     O: {player2}",
        small_font, GRAY, WIDTH // 2, 115
    )

    pygame.draw.rect(
        screen, PANEL,
        (BOARD_X - 15, BOARD_Y - 15, 3 * CELL_SIZE + 30,
         3 * CELL_SIZE + 30),
        border_radius=20
    )

    for row in range(3):
        for col in range(3):

            x = BOARD_X + col * CELL_SIZE
            y = BOARD_Y + row * CELL_SIZE

            rect = pygame.Rect(x + 5, y + 5,
                               CELL_SIZE - 10, CELL_SIZE - 10)

            pygame.draw.rect(screen, CELL, rect, border_radius=15)

            if board[row][col] == "X":
                color = BLUE
            else:
                color = PURPLE

            if board[row][col]:
                draw_text(
                    board[row][col],
                    mark_font,
                    color,
                    rect.centerx,
                    rect.centery
                )

    if game_over:
        draw_button(menu_button, "BACK TO MENU", BLUE)
    else:
        draw_button(restart_button, "RESTART", GREEN)


def check_winner():
    for i in range(3):

        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None


def reset_game():
    global board, current_player, winner, game_over

    board = [["" for _ in range(3)] for _ in range(3)]

    current_player = "X"
    winner = None
    game_over = False


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "menu":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if input1.collidepoint(event.pos):
                    active_input = 1

                elif input2.collidepoint(event.pos):
                    active_input = 2

                elif start_button.collidepoint(event.pos):

                    if name1.strip() and name2.strip():
                        player1 = name1.strip()
                        player2 = name2.strip()

                        reset_game()
                        game_state = "game"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_TAB:
                    active_input = 2 if active_input == 1 else 1

                elif event.key == pygame.K_BACKSPACE:

                    if active_input == 1:
                        name1 = name1[:-1]
                    else:
                        name2 = name2[:-1]

                elif event.key == pygame.K_RETURN:

                    if active_input == 1:
                        active_input = 2

                    elif name1.strip() and name2.strip():
                        player1 = name1.strip()
                        player2 = name2.strip()

                        reset_game()
                        game_state = "game"

                elif event.unicode.isprintable():

                    if active_input == 1 and len(name1) < 16:
                        name1 += event.unicode

                    elif active_input == 2 and len(name2) < 16:
                        name2 += event.unicode

        elif game_state == "game":

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = event.pos

                if game_over and menu_button.collidepoint(event.pos):
                    game_state = "menu"
                    name1 = player1
                    name2 = player2

                elif not game_over and restart_button.collidepoint(event.pos):
                    reset_game()

                elif not game_over:

                    if (BOARD_X <= mouse_x < BOARD_X + 3 * CELL_SIZE
                            and BOARD_Y <= mouse_y < BOARD_Y + 3 * CELL_SIZE):

                        col = (mouse_x - BOARD_X) // CELL_SIZE
                        row = (mouse_y - BOARD_Y) // CELL_SIZE

                        if board[row][col] == "":

                            board[row][col] = current_player

                            winner = check_winner()

                            if winner:
                                game_over = True

                            elif all(
                                board[r][c] != ""
                                for r in range(3)
                                for c in range(3)
                            ):
                                game_over = True

                            else:
                                current_player = (
                                    "O" if current_player == "X" else "X"
                                )

    if game_state == "menu":
        draw_menu()

    else:
        draw_board()

    pygame.display.flip()
    clock.tick(60)
