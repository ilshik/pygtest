import pygame
import random
from super_obj import Object

class Gagamel(Object):
   
    def __init__(self):
        print('gagamel init')
        super().__init__()
        self._gowhere = (random.randint(-10,10),random.randint(-10,10))
        self._crash = False
        self._crashcnt = 0
    def __new__(cls):
        print('gagamel new')
        return super().__new__(cls)

    def set_randpos(self):
        self.set_direction()
        self._pos = (self._pos[0] + self._gowhere[0],self._pos[1] + self._gowhere[1])
        self.run_away()

    def run_away(self):
        if self._pos[0]+self._img_size[0]/2>=self._bound[0]:
            self._pos=(self._pos[0]-20,self._pos[1])
        if self._pos[0]-self._img_size[0]/2<=0:
            self._pos=(20,self._pos[1])
        if self._pos[1]+self._img_size[1]/2>=self._bound[1]:
            self._pos=(self._pos[0],self._pos[1]-20)
        if self._pos[1]-self._img_size[1]/2<=0:
            self._pos=(self._pos[0],20)
        xpos,ypos = self._pos
        if abs(self._pos[0]-self._antpos[0])<self._img_size[0] and abs(self._pos[1]-self._antpos[1])<self._img_size[1]:
            self._crash = True
            self._crashcnt = 1
            if self._pos[0]>=self._antpos[0] and self._pos[0]-self._antpos[0]<self._img_size[0]:
                xpos = self._pos[0]+10
            if self._pos[0]<self._antpos[0] and self._antpos[0]-self._pos[0]<self._img_size[0]:
                xpos = self._pos[0]-10
            if self._pos[1]>=self._antpos[1] and self._pos[1]-self._antpos[1]<self._img_size[1]:
                ypos = self._pos[1]+10
            if self._pos[1]<self._antpos[1] and self._antpos[1]-self._pos[1]<self._img_size[1]:
                ypos = self._pos[1]-10
        elif self._crashcnt > 0 :
            self._crashcnt += 1
            self._crash = False
        self.set_pos((xpos,ypos))      

    def set_direction(self):
        self._gowhere = (random.randint(-9,9),random.randint(-9,9))
    def get_direction(self):
        return self._gowhere
    def set_bound(self,bound):
        self._bound = bound
    def set_antpos(self,antpos):
        self._antpos = antpos
    def get_status(self):
        return self._crashcnt
    def set_status(self):
        self._crashcnt = 0

#    def set_image(self,img_name,img_size):
#        self._pyg = pygame.image.load(img_name) 
#        self._pyg = pygame.transform.scale(self._pyg, img_size)
#        self._img_size = img_size
#        self._rect = self._pyg.get_rect()
#    def set_pos(self,pos):
#        self._pos = pos
#    def get_pos(self):
#        return self._pos
#    def get_pyg(self):
#        return self._pyg
#    def get_rect(self):
#        self._rect.center = self._pos
#        return self._rect