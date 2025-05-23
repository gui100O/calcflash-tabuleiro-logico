# CalcFlash: Tabuleiro Lógico 🧮🎮

## Descrição
CalcFlash é um jogo educativo que combina a mecânica de um **2048-like** com desafios matemáticos!  
A cada 3 movimentos, o jogador deve responder a uma questão matemática para continuar avançando, promovendo aprendizado enquanto se diverte.

---

## Como jogar
- Use as setas do teclado para mover as peças no tabuleiro 4x4.
- Peças com valores iguais se combinam, somando pontos.
- A cada 3 movimentos, uma questão matemática aparece.
- Responda corretamente para continuar; erros custam vidas.
- O jogo termina quando as vidas acabam ou não há mais movimentos possíveis.

---

## Tecnologias usadas
- Python 3
- [Pygame](https://www.pygame.org/news)
- [pygame_gui](https://pygame-gui.readthedocs.io/en/latest/)

---

## Arquivos principais

### calcflash.py
- Código principal do jogo, controla a interface, estados do jogo (menu, jogo, pergunta, recuperação e fim).
- Gerencia o tabuleiro, pontuação, vidas, input do usuário e integração com a lógica do jogo e geração das questões.

### game_logic.py
- Funções que manipulam o tabuleiro, movimentação e combinação das peças.
- Verifica se movimentos ainda são possíveis.

### quest_gen.py
- Gera questões matemáticas variadas (adição, subtração, multiplicação, divisão, números primos e paridade).
- Ajusta a dificuldade das questões conforme o nível.

---

## Como rodar

1. Clone o repositório ou baixe os arquivos.
2. Instale as dependências:
   ```bash
   pip install pygame pygame_gui
3. Execute o jogo:
python calcflash.py


Estrutura geral do código
CalcFlash/
│
├── calcflash.py         # Controle geral do jogo e interface
├── game_logic.py        # Lógica de movimentação e combinação das peças
└── quest_gen.py         # Geração das questões matemáticas


Controles
Setas do teclado: mover peças (esquerda, direita, cima, baixo)

Enter: confirmar resposta na pergunta

Backspace: apagar caractere na resposta

Próximos passos / melhorias
Implementar efeitos sonoros e visuais para combinações e respostas.

Salvar recordes locais.

Adicionar níveis de dificuldade configuráveis.

Melhorar a interface gráfica.

Autor
Guilherme
