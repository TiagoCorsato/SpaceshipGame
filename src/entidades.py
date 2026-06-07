import pygame
import random

from src.config import (
    LARGURA_TELA, ALTURA_TELA,
    JOGADOR_LARGURA, JOGADOR_ALTURA, JOGADOR_VELOCIDADE, JOGADOR_VIDAS,
    INIMIGO_LARGURA, INIMIGO_ALTURA,
    INIMIGO_COLUNAS, INIMIGO_LINHAS,
    INIMIGO_ESPACAMENTO_X, INIMIGO_ESPACAMENTO_Y,
    INIMIGO_ORIGEM_X, INIMIGO_ORIGEM_Y,
    INIMIGO_VELOCIDADE_INICIAL,
    PROJETIL_LARGURA, PROJETIL_ALTURA,
    PROJETIL_VELOCIDADE_JOGADOR, PROJETIL_VELOCIDADE_INIMIGO,
    VERDE, VERMELHO, AMARELO, CIANO, BRANCO,
    PONTOS_POR_LINHA,
)


# Nave do jogador

def criar_jogador():
    """Cria e retorna o dicionário que representa a nave do jogador."""
    rect = pygame.Rect(
        LARGURA_TELA // 2 - JOGADOR_LARGURA // 2,
        ALTURA_TELA - JOGADOR_ALTURA - 20,
        JOGADOR_LARGURA,
        JOGADOR_ALTURA,
    )
    return {
        "rect": rect,
        "velocidade": JOGADOR_VELOCIDADE,
        "vidas": JOGADOR_VIDAS,
        "invencivel": 0,   # frames de invencibilidade após levar dano
    }


def desenhar_jogador(tela, jogador):
    """Desenha a nave do jogador como um triângulo + base."""
    r = jogador["rect"]

    # Pisca durante invencibilidade
    if jogador["invencivel"] > 0 and (jogador["invencivel"] // 5) % 2 == 0:
        return

    cor = VERDE

    # Corpo central (retângulo)
    pygame.draw.rect(tela, cor, r, border_radius=4)

    # Canhão (retângulo fino no topo)
    canhao = pygame.Rect(r.centerx - 3, r.top - 10, 6, 12)
    pygame.draw.rect(tela, cor, canhao)

    # Asas laterais (triângulos via polígono)
    asa_esq = [
        (r.left,         r.bottom),
        (r.left - 12,    r.bottom),
        (r.left,         r.centery),
    ]
    asa_dir = [
        (r.right,        r.bottom),
        (r.right + 12,   r.bottom),
        (r.right,        r.centery),
    ]
    pygame.draw.polygon(tela, cor, asa_esq)
    pygame.draw.polygon(tela, cor, asa_dir)


# Inimigos

def criar_inimigos():
    """Cria e retorna a lista de dicionários dos inimigos em grade."""
    inimigos = []
    for linha in range(INIMIGO_LINHAS):
        for coluna in range(INIMIGO_COLUNAS):
            x = INIMIGO_ORIGEM_X + coluna * INIMIGO_ESPACAMENTO_X
            y = INIMIGO_ORIGEM_Y + linha * INIMIGO_ESPACAMENTO_Y
            rect = pygame.Rect(x, y, INIMIGO_LARGURA, INIMIGO_ALTURA)
            inimigos.append({
                "rect": rect,
                "linha": linha,
                "pontos": PONTOS_POR_LINHA[linha],
            })
    return inimigos


def _cor_por_linha(linha):
    """Retorna a cor do inimigo de acordo com a linha."""
    cores = [CIANO, AMARELO, AMARELO, VERMELHO]
    return cores[linha] if linha < len(cores) else BRANCO


def desenhar_inimigo(tela, inimigo):
    """Desenha um inimigo alienígena estilizado."""
    r = inimigo["rect"]
    cor = _cor_por_linha(inimigo["linha"])

    # Corpo
    corpo = pygame.Rect(r.x + 6, r.y + 6, r.width - 12, r.height - 10)
    pygame.draw.rect(tela, cor, corpo, border_radius=3)

    # Cabeça (semi-oval no topo)
    cabeca = pygame.Rect(r.x + 10, r.y, r.width - 20, 14)
    pygame.draw.rect(tela, cor, cabeca, border_radius=6)

    # Tentáculos / pés
    for i in range(3):
        px = r.x + 8 + i * (r.width - 16) // 2
        pygame.draw.line(tela, cor, (px, r.bottom - 4), (px - 4, r.bottom + 4), 2)
        pygame.draw.line(tela, cor, (px, r.bottom - 4), (px + 4, r.bottom + 4), 2)

    # Olhos
    pygame.draw.circle(tela, (0, 0, 0), (r.x + 14, r.y + 9), 3)
    pygame.draw.circle(tela, (0, 0, 0), (r.x + r.width - 14, r.y + 9), 3)


# Projéteis

def criar_projetil_jogador(jogador):
    """Cria um projétil disparado pelo jogador."""
    r = jogador["rect"]
    rect = pygame.Rect(
        r.centerx - PROJETIL_LARGURA // 2,
        r.top - PROJETIL_ALTURA,
        PROJETIL_LARGURA,
        PROJETIL_ALTURA,
    )
    return {
        "rect": rect,
        "velocidade": -PROJETIL_VELOCIDADE_JOGADOR,
        "dono": "jogador",
    }


def criar_projetil_inimigo(inimigo):
    """Cria um projétil disparado por um inimigo."""
    r = inimigo["rect"]
    rect = pygame.Rect(
        r.centerx - PROJETIL_LARGURA // 2,
        r.bottom,
        PROJETIL_LARGURA,
        PROJETIL_ALTURA,
    )
    return {
        "rect": rect,
        "velocidade": PROJETIL_VELOCIDADE_INIMIGO,
        "dono": "inimigo",
    }


def desenhar_projetil(tela, projetil):
    """Desenha um projétil na tela."""
    cor = AMARELO if projetil["dono"] == "jogador" else VERMELHO
    pygame.draw.rect(tela, cor, projetil["rect"], border_radius=2)
