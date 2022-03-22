import pygame, sys, os
from animations import Player_activity

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()

# Game constants
WIDTH = 1080
HEIGHT = 600

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BACKGROUND_COLOR = (198, 198, 198) # #c6c6c6


PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 1
PLATFORM_VER_GAP = 100
PLATFORM_HOR_GAP = 40
GAP = 50

# Player's physical and movement properties
Player_width = 64
Player_height = 64
Player_jump_status = False # initially
Player_go_up = True # initially
Player_jump_height = 200
Player_x_speed = 10
Player_y_speed = 20
Player_J_count = 9
Max_J_count = 9

# Player display animation properties----------
Player_activity_num = 0 # facing right initially
Player_facing = 0 # right initially

# the variables below control the animations
Player_wr_no = 0 # initially
Player_wl_no = 0 # initially
Player_jump_no = 0 # initially
#-----------------------------------

FPS = 30


PLATFORM_0 = pygame.Rect(0, HEIGHT -100 , WIDTH, PLATFORM_HEIGHT+20) # Ball initially on platform 0

PLATFORM_1 = pygame.Rect(PLATFORM_0.x , PLATFORM_0.y - PLATFORM_VER_GAP- PLATFORM_HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)

PLATFORM_2 = pygame.Rect(PLATFORM_1.x + PLATFORM_WIDTH + PLATFORM_HOR_GAP + GAP, PLATFORM_1.y - PLATFORM_VER_GAP- PLATFORM_HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)

PLATFORM_3 = pygame.Rect(PLATFORM_2.x + PLATFORM_WIDTH + PLATFORM_HOR_GAP + GAP, PLATFORM_2.y - PLATFORM_VER_GAP- PLATFORM_HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)

PLATFORM_4 = pygame.Rect(PLATFORM_3.x + PLATFORM_WIDTH + PLATFORM_HOR_GAP + GAP, PLATFORM_2.y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

PLATFORM_5 = pygame.Rect(PLATFORM_2.x, PLATFORM_3.y - PLATFORM_VER_GAP- PLATFORM_HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)

LIST_PLATFORMS = [PLATFORM_0 ,PLATFORM_1, PLATFORM_2, PLATFORM_3, PLATFORM_4, PLATFORM_5]


class Player():
    def __init__(self):
        self.x = PLATFORM_0.x + Player_width
        self.y = PLATFORM_0.y - Player_height
        self.platform = PLATFORM_0

    def hor_movement(self, keys_pressed):

        global Player_jump_status
        global Player_go_up
        global Player_activity_num
        global Player_facing

        if keys_pressed[pygame.K_a] and self.x > 0:
            self.x -= Player_x_speed
            Player_activity_num = 3
            Player_facing = 1
            if not(self.x in range(self.platform.x - Player_width, self.platform.x + self.platform.width)):
                # code for fall down from the platform
                if Player_jump_status == True: # already in jumping motion
                    return
                else: # Player_jump_status = False
                    Player_jump_status = True # fall down code
                    Player_go_up = False
                    Player_activity_num = Player_facing
        elif keys_pressed[pygame.K_d] and self.x + Player_width < WIDTH:
            self.x += Player_x_speed
            Player_activity_num = 2
            Player_facing = 0
            if not(self.x in range(self.platform.x - Player_width, self.platform.x + self.platform.width)):
                # code for fall down from the platform
                if Player_jump_status == True: # already in jumping motion
                    return
                else: # Player_jump_status = False
                    Player_jump_status = True # fall down code
                    Player_go_up = False
                    Player_activity_num = Player_facing
        else:
            Player_activity_num = Player_facing


    def ver_movement(self, key):

        global Player_jump_status
        global Player_go_up
        global Player_J_count
        global Player_activity_num
        global Player_facing

        if key == 1:
            Player_jump_status = True # go for a jump
            Player_go_up = True
        else: # if key == 0
            if Player_jump_status == True:
                if Player_go_up == True and Player_J_count >= 0:
                    self.y -= (Player_J_count**2) * 0.5
                    Player_J_count -= 1
                    Player_activity_num = 4
                else:
                    Player_go_up = False # come down
                    self.y += Player_y_speed # come down
                    if self.player_plat_collision() == True: # he hits the ground
                        Player_jump_status = False # he is not jumping anymore
                        Player_go_up = True # get ready for the next jump
                        Player_J_count = Max_J_count
                        Player_activity_num = 0
            pass # after his collision with the ground we change the Player_jump_status to false

    def player_plat_collision(self): # this will remain the same
        player_rect = pygame.Rect(self.x, self.y, Player_width, Player_height)
        # in player_rect we are checking if the player is colliding with any platform
        for platform in LIST_PLATFORMS:
            
            if self.x in range(platform.x , platform.x + platform.width):
                if(player_rect.colliderect(platform)): #collided into the platform
                    self.y = platform.y - Player_height
                    self.platform = platform
                    return True
        return False


def draw_display(player):

    global Player_wr_no
    global Player_wl_no
    global Player_jump_no

    gameDisplay.fill(BACKGROUND_COLOR)

    for platform in LIST_PLATFORMS: # Draw all the platforms
        pygame.draw.rect(gameDisplay, BLACK, platform)

    if Player_activity_num == 0: # draw player idle right
        image = Player_activity[0]
        image = pygame.transform.scale(image, (Player_width, Player_height))
        gameDisplay.blit(image, (player.x, player.y))

    elif Player_activity_num == 1: # draw player idle left
        image = Player_activity[1]
        image = pygame.transform.scale(image, (Player_width, Player_height))
        gameDisplay.blit(image, (player.x, player.y))

    elif Player_activity_num == 2: # draw player walk right
        image = Player_activity[2][Player_wr_no//3] # 2 frames each picture
        Player_wr_no +=1
        if Player_wr_no == 24:
            Player_wr_no = 0
        image = pygame.transform.scale(image, (Player_width, Player_height))
        gameDisplay.blit(image, (player.x, player.y))

    elif Player_activity_num == 3: # draw player walk left
        image = Player_activity[3][Player_wl_no//3] # 2 frames each picture
        Player_wl_no +=1
        if Player_wl_no == 24:
            Player_wl_no = 0
        image = pygame.transform.scale(image, (Player_width, Player_height))
        gameDisplay.blit(image, (player.x, player.y))

    elif Player_activity_num == 4: # draw player jump
        image = Player_activity[4][Player_jump_no//3] # 2 frames each picture
        Player_jump_no +=1
        if Player_jump_no == 30:
            Player_jump_no = 0
        image = pygame.transform.scale(image, (Player_width, Player_height))
        gameDisplay.blit(image, (player.x, player.y))


    pygame.display.update()


def main():

    running = True

    clock = pygame.time.Clock()

    player = Player()

    while running:

        clock.tick(FPS)

        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not(Player_jump_status):
                    player.ver_movement(1) # jump
        player.hor_movement(keys_pressed)
        player.ver_movement(0) # complete the jump or fall down
        draw_display(player)
        
    pygame.quit()

if __name__ == '__main__':
    main()