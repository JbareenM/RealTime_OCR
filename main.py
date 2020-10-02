import pygame
from settings import *
from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
import  pytesseract
import cv2
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ahmad\AppData\Local\Tesseract-OCR\tesseract.exe'
# a=cv2.imread('img/Netanya.png')
# a=cv2.resize(a,(1200,1200))
# a=cv2.flip(a , 1)
# cv2.imwrite('img/Netanya.png', a)
count = 0

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
sc_map = pygame.Surface(MINIMAP_RES)

sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc, sc_map)


startX , startY , endX ,endY = int(WIDTH * 0.10), int(HEIGHT * 0.30) ,int(WIDTH * 0.90) , int(HEIGHT * 0.70)
index =0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("  ", True, (0, 255, 0), (0, 0, 255))
textRect = text.get_rect()


# _,_ = set_text_map()
#grid = make_grid(HEIGHT, WIDTH)

end_pos = "Ariel"

Arrived  = False
Found = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    index = index + 1

    player.movement()
    sc.fill(BLACK)
    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    if Found == True :
        drawing.mini_map(player)

    #
    # algorithm(lambda: draw(sc, grid, HEIGHT, WIDTH), grid, player.pos, end)

    if index == 60:
        index = 0
        pygame.image.save(sc, 'img/test45.png')
        a = cv2.imread('img/test45.png')
        # dst = cv2.warpPerspective(a, M, (width1, height1))
        #
        # dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        config = ("-l eng --oem 1 --psm 7")
        text = pytesseract.image_to_string(a, config=config)



        if text.find('Bat Yam') != -1 :
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects =[
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 8)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 9)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 9.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 10))
                ]



        elif text.find('Netanya') != -1:
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects = [
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (1.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (1, 7.5))
                ]

        elif text.find('Petah Tikva') != -1:
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects = [
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 8)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5.5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8.5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9.5, 8.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9.5, 9)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9.5, 9.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9.5, 10))
                ]

        elif text.find('Jerusalem') != -1:
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects = [
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8.5, 7))
                ]

        elif text.find('Herzliya') != -1:
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects = [
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 4)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 3.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 3)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 2)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (1.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (1.47, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (1, 1.5))
                ]


        elif text.find('Beer Sheva') != -1:
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects = [
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9.5, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (10, 7.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (10.5, 7)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (10.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (10.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (10.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (11, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (11.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (12, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (12.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (13, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (13.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (14, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (14.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (15, 5.5))

                ]


        elif text.find('Haifa') != -1:
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects = [
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 6.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 6)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 5.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 4)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 3.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 3)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (7.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8.5, 2)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (8.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (9.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (10, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (10.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (11, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (11.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (12, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (12.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (13, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (13.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (14, 1.5))

                ]

        elif text.find('Tel Aviv') != -1:
            Found = True
            if end_pos == "Ariel":
                sprites.list_of_objects = [
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 4.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 4)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 3.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 3)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (2.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (3.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (4.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (5.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 2.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 2)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 1.5)),
                    SpriteObject(sprites.sprite_parameters['sprite_flame'], (6.5, 1))

                ]

        elif text.find('Ariel') != -1 :
            Arrived = True




        text = font.render("OCR: "+text, True, (0,255,0), (0,0,255))
        textRect = text.get_rect()
    if Arrived == True:
        count = count + 1
    if count == 200:
        pygame.quit()
        # set the center of the rectangular object.
    textRect.center = (WIDTH // 2, 60)
    sc.blit(text, textRect)
    if Arrived == False:
        text_dst = font.render("Destination: " + end_pos, True, (255, 0, 0))
        textRect_dst = text_dst.get_rect()
        textRect_dst.center = (200, 20)
    else:
        text_dst = font.render("You Have Arrived The Destination!!", True, (0, 255,0) , (0,0,255))
        textRect_dst = text_dst.get_rect()
        textRect_dst.center = (WIDTH//2, 60)

    sc.blit(text_dst, textRect_dst)
    # cv2.putText(sc, text, (startX, startY - 20),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    pygame.display.flip()
    clock.tick(FPS)
