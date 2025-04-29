#https://github.com/samseven1234/pygame-draw-rect/blob/main/main.py#L82
#https://www.pygame.org/docs/tut/newbieguide.html?highlight=collidepoint
#   Jogo Space invaders

import pygame
import datetime
from random import randint
from functools import reduce

## EM TESTE
#https://www.mathcentre.ac.uk/resources/uploaded/mc-ty-scalarprod-2009-1.pdf
#https://stackoverflow.com/questions/10002918/what-is-the-need-for-normalizing-a-vector
#https://stackoverflow.com/questions/64095396/detecting-collisions-between-polygons-and-rectangles-in-pygame
#https://stackoverflow.com/questions/59553156/pygame-detecting-collision-of-a-rotating-rectangle/59553589#59553589
#https://stackoverflow.com/questions/56312503/problem-with-calculating-line-intersections/56312654#56312654

## Função para detectar colisão entre linhas
def collisionLineLine(l1_p1, l1_p2, l2_p1, l2_p2):
    
    p = pygame.math.Vector2(l1_p1)
    l1_vec = pygame.math.Vector2(l1_p2) - p
    r = l1_vec.normalize()
    q = pygame.math.Vector2(l2_p1)
    l2_vec = pygame.math.Vector2(l2_p2) - q
    s = l2_vec.normalize()
    
    rnv = pygame.math.Vector2(r[1], -r[0])
    snv = pygame.math.Vector2(s[1], -s[0])
    
    qp = q - p
    t = qp.dot(snv) / r.dot(snv)
    u = qp.dot(rnv) / r.dot(snv)
    return t > 0 and u > 0 and t * t < l1_vec.magnitude_squared() and u * u < l2_vec.magnitude_squared()

## Função para verificar se ha colisão entre um quadrado 
def collideRectLine(rect, p1, p2):
    return (collisionLineLine(p1, p2, rect.topleft, rect.bottomleft) or 
            collisionLineLine(p1, p2, rect.bottomleft, rect.bottomright) or
            collisionLineLine(p1, p2, rect.bottomright, rect.topright) or
            collisionLineLine(p1, p2, rect.topright, rect.topleft))

def collideRectPolygon(rect, polygon):
    for i in range(len(polygon) -1):
        if collideRectLine(rect, polygon[i], polygon[i + 1]):
            return True
    return False

## Função para detectar colisão
#
#Bug na colisão
#   chamada precisa ser feita (pos_obj_maior, tam_obj_maior, pos_obj_menor, tam_obj_menor)
#  se não o obj_menor passara pelo centro do obj_maior sem detectar colisão
def collision(pos1, size1, pos2, size2):
    if (pos1[0] <= pos2[0] <= pos1[0] + size1[0] or pos1[0] <= pos2[0] + size2[0] <= pos1[0] + size1[0]) and (pos1[1] <= pos2[1] <= pos1[1] + size1[1] or pos1[1] <= pos2[1] + size2[1] <= pos1[1] + size1[1]):
        return True
    else: return False

