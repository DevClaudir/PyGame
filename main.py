VELOCIDADE_ALIEN = 2
# Quanto menor, mais rápido

QUANTIDADE_ALIENS = 10

""""
Você também pode adicionar seus próprios personagens (dica: olhe as imagens alien.png e spaceship.png!), sua fonte, cores e sua música!
"""
import pygame  # Importa a biblioteca pygame

import random  # Importa a biblioteca random

import sys  # Importa a biblioteca sys para interagir com o sistema operacional

from pygame.locals import QUIT  # Importa a constante QUIT da biblioteca pygame.locals para criar o sistema de sair do game

# Inicializa o Pygame e configura a tela
pygame.init()  # Inicializa o pygame

setFullScreenMode = pygame.display.set_mode(
    (0, 0), pygame.FULLSCREEN)  
# Cria e Define a tela em modo tela cheia

pygame.display.set_caption(
    'Atire nos Aliens!')  # Define o título da janela do jogo

LARGURA, ALTURA = setFullScreenMode.get_size()  # geta a dimensão da tela

FONTE_FIM_JOGO = pygame.font.SysFont(
    'comicsans', 150)  # Define a fonte para o texto de fim de jogo

# Carrega e redimensiona as imagens

setNaveImage = pygame.image.load(
    'cr7.jpg').convert_alpha()  # imagem da nave espacial

setAlienImage = pygame.image.load(
    'copa-do-mundo.webp').convert_alpha()  # imagem do alienígena

NAVE = pygame.transform.scale(
    setNaveImage,
    (60, 60))  # Redimensiona a imagem da nave espacial para 50x50 pixels
ALIEN = pygame.transform.scale(
    setAlienImage,
    (55, 55))  # Redimensiona a imagem do alienígena para 50x50 pixels

# Variáveis
posicao_nave_x, posicao_nave_y = LARGURA // 2, ALTURA - 100  # Define a posição inicial da nave espacial
aliens = [(random.randint(0, LARGURA), random.randint(-ALTURA, 0))
          for _ in range(QUANTIDADE_ALIENS)
          ]  # Cria uma lista de aliens com posições aleatórias
tiros = []  # Cria uma lista vazia para armazenar os tiros

# Loop principal
clock = pygame.time.Clock() 
# Cria um objeto Clock para controlar a velocidade do jogo

fim_jogo = False  # Variável para controlar o estado do jogo (se o jogo terminou ou não)
while True:  # Loop infinito para manter o jogo em execução
  clock.tick(
      120)  # Limita a taxa de quadros do game (60 para 30fps e 120 para 60)
  
  for event in pygame.event.get():  # Obtém todos os eventos do pygame
    if event.type == QUIT or (event.type == pygame.KEYDOWN
                              and event.key == pygame.K_ESCAPE):
      pygame.quit()  # Encerra o pygame
      sys.exit()  # Encerra o programa

  if fim_jogo == False:  # Se o jogo não tiver terminado

    teclas = pygame.key.get_pressed()  # Gueta os eventos do teclado
    if teclas[pygame.K_LEFT]:  # Se a tecla esquerda estiver pressionada
      posicao_nave_x -= 3  # Move a nave pra esquerda
    if teclas[pygame.K_RIGHT]:  # Se a tecla direita estiver pressionada
      posicao_nave_x += 3  # Move a nave pra direita
    if teclas[pygame.K_SPACE]:  # Se a tecla espaço estiver pressionada
      tiros.append([posicao_nave_x, posicao_nave_y])
# Adiciona um tiro à lista de tiros

    # Atualiza os tiros e os aliens
    tiros = [[x, y - 5] for x, y in tiros if y > 0
             ]  # Move os tiros para cima e remove os tiros que saíram da tela
    aliens = [
        (x, y + VELOCIDADE_ALIEN) if y < ALTURA else
        (random.randint(0, LARGURA), 0) for x, y in aliens
    ]  # Move os aliens para baixo e gera novos aliens quando eles saem da tela

    # Verifica colisão: tiros e aliens
    for ax, ay in aliens:  # Para cada alien na lista de aliens
      for bx, by in tiros:  # Para cada tiro na lista de tiros
        if ax < bx < ax + 50 and ay < by < ay + 50:  # Se houver uma colisão entre um tiro e um alien
          if (ax, ay) in aliens:  # Se o alien ainda estiver na lista de aliens
            aliens.remove((ax, ay))  # Remove o alien da lista de aliens
            aliens.append(
                (random.randint(0, LARGURA),
                 0))  # Adiciona um novo alien na parte superior da tela
          if (bx, by) in tiros:  # Se o tiro ainda estiver na lista de tiros
            tiros.remove([bx, by])  # Remove o tiro da lista de tiros

    # Verifica colisão: nave espacial e aliens
    for ax, ay in aliens:  # Para cada alien na lista de aliens
      if posicao_nave_x < ax < posicao_nave_x + 50 and posicao_nave_y < ay < posicao_nave_y + 50:  # Se houver uma colisão entre a nave espacial e um alien
        fim_jogo = True  # Define o estado do jogo como terminado
        break  # Sai do loop

    # Desenha na tela
    setFullScreenMode.fill((4, 41, 64))  # Preenche a tela com uma cor de fundo
    setFullScreenMode.blit(
        NAVE,
        (posicao_nave_x, posicao_nave_y))  # Desenha a nave espacial na tela
    for ax, ay in aliens:  # Para cada alien na lista de aliens
      setFullScreenMode.blit(ALIEN, (ax, ay))  # Desenha o alien na tela
    for bx, by in tiros:  # Para cada tiro na lista de tiros
      pygame.draw.rect(
          setFullScreenMode, (255, 0, 0),
          (bx, by, 5,
           10))  # Desenha um retângulo vermelho representando o tiro

    pygame.display.update()  # Atualiza a tela

  else:  # Se o jogo tiver terminado
    fim_jogo_label = FONTE_FIM_JOGO.render(
        "Se fudeu nego", 1,
        (255, 255, 255))  # Renderiza o texto de fim de jogo
    setFullScreenMode.blit(fim_jogo_label, (LARGURA // 2 - fim_jogo_label.get_width() // 2,
                               ALTURA // 2 - fim_jogo_label.get_height() //
                               2))  # Desenha o texto de fim de jogo na tela

    pygame.display.update()  # Atualiza a tela
