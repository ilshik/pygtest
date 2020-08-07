import pygame
import math
from super_obj import Object

class Bullet(Object):
   
    def __init__(self):
        print('Bullet init')
        super().__init__()
        self._dead = False
        
    def __new__(cls):
        print('Bullet new')
        return super().__new__(cls)     

    def bullet_factory(self,pos,bound,antpos):
        self.set_image('2659980.png',(20,20))
        self._img_size = (20,20)
        self.set_pos(pos)
        self.set_bound(bound)
        self.set_speed(10)
        src_posx = pos[0]
        src_posy = pos[1]
        target_posx = antpos[0]
        target_posy = antpos[1]
        self.set_angle(math.pi - math.atan2(target_posx - src_posx, target_posy - src_posy))

    def set_speed(self,speed):
        self._speed = speed

    def set_angle(self,angle):
        self._angle = angle
        print('angle',angle)
    def get_direction(self):
        return self._gowhere
    def set_bound(self,bound):
        self._bound = bound
    def set_antpos(self,antpos):
        self._antpos = antpos
    def nextpos(self):
        if self._dead:
            return self._rect
        xpos = self._pos[0]
        ypos = self._pos[1]
        xpos += self._speed* math.sin(self._angle)
        ypos -= self._speed* math.cos(self._angle)
        self.set_pos((xpos,ypos))
        return self._rect
    def is_out(self):
        out = False
        if self._pos[0]<0 or self._pos[1]<0 :
            out = True
        if self._pos[0]>self._bound[0] or self._pos[1]>self._bound[1] :
            out = True
        return out
    def crash(self):
        if self._dead:
            return False
        if abs(self._pos[0]-self._antpos[0])<self._img_size[0] and abs(self._pos[1]-self._antpos[1])<self._img_size[1]:
            print('crash',self._pos,self._antpos)
            self._dead = True
            self.set_image('crash.png',(30,30))
        return self._dead
    def set_antpos(self,antpos):
        self._antpos = antpos
    def get_status(self):
        return self._dead