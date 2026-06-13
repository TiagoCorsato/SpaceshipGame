import pygame
import random

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
    BRANCO, VERDE, VERMELHO, AMARELO, CIANO, CINZA_ESCURO,
    CAMINHO_RECORDE,
    INIMIGO_VELOCIDADE_INICIAL, INIMIGO_DESCIDA,
    CHANCE_TIRO_INIMIGO,
)
from src.funcoes import (
    calcular_pontos, tomar_dano, jogador_perdeu,
    limitar_valor, verificar_colisao,
    inimigo_deve_atirar, inimigos_chegaram_a_base,
)
from src.entidades import (
    criar_jogador, desenhar_jogador,
    criar_inimigos, desenhar_inimigo,
    criar_projetil_jogador, criar_projetil_inimigo, desenhar_projetil,
)
from src.dados import salvar_recorde, carregar_recorde


# ---------------------------------------------------------------------------
# Utilitário de texto
# ---------------------------------------------------------------------------

def _desenhar_texto(tela, texto, tamanho, x, y, cor=BRANCO, centralizado=True):
    fonte = pygame.font.SysFont("monospace", tamanho, bold=True)
    superficie = fonte.render(texto, True, cor)
    rect = superficie.get_rect()
    if centralizado:
        rect.centerx = x
    else:
        rect.x = x
    rect.y = y
    tela.blit(superficie, rect)


# ---------------------------------------------------------------------------
# HUD
# ---------------------------------------------------------------------------

