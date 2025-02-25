#https://github.com/samseven1234/pygame-draw-rect/blob/main/main.py#L82
#https://www.pygame.org/docs/tut/newbieguide.html?highlight=collidepoint
#   Jogo Space invaders


import pygame
import datetime
from random import randint

## Função de colisão
'''
def collision(x1, x2, y1, y2, x11, x21, y11, y21):
    if x1 <= x11 <= x2 or x1 <= x21 <= x2 and y1 <= y11 <= y2 or y1 <= y21 <= y2:
        return True
'''

## Função para detectar colisão
#
#Bug na colisão
#   chamada precisa ser feita (pos_obj_maior, tam_obj_maior, pos_obj_menor, tam_obj_menor)
#  se não o obj_menor passara pelo centro do obj_maior sem detectar colisão
def collision(pos1, size1, pos2, size2):
    if (pos1[0] <= pos2[0] <= pos1[0] + size1[0] or pos1[0] <= pos2[0] + size2[0] <= pos1[0] + size1[0]) and (pos1[1] <= pos2[1] <= pos1[1] + size1[1] or pos1[1] <= pos2[1] + size2[1] <= pos1[1] + size1[1]):
        return True
    else: return False

## Função para a movimentação do personagem
def playerControls():
    pygame.draw.circle(display, "red", (player["pos"]["x"], player["pos"]["y"]), 20)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player["pos"]["y"] -= 300 * dt
    if keys[pygame.K_s]:
        player["pos"]["y"] += 300 * dt
    if keys[pygame.K_a]:
        player["pos"]["x"] -= 300 * dt
    if keys[pygame.K_d]:
        player["pos"]["x"] += 300 * dt
    if keys[pygame.K_e]:
        shootPlayer()
    if player["pos"]["x"] < (player['size'][0] // 2):
        player["pos"]["x"] = (player['size'][0] // 2)
    elif player["pos"]["x"] > display.get_width() - (player['size'][0] // 2):
        player["pos"]["x"] = display.get_width() - (player['size'][0] // 2)
    
    if player["pos"]["y"] < (player['size'][1] // 2):
        player["pos"]["y"] = (player['size'][1] // 2)
    elif player["pos"]["y"] > display.get_height() - (player['size'][1] // 2):
        player["pos"]["y"] = display.get_height() - (player['size'][1] // 2)
    

##Função para atirar
def shootPlayer():
    timer = datetime.datetime.now()
    cooldown = datetime.timedelta(seconds=1)
    if timer - last_bullet[0] > cooldown:
        bullets_player.append([player["pos"]["x"], player["pos"]["y"] - (player['size'][1] // 2)])
        last_bullet[0] = timer

## Função para movimentação das balas
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

## Função para criar os inimigos
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

## Função para gerenciar os inimigos
def drawEnemies(enemies):
    del_enemy = -1
    rm_bullet = -1
    for k, e in enemies["pos"].items():
        coords = [e["x"], e['y']]
        pygame.draw.circle(display, "green", coords, 10)
        for bullet in bullets_player:
            if collision([coords[0] - 10, coords[1] - 10], enemies['size'], [bullet[0] -5, bullet[1] -5], [10, 10]):
                del_enemy = k
                rm_bullet = bullet
    if del_enemy != -1:
        del enemies['pos'][del_enemy]
    if rm_bullet != -1:
        bullets_player.remove(rm_bullet)

def enemyAtk():
    rm_bullet = -1
    for k, v in enemies['pos'].items():
        if randint(1, 1000) > 999:
            bullets_enemy.append([v['x'], v['y'] + (enemies['size'][1] // 2)])
    for bullet in bullets_enemy:
        pygame.draw.circle(display, "purple", (bullet[0], bullet[1]), 5)
        bullet[1] += 100 * dt
    for bullet in bullets_enemy:
        if collision([player['pos']['x'] - (player['size'][0] // 2), player['pos']['y'] - (player['size'][1] // 2)], player['size'], [bullet[0] -5, bullet[1] -5], [10, 10]):
            rm_bullet = bullet
            player['lives'] -= 1
        if bullet[1] >= display.get_height():
            rm_bullet = bullet
    if rm_bullet != -1:
        bullets_enemy.remove(rm_bullet)

def collisionBullet():
    rm_bullet = []
    for b1 in bullets_enemy:
        for b2 in bullets_player:
            if collision([b1[0] - 5, b1[1] -5], [10, 10], [b2[0] - 5, b2[1] -5], [10, 10]):
                rm_bullet.append(b1)
                rm_bullet.append(b2)
    for r in rm_bullet:
        if r in bullets_enemy:
            bullets_enemy.remove(r)
        if r in bullets_player:
            bullets_player.remove(r)

def createStructures():
    qtd_structures = randint(1,5)
    structure_size = randint(player['size'][0], int(player['size'][0] * 1.5))
    btween_structures = ((((display.get_width() // 4) * 3) - (display.get_width() // 4)) - structure_size) // qtd_structures
    xStructure_point = (display.get_width() // 4) + enemies['size'][0] + 10
    yStructure_point = ((display.get_height() // 4) * 3)
    for i in range(qtd_structures):
        new_structure = pygame.Rect(xStructure_point, yStructure_point, structure_size, 10)
        structures.append(new_structure)
        xStructure_point += structure_size + btween_structures

def structuresManage():
    for coords in structures:
        pygame.draw.rect(display, "white", coords)
    rm_bullet = -1
    w_bullet = 0
    for bullet in bullets_enemy:
        for coords in structures:
            if coords.collidepoint(bullet[0] -5, bullet[1] -5) or coords.collidepoint(bullet[0] -5, bullet[1] +5) or coords.collidepoint(bullet[0] +5, bullet[1] -5) or coords.collidepoint(bullet[0] +5, bullet[1] +5):
                rm_bullet = bullet
                w_bullet = 1
    if w_bullet == 1:
        bullets_enemy.remove(rm_bullet)
    for bullet in bullets_player:
        for coords in structures:
            if coords.collidepoint(bullet[0] -5, bullet[1] -5) or coords.collidepoint(bullet[0] -5, bullet[1] +5) or coords.collidepoint(bullet[0] +5, bullet[1] -5) or coords.collidepoint(bullet[0] +5, bullet[1] +5):
                rm_bullet = bullet
                w_bullet = 2
    if w_bullet == 2:
        bullets_player.remove(rm_bullet)


pygame.init()
display = pygame.display.set_mode((1280, 780))
clock = pygame.time.Clock()
fps = 60
rodando = True

player = {
    "pos": {
        "x" : display.get_width() // 2, 
        "y" : (display.get_height() // 10) * 9
    },
    "size": [40, 40],
    "lives": 5
}
enemies = {
    "pos" : {}, 
    "size" : [20, 20]
}

# Variaveis para gerenciar as balas
bullets_enemy = []
bullets_player = []
last_bullet = [datetime.datetime.now()]

# Chama a função para criar os inimigos
createEnemies(40)
keys = []

structures = []
createStructures()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rodando = False
        if event.type == pygame.QUIT:
            rodando = False
    
    
    dt = clock.tick(fps) / 1000
    
    display.fill("black")
    
    # Chama a função que gerencia os inimigos
    drawEnemies(enemies)
    
    if player['lives'] > 0:
        #Movimentação do player
        playerControls()
        
        ## Chama a função que gerencia as balas do player
        bulletMove()
        
        ## Chama função que gerencia as balas dos inimigos
        enemyAtk()
        
        ## Chama a função que verifica colisão entre as balas dos inimigos e player
        collisionBullet()
    
    ## Chama função que gerencia as estruturas
    structuresManage()
    
    pygame.display.update()
    pygame.display.flip()
    

pygame.quit()