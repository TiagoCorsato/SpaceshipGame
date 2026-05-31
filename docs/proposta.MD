# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1:
- Nome 2:
- Nome 3:
- Nome 4:

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Jogo de nave espacial com eliminação de ondas de inimigos, inspirado no clássico Space Invaders.

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> Na tela aparecem a nave do jogador (parte inferior da tela), ondas de inimigos alienígenas organizados em linhas e colunas (parte superior) e os projéteis disparados por ambos os lados. O jogador controla uma nave espacial que se move lateralmente e dispara projéteis para cima. Os inimigos se movem em grupo horizontalmente, descendo um nível ao tocarem as bordas da tela, e alguns deles podem atirar de volta no jogador. O desafio é eliminar todos os inimigos antes que eles alcancem a base, enquanto se desvia dos projéteis inimigos.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Destruir todos os inimigos alienígenas de cada fase, acumulando a maior pontuação possível e sobrevivendo pelo maior tempo possível.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O jogador inicia com uma quantidade fixa de vidas.
- Regra 2: A nave do jogador pode se mover apenas horizontalmente.
- Regra 3: O jogador pode disparar projéteis para destruir os inimigos.
- Regra 4: Os inimigos se movimentam em grupo; ao atingirem uma borda, descem um nível.
- Regra 5: Se um projétil do jogador atingir um inimigo, o inimigo é removido e o jogador ganha pontos.
- Regra 6: Se um projétil inimigo atingir a nave, o jogador perde uma vida.
- Regra 7: O jogo termina quando o jogador perder todas as vidas ou os inimigos alcançarem a parte inferior da tela.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> O jogador vence uma fase ao destruir todos os inimigos presentes nela. Em uma versão com múltiplas fases, o jogo é vencido ao concluir todas as fases disponíveis.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> O jogador perde se ficar sem vidas ou se os inimigos alcançarem a base (parte inferior da tela). O jogo também é encerrado quando o jogador optar por sair.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Uma nave espacial controlada pelo jogador, posicionada na parte inferior da tela, capaz de se mover para a esquerda e para a direita.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Inimigos alienígenas organizados em linhas e colunas que se movem em grupo horizontalmente e descem ao tocar as bordas da tela. Alguns inimigos disparam projéteis em direção ao jogador.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Projéteis disparados pela nave do jogador para destruir os inimigos. Cada inimigo destruído concede pontos ao jogador.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa com uma quantidade fixa de vidas. A pontuação aumenta a cada inimigo destruído. O jogo registra o recorde de pontuação em arquivo.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Seta para a esquerda: mover a nave para a esquerda
- Seta para a direita: mover a nave para a direita
- Espaço: atirar
- ESC ou Q: sair do jogo
- ENTER: iniciar ou reiniciar o jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela, cores e velocidades;
- `src/entidades.py`: contém as classes `Nave`, `Inimigo` e `Projetil`;
- `src/dados.py`: contém funções de leitura e escrita do recorde (`highscore.txt`);
- `assets/`: pasta com imagens, sons e fontes.

## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

- imagens/sprites obtidas de banco de imagens gratuito;
- sons gratuitos (tiros, explosões, música de fundo);
- fonte personalizada para exibição de pontuação e menus;
- tutoriais usados apenas como referência de conceito.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: implementar a movimentação coordenada dos inimigos em grupo;
- Dificuldade 2: controlar colisões entre tiros, inimigos e jogador;
- Dificuldade 3: gerenciar vários objetos em movimento ao mesmo tempo.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá uma nave controlável pelo jogador com movimentação lateral, disparo de projéteis, grupo de inimigos com movimentação padrão, detecção de colisão, sistema de vidas, sistema de pontuação, condição de vitória e de derrota, tela de início, tela de game over e possibilidade de reiniciar o jogo.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: sons — efeitos sonoros para tiros, explosões e música de fundo;
- Melhoria 2: múltiplas fases com aumento progressivo de velocidade e quantidade de inimigos;
- Melhoria 3: ranking de pontuação salvo em arquivo;
- Melhoria 4: animações de explosão ao destruir inimigos;
- Melhoria 5: menu de pausa durante a partida.
