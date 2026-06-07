import random


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)
def inimigo_deve_atirar(chance_percentual):
    """Retorna True aleatoriamente com base na chance fornecida (0–100)."""
    return random.random() * 100 < chance_percentual


def calcular_nova_velocidade(velocidade_atual, inimigos_restantes, total_inimigos):
    """Aumenta a velocidade dos inimigos conforme eles são eliminados."""
    proporcao_eliminados = 1 - (inimigos_restantes / total_inimigos)
    fator = 1 + proporcao_eliminados * 2.5
    return velocidade_atual * fator


def inimigos_chegaram_a_base(inimigos, limite_y):
    """Verifica se algum inimigo ultrapassou o limite inferior da tela."""
    for inimigo in inimigos:
        if inimigo["rect"].bottom >= limite_y:
            return True
    return False
