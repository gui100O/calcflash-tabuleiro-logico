# calcflash_game.py (com lógica: 1 questão a cada 3 movimentos)

import pygame
import pygame_gui
import sys
import random
from quest_gen import generate_question
from game_logic import combine_tiles, can_combine

# Constantes de tela
WIDTH, HEIGHT = 600, 700
TILE_SIZE = 100
GRID_SIZE = 4
MARGIN = 10

# Cores
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BLACK = (30, 30, 30)
BLUE = (50, 100, 200)
LIGHT_BLUE = (200, 230, 255)
RED = (220, 50, 50)
BACKGROUND_COLOR = (245, 250, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CalcFlash: Tabuleiro Lógico")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Fontes
font = pygame.font.SysFont('Arial', 42)
input_font = pygame.font.SysFont('Arial', 24, bold=True)
question_font = pygame.font.SysFont('Arial', 28, bold=True)
status_font = pygame.font.SysFont('Arial', 24, bold=True)

# Estados do jogo
MENU, JOGO, PERGUNTA, RECUPERACAO, FIM = range(5)
state = MENU

# Dados do jogo
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
lives = 3
score = 0
user_answer = ""
question_text = ""
correct_answer = ""
pending_points = 0
recovery_streak = 0
move_counter = 0  # Novo: contador de movimentos

# Botões
start_button = pygame_gui.elements.UIButton(pygame.Rect((WIDTH//2 - 110, 300), (220, 70)), 'Iniciar Jogo', manager)
exit_button = pygame_gui.elements.UIButton(pygame.Rect((WIDTH//2 - 110, 390), (220, 70)), 'Sair', manager)
retry_button = pygame_gui.elements.UIButton(pygame.Rect((WIDTH//2 - 110, 430), (220, 70)), 'Tentar Novamente', manager, visible=False)

# Ícone de vida
life_icon = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.polygon(life_icon, RED, [(15, 28), (28, 15), (28, 6), (24, 2), (15, 10), (6, 2), (2, 6), (2, 15)])
pygame.draw.circle(life_icon, RED, (9, 9), 8)
pygame.draw.circle(life_icon, RED, (21, 9), 8)

def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    
    grid_width = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * MARGIN
    start_x = (WIDTH - grid_width) // 2

    current_y = 10

    # Vidas centralizadas
    total_lives_width = lives * 34 - 10
    lives_x = (WIDTH - total_lives_width) // 2
    for i in range(lives):
        screen.blit(life_icon, (lives_x + i * 34, current_y))

    current_y += 40

    # Pontuação
    score_text = status_font.render(f"Pontuação: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, current_y))
    screen.blit(score_text, score_rect)

    current_y += 40

    # Questão
    if state in [PERGUNTA, RECUPERACAO]:
        question_surf = question_font.render(question_text, True, BLUE)
        question_rect = question_surf.get_rect(center=(WIDTH // 2, current_y + 20))
        rect_padding = 10
        bg_rect = pygame.Rect(
            question_rect.left - rect_padding,
            question_rect.top - rect_padding,
            question_rect.width + 2 * rect_padding,
            question_rect.height + 2 * rect_padding)
        pygame.draw.rect(screen, LIGHT_BLUE, bg_rect, border_radius=12)
        pygame.draw.rect(screen, BLUE, bg_rect, 2, border_radius=12)
        screen.blit(question_surf, question_rect)

        current_y = question_rect.bottom + 20

        # Resposta
        answer_surf = input_font.render(f"Resposta: {user_answer}", True, BLACK)
        answer_rect = answer_surf.get_rect(center=(WIDTH // 2, current_y))
        screen.blit(answer_surf, answer_rect)

        current_y = answer_rect.bottom + 20

    else:
        current_y += 20

    # Grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = grid[row][col]
            rect_x = start_x + col * (TILE_SIZE + MARGIN) + MARGIN
            rect_y = current_y + row * (TILE_SIZE + MARGIN) + MARGIN
            rect = pygame.Rect(rect_x, rect_y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, LIGHT_BLUE if value == 0 else GRAY, rect, border_radius=12)
            if value != 0:
                val_surf = font.render(str(value), True, BLACK)
                val_rect = val_surf.get_rect(center=rect.center)
                screen.blit(val_surf, val_rect)

def get_empty_cells():
    return [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c] == 0]

def spawn_tile():
    empty = get_empty_cells()
    if empty:
        r, c = random.choice(empty)
        grid[r][c] = random.choice([2, 4])

def start_game():
    global grid, lives, score, state, recovery_streak, user_answer, question_text, correct_answer, pending_points, move_counter
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    lives = 3
    score = 0
    recovery_streak = 0
    user_answer = ""
    question_text = ""
    correct_answer = ""
    pending_points = 0
    move_counter = 0
    spawn_tile()
    spawn_tile()
    state = JOGO

running = True

while running:
    time_delta = clock.tick(60) / 1000.0

    if state == MENU:
        screen.fill(BACKGROUND_COLOR)
        title_font = pygame.font.SysFont('Arial', 64, bold=True)
        title_text = title_font.render("CalcFlash!", True, BLUE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 150))
        screen.blit(title_text, title_rect)
        manager.update(time_delta)
        manager.draw_ui(screen)

    elif state in [JOGO, PERGUNTA, RECUPERACAO]:
        draw_grid()

    elif state == FIM:
        screen.fill(BACKGROUND_COLOR)
        over_font = pygame.font.SysFont('Arial', 64, bold=True)
        game_over = over_font.render("Fim de Jogo!", True, RED)
        game_over_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over, game_over_rect)
        final_score_text = font.render(f"Pontuação Final: {score}", True, BLACK)
        final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(final_score_text, final_score_rect)
        manager.update(time_delta)
        manager.draw_ui(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                start_game()
                start_button.hide()
                exit_button.hide()
                retry_button.hide()
            elif event.ui_element == exit_button:
                running = False
            elif event.ui_element == retry_button:
                retry_button.hide()
                start_game()

        elif state in [PERGUNTA, RECUPERACAO]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_answer.strip().lower() == str(correct_answer).lower():
                        state = JOGO
                    else:
                        lives -= 1
                        if lives <= 0:
                            state = FIM
                            retry_button.show()
                        else:
                            state = RECUPERACAO
                            question_text, correct_answer = generate_question(1)
                    user_answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                else:
                    user_answer += event.unicode

        elif state == JOGO and event.type == pygame.KEYDOWN:
            direction = None
            if event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'

            if direction:
                combined, moved, points = combine_tiles(grid, direction)
                if moved:
                    move_counter += 1
                    if combined:
                        score += points
                    if move_counter >= 3:
                        question_text, correct_answer = generate_question()
                        pending_points = 0
                        state = PERGUNTA
                        move_counter = 0
                    else:
                        spawn_tile()
                elif not can_combine(grid):
                    state = FIM
                    retry_button.show()

    manager.update(time_delta)

pygame.quit()
sys.exit()
