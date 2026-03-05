import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class sprite1(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect  = self.image.get_rect()
        self.velocity= [random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit= False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit= True
        if self.rect.top <=0 or self.rect.bottom >=400:
            self.velocity[1] = -self.velocity[1]
            boundry_hit= True
        
        if boundry_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

def changeBgColor():
    global bg_color 
    bg_color= random.choice([BLUE, LIGHTBLUE, DARKBLUE])

sprites_list= pygame.sprite.Group()
sp1 = sprite1(WHITE, 30, 30)

sp1.rect.x = random.randint(0,470)
sp1.rect.y = random.randint(0,370)
sprites_list.add(sp1)

sp2 = sprite1(YELLOW, 20,20)
sp2.rect.x= random.randint(0,470)
sp2.rect.y= random.randint(0,370)
sprites_list.add(sp2)

sp3 = sprite1(ORANGE, 40,40)
sp3.rect.x= random.randint(0,470)
sp3.rect.y= random.randint(0,370)
sprites_list.add(sp3)

# Create the game window
screen = pygame.display.set_mode((500, 400))

# Set the window title
pygame.display.set_caption("Colorful Bounce")

# Set the initial background color
bg_color = BLUE
# Apply the background color
screen.fill(bg_color)
# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            changeBgColor()

    sprites_list.update()
    screen.fill(bg_color)
    sprites_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(240)