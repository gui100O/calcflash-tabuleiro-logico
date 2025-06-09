import pygame
import sys
import random
from game_logic import move, can_move
from quest_gen import generate_question

pygame.init()

# --- Configurações Padrão 2048 ---
WIDTH, HEIGHT = 1000, 800
GRID_WIDTH = 500
GRID_SIZE = 4
TILE_SIZE = 100
MARGIN = 10

# --- Cores Atualizadas (Tema Escuro como na imagem) ---
BACKGROUND_COLOR = (51, 53, 50)      # Cor de fundo geral (quase preto)
WHITE = (255, 255, 255)              # Texto branco
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (60, 60, 60)            # Caixa de instruções
BUTTON_COLOR = (43, 45, 42)          # Botão escuro
TITLE_COLOR = (255, 255, 255)        # Título branco
QUESTION_BOX_COLOR = (0, 0, 0)    # Caixa de pergunta escura


COLOR_MAP = {
    0: (205, 205, 205),
    2: (245, 245, 245),
    4: (230, 242, 255),
    8: (196, 224, 255),
    16: (107, 168, 255),
    32: (61, 138, 255),
    64: (10, 107, 255),
    128: (0, 82, 204),
    256: (0, 57, 166),
    512: (0, 37, 122),
    1024: (0, 25, 77),
    2048: (0, 13, 38)
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CalcFlash: Tabuleiro Lógico")

font = pygame.font.SysFont('segoeui', 32)
big_font = pygame.font.SysFont('segoeui', 48, bold=True)
small_font = pygame.font.SysFont('segoeui', 20)

MENU = 'menu'
NORMAL = 'normal'
PERGUNTA = 'pergunta'
state = MENU

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
score = 0
lives = 3
level = 1
question_text = ''
correct_answer = ''
user_answer = ''
move_counter = 0

start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 40, 200, 50)


def get_tile_color(value):
    return COLOR_MAP.get(value, COLOR_MAP[0])


def draw_menu():
    screen.fill(BACKGROUND_COLOR)
    
    # Título principal
    title = big_font.render("CalcFlash!", True, WHITE)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 130)))

    # Subtítulo
    subtitle = small_font.render("Tabuleiro Lógico", True, WHITE)
    screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 170)))

    # Caixa de instruções
    instruction_box = pygame.Rect(WIDTH // 2 - 250, 220, 500, 250)
    pygame.draw.rect(screen, LIGHT_GRAY, instruction_box, border_radius=12)

    instructions = [
        "Como jogar?",
        "Movimentação: Use as teclas  ↑ ↓ ← →  para deslizar todos",
        "os blocos na direção desejada.",
        "Resposta: Digite a resposta correta usando as teclas",
        "numéricas (0 - 9) e pressione Enter para confirmar."
    ]

    for i, line in enumerate(instructions):
        font_used = small_font if i != 0 else font
        text = font_used.render(line, True, WHITE)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, 250 + i * 30)))

    # Botão
    global start_button
    start_button = pygame.Rect(WIDTH // 2 - 60, 500, 120, 40)
    pygame.draw.rect(screen, BUTTON_COLOR, start_button, border_radius=6)
    button_text = small_font.render("Iniciar jogo", True, WHITE)
    screen.blit(button_text, button_text.get_rect(center=start_button.center))



def draw_grid(start_y):
    total_grid_width = GRID_SIZE * TILE_SIZE + (GRID_SIZE - 1) * MARGIN
    start_x = (WIDTH - total_grid_width) // 2  # centraliza horizontalmente

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            val = grid[row][col]
            x = start_x + col * (TILE_SIZE + MARGIN)
            y = start_y + row * (TILE_SIZE + MARGIN)
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, get_tile_color(val), rect, border_radius=6)
            if val:
                text_color = BLACK if val <= 4 else WHITE
                text = font.render(str(val), True, text_color)
                screen.blit(text, text.get_rect(center=rect.center))



