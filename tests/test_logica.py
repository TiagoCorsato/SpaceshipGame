from src.funcoes import (
    calcular_pontos,
    tomar_dano,
    jogador_perdeu,
    limitar_valor,
    inimigo_deve_atirar,
    inimigos_chegaram_a_base,
)
from src.dados import salvar_recorde, carregar_recorde
import os
import tempfile


# ---------------------------------------------------------------------------
# calcular_pontos
# ---------------------------------------------------------------------------

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_zero():
    """Soma com zero não altera a pontuação."""
    assert calcular_pontos(50, 0) == 50


# ---------------------------------------------------------------------------
# tomar_dano
# ---------------------------------------------------------------------------

def test_tomar_dano():
    """Deve reduzir as vidas corretamente."""
    assert tomar_dano(3, 1) == 2


def test_tomar_dano_zera_vidas():
    """Deve retornar zero ao esgotar as vidas."""
    assert tomar_dano(1, 1) == 0


# ---------------------------------------------------------------------------
# jogador_perdeu
# ---------------------------------------------------------------------------

def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_perdeu_com_vidas_negativas():
    """Deve indicar derrota com vidas negativas."""
    assert jogador_perdeu(-1) is True


def test_jogador_nao_perdeu_com_vidas():
    """Não deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


# ---------------------------------------------------------------------------
# limitar_valor
# ---------------------------------------------------------------------------

def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o mínimo quando o valor for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o máximo quando o valor for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando já estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_limitar_valor_nos_limites_exatos():
    """Deve aceitar valores exatamente nos limites."""
    assert limitar_valor(0, 0, 100) == 0
    assert limitar_valor(100, 0, 100) == 100


# ---------------------------------------------------------------------------
# inimigo_deve_atirar
# ---------------------------------------------------------------------------

def test_inimigo_nao_atira_com_chance_zero():
    """Com chance 0, o inimigo nunca deve atirar."""
    for _ in range(100):
        assert inimigo_deve_atirar(0) is False


def test_inimigo_sempre_atira_com_chance_cem():
    """Com chance 100, o inimigo sempre deve atirar."""
    for _ in range(10):
        assert inimigo_deve_atirar(100) is True


# ---------------------------------------------------------------------------
# inimigos_chegaram_a_base
# ---------------------------------------------------------------------------

def _fazer_inimigo(y):
    """Cria um dicionário de inimigo simples com rect na posição y."""
    import pygame
    pygame.init()
    rect = pygame.Rect(100, y, 40, 30)
    return {"rect": rect, "linha": 0, "pontos": 10}


def test_inimigos_nao_chegaram_a_base():
    """Inimigos acima do limite não devem acionar a derrota."""
    inimigos = [_fazer_inimigo(100)]
    assert inimigos_chegaram_a_base(inimigos, 560) is False


def test_inimigos_chegaram_a_base():
    """Inimigo no limite ou abaixo deve acionar a derrota."""
    inimigos = [_fazer_inimigo(540)]
    assert inimigos_chegaram_a_base(inimigos, 560) is True


def test_lista_vazia_nao_aciona_derrota():
    """Lista vazia não deve acionar a derrota por invasão."""
    assert inimigos_chegaram_a_base([], 560) is False


# ---------------------------------------------------------------------------
# salvar_recorde / carregar_recorde
# ---------------------------------------------------------------------------

def test_salvar_e_carregar_recorde():
    """Recorde salvo deve ser carregado corretamente."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        caminho = f.name
    try:
        salvar_recorde(caminho, 250)
        assert carregar_recorde(caminho) == 250
    finally:
        os.remove(caminho)


def test_carregar_recorde_arquivo_inexistente():
    """Deve retornar 0 quando o arquivo não existir."""
    assert carregar_recorde("data/nao_existe.txt") == 0
