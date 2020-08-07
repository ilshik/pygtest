import pygame # pygame 모듈의 임포트
import sys # 외장 모듈
from pygame.locals import * # QUIT 등의 pygame 상수들을 로드한다.
from gagamel import Gagamel 
from attacker import Attacker
from bullet import Bullet
import random

width = 600 # 상수 설정
height = 400
white = (255, 255, 255)
black = (  0,   0,   0)
fps = 30

pygame.init() # 초기화

pygame.display.set_caption('Hello, world!') # 창 제목 설정
displaysurf = pygame.display.set_mode((width, height), 0, 32) # 메인 디스플레이를 설정한다
clock = pygame.time.Clock() # 시간 설정

#gulimfont = pygame.font.SysFont('굴림', 70) # 서체 설정
#helloworld = gulimfont.render('Hello, world!', 1, black) 
# .render() 함수에 내용과 안티앨리어싱, 색을 전달하여 글자 이미지 생성

#helloworld = pygame.image.load('attack.png')
#helloworld = pygame.transform.scale(helloworld, (50,50))
#hellorect = helloworld.get_rect() # 생성한 이미지의 rect 객체를 가져온다
#hellorect.center = (width / 2, height / 2) # 해당 rect의 중앙을 화면 중앙에 맞춘다

atkr = Attacker()
atkr.set_image('attack.png',(50,50))
atkr.set_pos((width / 2, height / 2))

gaga = Gagamel()
gaga.set_image('2659980.png',(50,50))
gaga.set_pos( (width / 2, height / 2))
gaga.set_bound((width,height))

bullets = []

while True: # 아래의 코드를 무한 반복한다.
    
    displaysurf.fill(white) # displaysurf를 하얀색으로 채운다
    gaga.set_antpos((width,height))
    gaga.set_randpos()

    for event in pygame.event.get(): # 발생한 입력 event 목록의 event마다 검사
        if event.type == QUIT: # event의 type이 QUIT에 해당할 경우
            pygame.quit() # pygame을 종료한다
            sys.exit() # 창을 닫는다
        if event.type == MOUSEMOTION:
            width,height = pygame.mouse.get_pos()            
        if event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT:
                width+=1
            if event.key == pygame.K_LEFT:
                width-=1
            if event.key == pygame.K_UP:
                height-=10
            if event.key == pygame.K_DOWN:                
                height+=10
            if event.key == pygame.K_SPACE:
                bullet = Bullet()
#                bullet.bullet_factory((width,height),(600,400),gaga.get_pos())
                bullet.bullet_factory(gaga.get_pos(),(600,400),(width,height))
                bullets.append(bullet)
    if random.randint(0,10)>8:
        bullet = Bullet()
    #   bullet.bullet_factory((width,height),(600,400),gaga.get_pos())
        bullet.bullet_factory(gaga.get_pos(),(600,400),(width,height))
        bullets.append(bullet)

    atkr.set_pos((width,height))
    displaysurf.blit(atkr.get_pyg(), atkr.get_rect()) # displaysurf의 hellorect의 위치에 helloworld를 뿌린다
    gaga.run_away()

    if len(bullets)>0:
        i=0
        for bullet in bullets:
            bullet.nextpos()
            bullet.set_antpos((width,height))
            bullet.crash()
            displaysurf.blit(bullet.get_pyg(),bullet.get_pos())
#            gaga.set_antpos(bullet.get_pos())
#            gaga.run_away()
            if bullet.is_out() or bullet.get_status()>5:
                print ('Bullet del',i,len(bullets))
                del bullet
                del bullets[i]
            i=i+1        

    displaysurf.blit(gaga.get_pyg(),gaga.get_rect())
    pygame.display.update() # 화면을 업데이트한다
    clock.tick(fps) # 화면 표시 회수 설정만큼 루프의 간격을 둔다