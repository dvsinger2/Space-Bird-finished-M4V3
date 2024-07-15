import pygame

pygame.init()

# our game variables:
# ----- CREATE THE WINDOW SIZE (A) ----

window_width = 700  # adjust width
window_height = 700  # adjust height
screen = pygame.display.set_mode((window_width, window_height))

game_icon_img = pygame.image.load('assets/images/star.png') # pick img
pygame.display.set_icon(game_icon_img)  
pygame.display.set_caption('Space Bird')  # name game window



# ----- SET UP BACKGROUND \0_0 (B) ------
# write code here

def make_background(image_path):
    background_img = pygame.image.load(image_path)
    background_img_scaled = pygame.transform.scale(background_img, (window_width, window_height))
    screen.blit(background_img_scaled, (0, 0))


# ------- SET UP PLAYER :0 (C) --------
# write code here
player_img = pygame.image.load('assets/images/pink_bird.png')
player_rect = player_img.get_rect()
player_rect.centerx = 350
player_rect.y = 350
player_speed = 16



# ----- SET UP TEXT ON SCREEN ;0 (D) ------
def make_text(font_path, font_size, text, color, x, y):
    fancy_font = pygame.font.Font(font_path, font_size)
    title_text = fancy_font.render(text, 1, color)
    title_text_rect = title_text.get_rect()
    title_text_rect.centerx = x
    title_text_rect.y = y
    screen.blit(title_text, title_text_rect)

#fancy_font_small = pygame.font.Font('assets/fonts/CANAVAR.ttf', 15)
# subtitle_text = fancy_font_small.render('The happiest bird alive', 1, 'white')
# subtitle_text_rect = subtitle_text.get_rect()
# subtitle_text_rect.centerx = 350
# subtitle_text_rect.y = 90



# ------ SET UP GOAL :] (E) -------
# write code here
goal_img = pygame.image.load('assets/images/star.png')
goal_rect = goal_img.get_rect()



# ------ SET UP ENEMY <_< -------



# ------ SET UP WIN :) ---------



# ------ SET UP LOSE :( ---------



# ----- SET UP MORE \00/ ---------
def check_click():
    print('You Clicked')
def clicked():
    print('You Clicked')
    return True
def add_power_up():
    return 5+5

# our game loop:
game_running = True

while game_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        # (optional: set up mouse click here)
        if event.type == pygame.MOUSEBUTTONDOWN:
            #check_click()
            #print(clicked())
            print(add_power_up()) 
    
    
    # ---- SET UP GAME -----
    # your game here:
    # we'll write code here

    # use if statements to move player around (F)! 
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_SPACE]:
        player_rect.y -= player_speed


    # use if statements to stop player from leaving the screen (G)
    if player_rect.bottom >= window_height:
        player_rect.bottom = window_height

    # make the player move down always (H)
    player_rect.y += 8

    # try writing your first collision statement here (I):
    if player_rect.colliderect(goal_rect):
        print('You reached the goal')
    
    
    
    pygame.time.delay(30)
    # --- PUT STUFF ON SCREEN (J) ---
    screen.fill('purple')
    make_background('assets/images/Future City 3.jpg')
    screen.blit(player_img, player_rect)
    screen.blit(goal_img, goal_rect)
    make_text('assets/fonts/CANAVAR.ttf', 30, 'Space Bird', 'White', 350, 50)
    make_text('assets/fonts/CANAVAR.ttf', 15, 'The happiest bird alive', 'White', 350, 90)
    make_text('assets/fonts/CANAVAR.ttf', 60, 'In Da City', (0, 255, 244), 350, 350)
    #screen.blit(subtitle_text, subtitle_text_rect)

    

    # puts work on screen
    pygame.display.flip()

pygame.quit()