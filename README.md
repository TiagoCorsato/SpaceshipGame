# Spaceship Game

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Davi Cordova
- Rafael Andrade Claudino
- Tiago Alvarenga Corsato
- Nome do integrante 4

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Descreva brevemente a ideia principal do jogo.

Exemplo:

> O jogo consiste em controlar um personagem que deve coletar moedas e evitar obstáculos. O jogador ganha pontos ao coletar itens e perde vidas ao colidir com obstáculos. A partida termina quando o tempo acaba ou quando o jogador perde todas as vidas.

## Objetivo do jogador

Explique o que o jogador precisa fazer para vencer ou avançar no jogo.

Exemplo:

> O objetivo é coletar a maior quantidade possível de itens antes que o tempo acabe, evitando colisões com os obstáculos.

## Regras do jogo

- O jogador começa com **3 vidas**.
- Cada inimigo destruído concede pontos (varia por linha: 10, 20 ou 30 pts).
- Os inimigos se movem em grupo e descem ao atingir a borda da tela.
- Inimigos aleatoriamente disparam projéteis contra o jogador.
- O jogador perde uma vida ao ser atingido (com 1,5 s de invencibilidade).
- **Derrota:** vidas chegam a zero ou os inimigos alcançam a base.
- **Vitória:** todos os inimigos são eliminados.
- O recorde é salvo automaticamente em `data/recorde.txt`.


## Controles

| Tecla            | Ação                    |
|------------------|-------------------------|
| ← Seta esquerda  | Mover nave para esquerda |
| → Seta direita   | Mover nave para direita  |
| Espaço           | Atirar                   |
| Enter            | Iniciar / Reiniciar      |
| ESC ou Q         | Sair                     |

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
