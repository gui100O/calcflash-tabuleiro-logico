import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tela Game Over")

# Cores
vermelho = (255, 0, 0)
preto_transparente = (0, 0, 0, 180)  # Transparência sobre a imagem

# Carregar imagem de fundo
fundo = pygame.image.load("fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))

# Fonte
fonte = pygame.font.SysFont(None, 100)
texto = fonte.render("GAME OVER", True, vermelho)

# Criar superfície de sobreposição com transparência
overlay = pygame.Surface((largura, altura), pygame.SRCALPHA)
overlay.fill(preto_transparente)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Desenhar fundo
    tela.blit(fundo, (0, 0))

    # Aplicar camada escura transparente
    tela.blit(overlay, (0, 0))

    # Centralizar texto
    texto_rect = texto.get_rect(center=(largura / 2, altura / 2))
    tela.blit(texto, texto_rect)

    # Atualizar tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()