def _desenhar_hud(tela, pontos, recorde, vidas):
    """Exibe pontuação, recorde e vidas na parte inferior da tela."""
    fonte = pygame.font.SysFont("monospace", 18, bold=True)

    texto_pontos  = fonte.render(f"PONTOS: {pontos}", True, BRANCO)
    texto_recorde = fonte.render(f"RECORDE: {recorde}", True, AMARELO)
    texto_vidas   = fonte.render(f"VIDAS: {'v ' * vidas}", True, VERMELHO)

    tela.blit(texto_pontos,  (10, ALTURA_TELA - 28))
    tela.blit(texto_recorde, (LARGURA_TELA // 2 - texto_recorde.get_width() // 2, ALTURA_TELA - 28))
    tela.blit(texto_vidas,   (LARGURA_TELA - texto_vidas.get_width() - 10, ALTURA_TELA - 28))

    pygame.draw.line(tela, (60, 60, 80), (0, ALTURA_TELA - 35), (LARGURA_TELA, ALTURA_TELA - 35), 1)


# ---------------------------------------------------------------------------
# Tela inicial
# ---------------------------------------------------------------------------

def tela_inicial(tela, relogio, recorde):
    """Exibe a tela inicial e aguarda ENTER para começar."""
    tick = 0
    while True:
        relogio.tick(FPS)
        tick += 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    return True
                if evento.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False

        tela.fill(CINZA_ESCURO)
        _desenhar_texto(tela, "SPACE INVADERS", 42, LARGURA_TELA // 2, 140)
        _desenhar_texto(tela, "< > : mover nave", 20, LARGURA_TELA // 2, 260, CIANO)
        _desenhar_texto(tela, "ESPACO : atirar",  20, LARGURA_TELA // 2, 295, CIANO)
        _desenhar_texto(tela, "ESC / Q : sair",   20, LARGURA_TELA // 2, 330, CIANO)
        _desenhar_texto(tela, f"RECORDE: {recorde}", 22, LARGURA_TELA // 2, 390, AMARELO)

        if (tick // 30) % 2 == 0:
            _desenhar_texto(tela, "PRESSIONE ENTER PARA JOGAR", 22, LARGURA_TELA // 2, 470, VERDE)

        pygame.display.flip()


# ---------------------------------------------------------------------------
# Tela de fim de jogo
# ---------------------------------------------------------------------------

def tela_game_over(tela, relogio, pontos, recorde, vitoria):
    """Exibe resultado e aguarda ENTER (reiniciar) ou ESC (sair)."""
    tick = 0
    while True:
        relogio.tick(FPS)
        tick += 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    return True
                if evento.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False

        tela.fill(CINZA_ESCURO)

        titulo  = "VOCE VENCEU!" if vitoria else "GAME OVER"
        cor_titulo = VERDE if vitoria else VERMELHO
        _desenhar_texto(tela, titulo, 48, LARGURA_TELA // 2, 150, cor_titulo)
        _desenhar_texto(tela, f"PONTUACAO: {pontos}", 28, LARGURA_TELA // 2, 260, BRANCO)
        _desenhar_texto(tela, f"RECORDE:   {recorde}", 28, LARGURA_TELA // 2, 300, AMARELO)

        if (tick // 30) % 2 == 0:
            _desenhar_texto(tela, "ENTER: jogar novamente   ESC: sair", 20, LARGURA_TELA // 2, 400, CIANO)

        pygame.display.flip()


# ---------------------------------------------------------------------------
# Loop de uma partida
# ---------------------------------------------------------------------------

def _partida(tela, relogio, recorde):
    """Executa uma rodada completa. Retorna (pontos, recorde, vitoria, saiu)."""
    jogador   = criar_jogador()
    inimigos  = criar_inimigos()
    projeteis = []

    total_inimigos      = len(inimigos)
    velocidade_inimigos = INIMIGO_VELOCIDADE_INICIAL
    direcao_inimigos    = 1

    pontos        = 0
    cooldown_tiro = 0
    vitoria       = False
    rodando       = True

    while rodando:
        relogio.tick(FPS)

        # -- Eventos ------------------------------------------------------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return pontos, recorde, False, True
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_ESCAPE, pygame.K_q):
                    return pontos, recorde, False, True

        # -- Entrada do jogador -------------------------------------------
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            jogador["rect"].x -= jogador["velocidade"]
        if teclas[pygame.K_RIGHT]:
            jogador["rect"].x += jogador["velocidade"]

        jogador["rect"].x = limitar_valor(
            jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width
        )

        cooldown_tiro = max(0, cooldown_tiro - 1)
        if teclas[pygame.K_SPACE] and cooldown_tiro == 0:
            projeteis.append(criar_projetil_jogador(jogador))
            cooldown_tiro = 20

        if jogador["invencivel"] > 0:
            jogador["invencivel"] -= 1

        # -- Movimentação dos inimigos ------------------------------------
        restantes = len(inimigos)
        if restantes > 0:
            fator = 1 + (1 - restantes / total_inimigos) * 2.5
            vel = velocidade_inimigos * fator
        else:
            vel = velocidade_inimigos

        borda_atingida = any(
            (inimigo["rect"].right + direcao_inimigos * vel >= LARGURA_TELA) or
            (inimigo["rect"].left  + direcao_inimigos * vel <= 0)
            for inimigo in inimigos
        )
        if borda_atingida:
            direcao_inimigos *= -1
            for inimigo in inimigos:
                inimigo["rect"].y += INIMIGO_DESCIDA

        for inimigo in inimigos:
            inimigo["rect"].x += direcao_inimigos * vel

        # -- Tiros dos inimigos -------------------------------------------
        if inimigos and inimigo_deve_atirar(CHANCE_TIRO_INIMIGO):
            atirador = random.choice(inimigos)
            projeteis.append(criar_projetil_inimigo(atirador))

        # -- Movimentação dos projéteis ------------------------------------
        for p in projeteis:
            p["rect"].y += p["velocidade"]

        projeteis = [p for p in projeteis if 0 <= p["rect"].y <= ALTURA_TELA]

        # -- Colisão: projétil do jogador x inimigos ----------------------
        inimigos_atingidos = set()
        projeteis_usados   = set()

        for proj in [p for p in projeteis if p["dono"] == "jogador"]:
            for j, inimigo in enumerate(inimigos):
                if verificar_colisao(proj["rect"], inimigo["rect"]):
                    pontos = calcular_pontos(pontos, inimigo["pontos"])
                    inimigos_atingidos.add(j)
                    projeteis_usados.add(id(proj))
                    break

        inimigos  = [inv for k, inv in enumerate(inimigos)  if k not in inimigos_atingidos]
        projeteis = [p   for p       in projeteis            if id(p) not in projeteis_usados]

        # -- Colisão: projétil inimigo x jogador --------------------------
        if jogador["invencivel"] == 0:
            for p in [p for p in projeteis if p["dono"] == "inimigo"]:
                if verificar_colisao(p["rect"], jogador["rect"]):
                    jogador["vidas"] = tomar_dano(jogador["vidas"], 1)
                    jogador["invencivel"] = 90
                    projeteis.remove(p)
                    break

        # -- Colisão direta: inimigo x jogador ----------------------------
        for inimigo in inimigos:
            if verificar_colisao(inimigo["rect"], jogador["rect"]):
                jogador["vidas"] = 0
                break

        # -- Atualiza recorde ---------------------------------------------
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        # -- Condições de encerramento ------------------------------------
        if jogador_perdeu(jogador["vidas"]):
            rodando = False

        elif inimigos_chegaram_a_base(inimigos, ALTURA_TELA - 40):
            rodando = False

        elif not inimigos:
            vitoria = True
            rodando = False

        # -- Renderização -------------------------------------------------
        tela.fill(CINZA_ESCURO)

        pygame.draw.line(tela, (60, 60, 80), (0, ALTURA_TELA - 40), (LARGURA_TELA, ALTURA_TELA - 40), 1)

        for inimigo in inimigos:
            desenhar_inimigo(tela, inimigo)
        for p in projeteis:
            desenhar_projetil(tela, p)
        desenhar_jogador(tela, jogador)
        _desenhar_hud(tela, pontos, recorde, jogador["vidas"])

        pygame.display.flip()

    return pontos, recorde, vitoria, False


# ---------------------------------------------------------------------------
# Ponto de entrada
# ---------------------------------------------------------------------------

def executar_jogo():
    """Inicializa o Pygame e gerencia o fluxo de telas."""
    pygame.init()

    tela    = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    recorde = carregar_recorde(CAMINHO_RECORDE)

    while True:
        if not tela_inicial(tela, relogio, recorde):
            break

        pontos, recorde, vitoria, saiu = _partida(tela, relogio, recorde)
        if saiu:
            break

        if not tela_game_over(tela, relogio, pontos, recorde, vitoria):
            break

    pygame.quit()
