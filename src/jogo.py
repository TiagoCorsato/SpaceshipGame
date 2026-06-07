import pygame
import random

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
    BRANCO, VERMELHO, CINZA_ESCURO,
    INIMIGO_VELOCIDADE_INICIAL, INIMIGO_DESCIDA,
    CHANCE_TIRO_INIMIGO,
)
from src.funcoes import (
    calcular_pontos, tomar_dano,
    limitar_valor, verificar_colisao,
    inimigo_deve_atirar,
)
from src.entidades import (
    criar_jogador, desenhar_jogador,
    criar_inimigos, desenhar_inimigo,
    criar_projetil_jogador, criar_projetil_inimigo, desenhar_projetil,
)


def _desenhar_hud(tela, pontos, vidas):
    """Exibe pontuação e vidas na parte inferior da tela."""
    fonte = pygame.font.SysFont("monospace", 18, bold=True)

    texto_pontos = fonte.render(f"PONTOS: {pontos}", True, BRANCO)
    texto_vidas  = fonte.render(f"VIDAS: {'v ' * vidas}", True, VERMELHO)

    tela.blit(texto_pontos, (10, ALTURA_TELA - 28))
    tela.blit(texto_vidas,  (LARGURA_TELA - texto_vidas.get_width() - 10, ALTURA_TELA - 28))

    pygame.draw.line(tela, (60, 60, 80), (0, ALTURA_TELA - 35), (LARGURA_TELA, ALTURA_TELA - 35), 1)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    jogador   = criar_jogador()
    inimigos  = criar_inimigos()
    projeteis = []

    total_inimigos      = len(inimigos)
    velocidade_inimigos = INIMIGO_VELOCIDADE_INICIAL
    direcao_inimigos    = 1

    pontos        = 0
    cooldown_tiro = 0
    rodando       = True

    while rodando:
        relogio.tick(FPS)

        # -- Eventos ------------------------------------------------------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_ESCAPE, pygame.K_q):
                    rodando = False

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

        # -- Renderização --------------------------------------------------
        tela.fill(CINZA_ESCURO)

        pygame.draw.line(tela, (60, 60, 80), (0, ALTURA_TELA - 40), (LARGURA_TELA, ALTURA_TELA - 40), 1)

        for inimigo in inimigos:
            desenhar_inimigo(tela, inimigo)
        for p in projeteis:
            desenhar_projetil(tela, p)
        desenhar_jogador(tela, jogador)
        _desenhar_hud(tela, pontos, jogador["vidas"])

        pygame.display.flip()

    pygame.quit()