import pygame
import os


#----------------------code for working on terminal----------
final_path = os.getcwd()
path_list = final_path.split("/")
final_path = final_path + "/" + "player"+ "/"
if path_list[-1] == "Enderman's adventure":
    pass
#----------------------code for working on terminal----------

#----------------------code for working on vs code----------
else:
    final_path = os.path.dirname(__file__)  + "/" + "player" + "/"
#----------------------code for working on vs code----------



# Animations

Player_walk_right_anim = [
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right1.png"),
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right2.png"),
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right3.png"),
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right4.png"),
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right5.png"),
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right6.png"),
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right7.png"),
    pygame.image.load(final_path + "character_walk_right" + "/character_walk_right8.png")
    ]
Player_walk_left_anim = [
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left1.png"),
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left2.png"),
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left3.png"),
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left4.png"),
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left5.png"),
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left6.png"),
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left7.png"),
    pygame.image.load(final_path + "character_walk_left" + "/character_walk_left8.png")
    ]
Player_Idle_right_anim = pygame.image.load(final_path + "character_idle_right_side.png")
Player_Idle_left_anim = pygame.image.load(final_path + "character_idle_left_side.png")

Player_Jump_anim = [
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation1.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation2.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation3.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation4.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation5.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation6.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation7.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation8.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation9.png"),
    pygame.image.load(final_path + "character_jump" +"/character_jump_animation10.png")
]


Player_activity = [
    Player_Idle_right_anim, Player_Idle_left_anim, Player_walk_right_anim, Player_walk_left_anim, Player_Jump_anim
]