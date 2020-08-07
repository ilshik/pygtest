import pygame
from super_obj import Object

class Attacker(Object):
   
    def __init__(self):
        print('attacker init')
        super().__init__()
    def __new__(cls):
        print('attacker new')
        return super().__new__(cls)     