## Função para movimentação do player 
def move(s, x, y):
    speed = 2
    x *= speed
    y *= speed
    polygon = []
    
    # Verifica se o player colide com as estruturas
    for i in player['polygon']:
        polygon.append([i[0] + x, i[1] + y])
    for coords in structures:
        if collideRectPolygon(coords[0], polygon):
            player['colliding'] = True
    
    # Move o player se não houver colisão
    if not player['colliding']:
        s['x'] += x
        s['y'] += y
    player['colliding'] = False
    
    # Limita o espaço em que o player pode se mover
    if player["pos"]["x"] < display.get_width() // 4 - player['size'][0]:
        player["pos"]["x"] = display.get_width() // 4 - player['size'][0]
    elif player["pos"]["x"] > (display.get_width() // 4 * 3):
        player["pos"]["x"] = (display.get_width() // 4 * 3)
    
    if player["pos"]["y"] < (display.get_height() // 2) + player['size'][1]:
        player["pos"]["y"] = (display.get_height() // 2) + player['size'][1]
    elif player["pos"]["y"] > display.get_height():
        player["pos"]["y"] = display.get_height()
    return

## Função para desenhar o player e gerenciar os controles do player
def playerControls():
    # Cria o poligono e o desenha
    player['polygon'] = [[player['pos']['x'], player['pos']['y']], [player['pos']['x'] + player['size'][0] // 2, player['pos']['y'] - player['size'][1]], [player['pos']['x'] + player['size'][0], player['pos']['y']]]
    player['rect'] = pygame.draw.polygon(display, "red", player['polygon'])
    
    # Recebe as teclas precionadas e chama a função relacionada
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move(player["pos"], 0, -1)
        tutorial[0] = True
    if keys[pygame.K_s]:
        move(player["pos"], 0, 1)
        tutorial[1] = True
    if keys[pygame.K_a]:
        move(player["pos"], -1, 0)
        tutorial[2] = True
    if keys[pygame.K_d]:
        move(player["pos"], 1, 0)
        tutorial[3] = True
    if keys[pygame.K_e]:
        shootPlayer()
        tutorial[4] = True
    
    # Mostra a quantidade de vidas do jogador na tela
    x = 20
    y = 20
    for i in range(player['lives']):
        display.blit(heart, (x, y))
        x += 50
    
    return

## Função para o player atirar
def shootPlayer():
    # Gere o tempo do cooldown para os tiros
    timer = datetime.datetime.now()
    cooldown = datetime.timedelta(seconds=1)
    if timer - last_bullet[0] > cooldown:
        # Cria as coordenadas iniciais das balas
        bullets_player.append([player["pos"]["x"] + (player['size'][1] // 2), player["pos"]["y"] - (player['size'][1] // 2)])
        last_bullet[0] = timer
    return

## Função para movimentação das balas do player e deleta-los caso saiam da tela
def bulletMove():
    rm_bullet = -1
    if len(bullets_player) > 0:
        for b in bullets_player:
            pygame.draw.circle(display, "blue", (b[0] , b[1] + (100 * dt)), 5)
            b[1] -= (100 * dt)
        for i in range(len(bullets_player)):
            if bullets_player[i][1] < 0:
                rm_bullet = i
        if rm_bullet > -1:
            del bullets_player[rm_bullet]
    return

## Função para gerar as coordenadas dos inimigos
def createEnemies(enemyNumber):
    last_enemy = [display.get_width() // 4, display.get_height() //4]
    for e in range(1, enemyNumber + 1):
        new_x = last_enemy[0] + enemies['size'][0] + 10
        new_y = last_enemy[1] 
        if new_x >= (display.get_width() // 4) * 3:
            new_x = display.get_width() // 4 + enemies['size'][0] + 10
            new_y = last_enemy[1] + enemies['size'][1] + 10
        enemies["pos"][e] = {"x": new_x, "y" : new_y}
        last_enemy = [new_x, new_y]
    return

## Função para desenhar os inimigos e apaga-los se alguma bala do player acerta-los
def drawEnemies(enemies):
    rm_enemy = -1
    rm_bullet = -1
    # Desenha os inimigos
    for k, e in enemies["pos"].items():
        coords = [e["x"], e['y']]
        pygame.draw.circle(display, "green", coords, 10)
        # Verifica se a colisão entre balas do player e os inimigos 
        for bullet in bullets_player:
            if collision([coords[0] - 10, coords[1] - 10], enemies['size'], [bullet[0] -5, bullet[1] -5], [10, 10]):
                rm_enemy = k
                rm_bullet = bullet
    # Remove a bala e o inimigo que colidiram
    if rm_enemy != -1:
        del enemies['pos'][rm_enemy]
    if rm_bullet != -1:
        bullets_player.remove(rm_bullet)
    return

## Função para gerar as balas dos inimigos, move-las, gerir suas interações com o player e deleta-las caso saiam da tela
def enemyAtk():
    rm_bullet = -1
    
    # Cria as posições iniciais das balas dos inimigos
    for k, v in enemies['pos'].items():
        if randint(1, 1000) > 999:
            bullets_enemy.append([v['x'], v['y'] + (enemies['size'][1] // 2)])
    
    # Desenha as balas e as move 
    for bullet in bullets_enemy:
        pygame.draw.circle(display, "purple", (bullet[0], bullet[1]), 5)
        bullet[1] += 100 * dt
    
    # Verifica se a colisão com o player ou se saiu da tela e as remove
    for bullet in bullets_enemy:
        bullet_rect = pygame.Rect(bullet[0] -5, bullet[1] -5, 10, 10)
        if collideRectPolygon(bullet_rect, player['polygon']):
            rm_bullet = bullet
            player['lives'] -= 1
        if bullet[1] >= display.get_height():
            rm_bullet = bullet
    if rm_bullet != -1:
        bullets_enemy.remove(rm_bullet)
    return

## Função para verificar colisão entre as balas dos inimigos e do player e deletalas se houver colisão
def collisionBullet():
    rm_bullet = []
    # Verficia se a colição entre todas as balas
    for b1 in bullets_enemy:
        for b2 in bullets_player:
            if collision([b1[0] - 5, b1[1] -5], [10, 10], [b2[0] - 5, b2[1] -5], [10, 10]):
                rm_bullet.append(b1)
                rm_bullet.append(b2)
    
    # Remove as balas que colidiram
    for r in rm_bullet:
        if r in bullets_enemy:
            bullets_enemy.remove(r)
        if r in bullets_player:
            bullets_player.remove(r)
    return

## Função para gerar as coordenadas das estruturas
def createStructures():
    # Define a quantidade de estruturas e o tamanho delas
    qtd_structures = randint(1,5)
    structure_size = randint(player['size'][0], int(player['size'][0] * 1.5))
    
    # Espaço entre estruturas e ponto da primeira estrutura
    btween_structures = ((((display.get_width() // 4) * 3) - (display.get_width() // 4)) - structure_size) // qtd_structures
    xStructure_point = (display.get_width() // 4) + enemies['size'][0] + 10
    yStructure_point = ((display.get_height() // 4) * 3)
    
    # Cria as estruturas e adciona-as a lista de estruturas
    for i in range(qtd_structures):
        new_structure = pygame.Rect(xStructure_point, yStructure_point, structure_size, 10)
        structures.append([new_structure, 20])
        xStructure_point += structure_size + btween_structures
    return

## Função para manter as estruturas na tela e gerir as interações com as estruturas
def structuresManage():
    # Desenha as estruturas na tela
    for coords in structures:
        pygame.draw.rect(display, "white", coords[0])
    rm_bullet = -1
    w_bullet = 0
    
    # Deleta bala dos inimigos se ela atingir uma estrutura
    for bullet in bullets_enemy:
        for coords in structures:
            if coords[0].collidepoint(bullet[0] -5, bullet[1] -5) or coords[0].collidepoint(bullet[0] -5, bullet[1] +5) or coords[0].collidepoint(bullet[0] +5, bullet[1] -5) or coords[0].collidepoint(bullet[0] +5, bullet[1] +5):
                rm_bullet = bullet
                w_bullet = 1
                coords[1] -= 1
    if w_bullet == 1:
        bullets_enemy.remove(rm_bullet)
    
    # Deleta bala do player se ela atingir uma estrutura
    for bullet in bullets_player:
        for coords in structures:
            if coords[0].collidepoint(bullet[0] -5, bullet[1] -5) or coords[0].collidepoint(bullet[0] -5, bullet[1] +5) or coords[0].collidepoint(bullet[0] +5, bullet[1] -5) or coords[0].collidepoint(bullet[0] +5, bullet[1] +5):
                rm_bullet = bullet
                w_bullet = 2
                coords[1] -= 1
    if w_bullet == 2:
        bullets_player.remove(rm_bullet)
    
    # Deleta struturas se a mesma foi atingida 20 vezes
    rm_structure = -1
    structure_life = 0
    for coords in structures:
        if coords[1] < 1:
            rm_structure = coords[0]
            structure_life = coords[1]
    if rm_structure != -1:
        structures.remove([rm_structure, structure_life])
    return

## Função do background
def createBackground():
    x = randint(1, display.get_width())
    y = randint(1, display.get_height())
    for i in range(100):
        stars.append((x, y))
        x = randint(1, display.get_width())
        y = randint(1, display.get_height())
    return

def background():
    display.fill("black")
    for i in stars:
        pygame.draw.circle(display, "white", i, randint(1, 3))

## Função para desenhar os controles
def displayTutorial(y, text_list):
    for i in text_list:
        game_font.render_to(display, (40, y), i, "white")
        y += 24
    return

## Função que faz a tela de gameover
def gameover():
    gameover_font.render_to(display, (display.get_width() // 3, display.get_height() // 2), "GAME OVER", "white")
    retry_rect = pygame.draw.rect(display, "white", (display.get_width() // 2 - 35, display.get_height() // 2 + 100, 70, 30))
    game_font.render_to(display, (display.get_width() // 2 -30, display.get_height() // 2 + 104), "Retry", "black")
    quit_rect = pygame.draw.rect(display, "white", (display.get_width() // 2 - 35, display.get_height() // 2 + 140, 70, 30))
    game_font.render_to(display, (display.get_width() // 2 -28, display.get_height() // 2 + 144), "Quit", "black")
    if retry_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        enemies["pos"] = {}
        createEnemies(40)
        createStructures()
        player['pos']["x"] = display.get_width() // 2
        player['pos']["y"] = (display.get_height() // 10) * 9
        player['lives'] = 3
    if quit_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        return False
    return True

pygame.init()
display = pygame.display.set_mode((1280, 780)) 
pygame.display.set_caption("Space Invaders") # Muda o nome da janela para o nome do jogo
clock = pygame.time.Clock()
fps = 60
heart = pygame.image.load("heart.png") # Variavel da imagem do coração
heart = pygame.transform.scale(heart, (40, 40)) # Variavel da imagem do coração redimensionada
rodando = True

# Variaveis do jogador
player = {
    "pos": {
        "x" : display.get_width() // 2, 
        "y" : (display.get_height() // 10) * 9
    },
    "size": [40, 40],
    "lives": 3,
    "colliding": False
}

# Variaveis dos inimigos
enemies = {
    "pos" : {}, 
    "size" : [20, 20]
}

game_font = pygame.freetype.SysFont('Comic Sans MS', 24) # Variavel da fonte menor
gameover_font = pygame.freetype.SysFont('Comic Sans MS', 70) # Variavel da fonte maior
controls_str = ["Controls:", "W - Move up", "S - Move down", "A - Move left", "D - Move rigth", "E - Shoot"] # Variavel dos textos do tutorial
tutorial = [False, False, False, False, False] # Variavel que guarda se as teclas ja foram precionadas 

bullets_enemy = [] # Lista que guardará as coordenadas das balas dos inimigos
bullets_player = [] # Lista que guardará as coordenadas das balas do jogador
last_bullet = [datetime.datetime.now()] # variavel que guardará a hora em que a ultima bala foi atirada pelo jogador

structures = [] # Lista que guardará as coordenadas das estruturas
stars = [] # Lista que guardará as coordenadas das estrelas

createEnemies(40) # Cria os inimigos
createStructures() # Cria as estruturas
createBackground() # Cria as estrelas

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rodando = False
        if event.type == pygame.QUIT:
            rodando = False
    
    dt = clock.tick(fps) / 1000
    background()
    
    if player['lives'] > 0:
        drawEnemies(enemies) ## Chama a função que gerencia os inimigos
        playerControls() ## Controles do jogador
        bulletMove() ## Chama a função que gerencia as balas do player
        enemyAtk() ## Chama função que gerencia as balas dos inimigos
        collisionBullet()## Chama a função que verifica colisão entre as balas dos inimigos e player
        structuresManage() ## Chama função que gerencia as estruturas
    else:
        # Reseta o jogo
        enemies['pos'] = {}
        bullets_enemy = []
        bullets_player = []
        structures = []
        rodando = gameover()
    
    if not all(tutorial):
        displayTutorial(600, controls_str)
    
    pygame.display.update()
    pygame.display.flip()

pygame.quit()