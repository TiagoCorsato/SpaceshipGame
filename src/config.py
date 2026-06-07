# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Space Invaders"

# Cores
PRETO       = (0,   0,   0)
BRANCO      = (255, 255, 255)
VERDE       = (0,   255, 0)
VERMELHO    = (220, 50,  50)
AMARELO     = (255, 220, 0)
CIANO       = (0,   220, 220)
CINZA_ESCURO = (30,  30,  40)

# Jogador
JOGADOR_VELOCIDADE   = 5
JOGADOR_VIDAS        = 3
JOGADOR_LARGURA      = 50
JOGADOR_ALTURA       = 30

# Projéteis
PROJETIL_VELOCIDADE_JOGADOR  = 8
PROJETIL_VELOCIDADE_INIMIGO  = 4
PROJETIL_LARGURA             = 4
PROJETIL_ALTURA              = 14

# Inimigos
INIMIGO_LARGURA     = 40
INIMIGO_ALTURA      = 30
INIMIGO_COLUNAS     = 10
INIMIGO_LINHAS      = 4
INIMIGO_ESPACAMENTO_X = 65
INIMIGO_ESPACAMENTO_Y = 55
INIMIGO_ORIGEM_X    = 60
INIMIGO_ORIGEM_Y    = 60
INIMIGO_VELOCIDADE_INICIAL = 1.5
INIMIGO_DESCIDA     = 20          # pixels que os inimigos descem ao bater na borda

# Pontuação por linha de inimigo (linha 0 = topo = mais pontos)
PONTOS_POR_LINHA = [30, 20, 20, 10]

# Chance (0–100) de um inimigo vivo atirar a cada frame
CHANCE_TIRO_INIMIGO = 0.3

# Arquivos
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"