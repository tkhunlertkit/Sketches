import pygame
import math

BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)
BLUE    = (  0,   0, 255)
PI = math.pi

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
coordinate = [0, 0]
poly_size = 100
sides = 20
weight = 3
x_direction = 5
y_direction = 3

def draw_line_at_angle(screen, color, coor, size, weight, degree):
    x = coor[0] - math.cos(math.radians(degree)) * size
    y = coor[1] - math.sin(math.radians(degree)) * size
    pygame.draw.line(screen, color, (x, y), coor, weight)
    return (x, y)

def draw_regular_poly(screen, color, coor, size, weight, sides):
    omega = 360. / sides
    N = int(math.floor(90 / omega))

    denom = 0
    for i in range(1, N + 1):
        denom += math.cos(math.radians(omega * i))
    denom *= 2
    denom += 1
    my_len = size / denom
    x = ((size - my_len) / 2) + coor[0] + my_len
    y = size + coor[1]
    coor = (x, y)
    for i in range(0, sides):
        coor = draw_line_at_angle(screen, color, coor, my_len, weight, omega * i)

if __name__=='__main__':

    done = False
    prev_mouse_location = pygame.mouse.get_pos()
    print prev_mouse_location

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    print 'down arrow pressed'
                    coordinate[1] += 5
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_UP]:
                    print 'up arrow pressed'
                    coordinate[1] -= 5
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    print 'left arrow pressed'
                    coordinate[0] -= 5
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    print 'right arrow pressed'
                    coordinate[0] += 5

        curr_mouse_loc = pygame.mouse.get_pos()
        if prev_mouse_location != curr_mouse_loc:
            prev_mouse_location = curr_mouse_loc
            print curr_mouse_loc
        coordinate[0] += x_direction
        coordinate[1] += y_direction
        if coordinate[0] + poly_size >= size[0] or coordinate[0] <= 0:
            x_direction *= -1
        if coordinate[1] + poly_size >= size[1] or coordinate[1] <= 0:
            y_direction *= -1

        screen.fill(WHITE)

        draw_regular_poly(screen, RED, coordinate, poly_size, weight, sides)

        pygame.display.flip()
        clock.tick(60)


pygame.quit()
