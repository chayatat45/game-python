import pygame
from sprites import *
from config import *
import sys
#12
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #game window
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')

    def createTilemap(self):
        for i,row in enumerate(tilemap):
            for j,column in enumerate(row):
                Ground(self,j,i)
                if column == "B":
                    Block(self,j,i)
                if column == "P":
                    Player(self,j,i)
                


    def new(self): 
        #new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        #game loop events
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #game loop update
        self.all_sprites.update()

    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing: 
            self.events()
            self.update()
            self.draw()
        self.running = False

    def gameover(self):
        pass

    def intro_screen(self):
        pass

g =Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.gameover()

pygame.quit
sys.exit()

