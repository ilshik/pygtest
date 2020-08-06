import pygame
import random

class Gagamel:
   
    def __init__(self):
        print('init')
        super().__init__()
        self._gowhere = (random.randint(-10,10),random.randint(-10,10))
    def __new__(cls):
        print('new')
        return super().__new__(cls)
    def set_image(self,img_name,img_size):
        self._pyg = pygame.image.load(img_name) 
        self._pyg = pygame.transform.scale(self._pyg, img_size)
    def set_pos(self,pos):
        self._pos = pos
    def set_randpos(self):
        self.set_direction()
        self._pos = (self._pos[0] + self._gowhere[0],self._pos[1] + self._gowhere[1])
        if self._pos[0]>=self._bound[0]:
            self._pos=(self._pos[0]-10,self._pos[1])
        if self._pos[0]<=0:
            self._pos=(10,self._pos[1])
        if self._pos[1]>=self._bound[1]:
            self._pos=(self._pos[0],self._pos[1]-10)
        if self._pos[1]<=0:
            self._pos=(self._pos[0],10)
        print(self._pos)        
    def get_pos(self):
        return self._pos
    def get_pyg(self):
        return self._pyg
    def set_direction(self):
        self._gowhere = (random.randint(-10,10),random.randint(-10,10))
    def get_direction(self):
        return self._gowhere
    def set_bound(self,bound):
        self._bound = bound