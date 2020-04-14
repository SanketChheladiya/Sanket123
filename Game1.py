import pygame
import random
import sys

pygame.init()
WIDTH = 900
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (150,0,250)
BACKGROUNG_COLOR=(150,125,160)

player_pos = [400,300]
player_size=35
player_pos = [WIDTH/2,HEIGHT-2*player_size]

enemy_size = 35
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]
enemy_list = [enemy_pos]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False

SPEED = 15
clock = pygame.time.Clock()

score = 0

myFont = pygame.font.SysFont("monospace",35)   #35px

def detect_collision(player_pos,enemy_pos):
	p_x=player_pos[0]
	p_y=player_pos[1]

	e_x=enemy_pos[0]
	e_y=enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False

def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list)<25 and delay<0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen,BLUE,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

def update_enemy_position(enemy_list,score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] = enemy_pos[1]+SPEED
		else:
			enemy_list.pop(idx)
			score+=1
	return score

def collision_check(enemy_list,player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

while not game_over:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			x=player_pos[0]
			y=player_pos[1]
			if event.key == pygame.K_LEFT:
				x=x-player_size   #Moving block size to right and left
			elif event.key == pygame.K_RIGHT:
				x=x+player_size

			player_pos=[x,y]

	screen.fill(BACKGROUNG_COLOR)

	if detect_collision(player_pos,enemy_pos):
		game_over = True
		break
	drop_enemies(enemy_list)
	score = update_enemy_position(enemy_list,score)
	
	text = "Score is = " + str(score)
	label = myFont.render(text,1,YELLOW)
	screen.blit(label,(WIDTH-400,HEIGHT-40))
	print(score)

	if score>30 and score<=60:
		SPEED = 10
	elif score>60 and score<=120:
		SPEED = 15
	elif score>120 and score<=150:
		SPEED = 20
	else:
		SPEED = 25

	if collision_check(enemy_list,player_pos):
		game_over=True
		break

	draw_enemies(enemy_list)
	pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))

	clock.tick(30)
	pygame.display.update()
pygame.quit()
print("Your Final Score = {} \n".format(score))
sys.exit()