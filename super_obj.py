import pygame

class Object:
   
    def __init__(self):
        print('super init')
        super().__init__()
    def __new__(cls):
        print('super new')
        return super().__new__(cls)
    def set_image(self,img_name,img_size):
        self._pyg = pygame.image.load(img_name) 
        self._pyg = pygame.transform.scale(self._pyg, img_size)
        self._img_size = img_size
        self._rect = self._pyg.get_rect()
    def set_pos(self,pos):
        self._pos = pos
        self._rect.center = pos
    def get_pos(self):
        return self._pos
    def get_pyg(self):
        return self._pyg
    def get_rect(self):
        return self._rect        