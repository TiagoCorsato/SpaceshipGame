from src.funcoes import (
    calcular_pontos,
    tomar_dano,
    jogador_perdeu,
    limitar_valor,
    inimigo_deve_atirar,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_zero():
    """Soma com zero não altera a pontuação."""
    assert calcular_pontos(50, 0) == 50


def test_tomar_dano():
    """Deve reduzir as vidas corretamente."""
    assert tomar_dano(3, 1) == 2


def test_tomar_dano_mata():
    """Deve retornar zero ao esgotar as vidas."""
    assert tomar_dano(1, 1) == 0


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_perdeu_com_vidas_negativas():
    """Deve indicar derrota com vidas negativas."""
    assert jogador_perdeu(-1) is True


def test_jogador_nao_perdeu_com_vidas():
    """Não deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o mínimo quando o valor for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o máximo quando o valor for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando já estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_limitar_valor_no_limite_exato():
    """Deve aceitar valores exatamente nos limites."""
    assert limitar_valor(0, 0, 100) == 0
    assert limitar_valor(100, 0, 100) == 100


def test_inimigo_deve_atirar_chance_zero():
    """Com chance 0, o inimigo nunca deve atirar."""
    for _ in range(100):
        assert inimigo_deve_atirar(0) is False


def test_inimigo_deve_atirar_chance_cem():
    """Com chance 100, o inimigo sempre deve atirar."""
    for _ in range(10):
        assert inimigo_deve_atirar(100) is True
