import pygame
pygame.init()
screen = pygame.display.set_mode((624, 624))
clock = pygame.time.Clock()

background = pygame.image.load("graphics/background.png").convert()
blankTile = "graphics/blankTile.png"
circle = "graphics/circle.png"
cross = "graphics/cross.png"
current = "cross"

positionList = [(6, 6), (210, 6), (420, 6), (6, 210), (210, 210), (420, 210), (6, 420), (210, 420), (420, 420)]
markerList = []

class Tile():
    def __init__(self, pos, image):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.placed = False

    def draw(self):
        screen.blit(self.image, self.rect)

    def mark(self, image):
        mousePOS = pygame.mouse.get_pos()
        if mousePOS[0] >= self.pos[0] and mousePOS[0] <= self.pos[0] + 198 and mousePOS[1] >= self.pos[1] and mousePOS[1] <= self.pos[1] + 198:
            if self.placed == False:
                if image == "circle":
                    self.image = pygame.image.load(circle).convert_alpha()
                if image == "cross":
                    self.image = pygame.image.load(cross).convert_alpha()
                self.placed = True

for i in positionList:
    markerList.append(Tile(i, blankTile))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in markerList:
                i.mark(current)
            if current == "cross": 
                current = "circle"
            elif current == "circle": 
                current = "cross"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                markerList = []
                for i in positionList:
                    markerList.append(Tile(i, blankTile))
                current = "cross"

    screen.blit(background, (0, 0))

    for i in markerList:
        i.draw()

    pygame.display.flip()
    clock.tick(30)