def draw_top():
    # Limpar topo
    pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, WIDTH, 200))

    # Textos centralizados, empilhados verticalmente, com espaçamento
    spacing = 10
    y = 20

    # CalcFlash!
    title_text = big_font.render("CalcFlash!", True, TITLE_COLOR)
    title_rect = title_text.get_rect(center=(WIDTH // 2, y + title_text.get_height() // 2))
    screen.blit(title_text, title_rect)
    y += title_text.get_height() + spacing

    # Pontos
    points_text = small_font.render(f"Pontos: {score}", True, TITLE_COLOR)
    points_rect = points_text.get_rect(center=(WIDTH // 2, y + points_text.get_height() // 2))
    screen.blit(points_text, points_rect)
    y += points_text.get_height() + spacing

    # Vidas
    lives_text = small_font.render(f"Vidas: {lives}", True, TITLE_COLOR)
    lives_rect = lives_text.get_rect(center=(WIDTH // 2, y + lives_text.get_height() // 2))
    screen.blit(lives_text, lives_rect)

    return y + lives_text.get_height()  # posição final após vidas para colocar caixa pergunta


def draw_question_box(top_y):
    box_y = top_y + 15  # espaço entre vida e caixa pergunta
    box_rect = pygame.Rect(WIDTH // 2 - 350, box_y, 700, 80)
    pygame.draw.rect(screen, QUESTION_BOX_COLOR, box_rect, border_radius=12)
    pygame.draw.rect(screen, TITLE_COLOR, box_rect, 2, border_radius=12)

    line_height = 24
    words = question_text.split()
    lines = []
    line = ""
    for word in words:
        test_line = line + " " + word if line else word
        if small_font.size(test_line)[0] > box_rect.width - 20:
            lines.append(line)
            line = word
        else:
            line = test_line
    if line:
        lines.append(line)

    for i, l in enumerate(lines):
        text = small_font.render(l, True, WHITE)
        screen.blit(text, (box_rect.x + 10, box_rect.y + 10 + i * line_height))

    response = small_font.render(f"Resposta: {user_answer}", True, WHITE)
    screen.blit(response, (box_rect.x + 10, box_rect.y + 10 + len(lines) * line_height))

    return box_rect.bottom  # retorno a posição y logo abaixo da caixa


def spawn_tile():
    empty = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        grid[r][c] = 2 if random.random() < 0.9 else 4


def reset_game():
    global grid, score, lives, level, user_answer, state, question_text, correct_answer, move_counter
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    score = 0
    lives = 3
    level = 1
    user_answer = ''
    move_counter = 0
    state = NORMAL
    spawn_tile()
    spawn_tile()
    question_text, correct_answer = generate_question(level)


# --- Loop Principal ---
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == MENU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    reset_game()

        elif state == NORMAL:
            if event.type == pygame.KEYDOWN:
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
                    if move(grid, direction):
                        spawn_tile()
                        score += 4
                        move_counter += 1
                        if move_counter >= 4:
                            move_counter = 0
                            state = PERGUNTA

        elif state == PERGUNTA:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_answer.strip().lower() == correct_answer.lower():
                        level += 1
                        state = NORMAL
                    else:
                        lives -= 1
                        state = MENU if lives <= 0 else NORMAL
                    user_answer = ''
                    question_text, correct_answer = generate_question(level)
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                elif event.unicode.isdigit() or event.unicode.lower() in ['s', 'n']:
                    user_answer += event.unicode

    # Desenho separado da lógica
    if state == MENU:
        draw_menu()
    else:
        bottom_of_lives = draw_top()  # posição logo abaixo da vida
        if state == PERGUNTA:
            bottom_of_question = draw_question_box(bottom_of_lives)
        else:
            bottom_of_question = bottom_of_lives + 15 + 80  # espaço + altura da caixa

        draw_grid(bottom_of_question + 15)  # grid começa um pouco abaixo da caixa

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()