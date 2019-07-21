import pygame
import pygame.locals
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

vertices = (
    (-1, 1, -1),  # 0
    (1, 1, -1),  # 1
    (1, -1, -1),  # 2
    (1, -1, 1),  # 3
    (-1, -1, 1),  # 4
    (-1, 1, 1),  # 5
    (1, 1, 1),  # 6
    (-1, -1, -1),  # 7
)

edges = (
    (0, 1),
    (0, 5),
    (0, 7),
    (2, 1),
    (2, 3),
    (2, 7),
    (4, 3),
    (4, 7),
    (4, 5),
    (6, 1),
    (6, 3),
    (6, 5),
)

surfaces = (
    (0, 1, 2, 7),
    (1, 2, 3, 6),
    (3, 4, 5, 6),
    (4, 5, 0, 7),
    (2, 3, 4, 7),
    (0, 1, 6, 5),

)

ground_surface = (0, 1, 2, 3)

ground_vertices = (
    (-10, -.1, 50),
    (10, -.1, 50),
    (-10, -.1, -300),
    (10, -.1, -300),
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    )


def ground():
    glBegin(GL_QUADS)
    # val = 0
    for vertex in ground_vertices:
        # val += 1
        glColor3fv((0, 1, 1))
        glVertex3fv(vertex)

    glEnd()


def set_vertices(max_distance):
    x_val_change = random.randrange(-10, 10)
    y_val_change = 0  # random.randrange(-10, 10)
    z_val_change = random.randrange(-1*max_distance, -20)

    final_vertices = []

    for vert in vertices:
        new_vertices = []
        x_vertex = vert[0] + x_val_change
        y_vertex = vert[1] + y_val_change
        z_vertex = vert[2] + z_val_change

        new_vertices.append(x_vertex)
        new_vertices.append(y_vertex)
        new_vertices.append(z_vertex)

        final_vertices.append(new_vertices)
    return final_vertices


def cube(cube_vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        val = 0
        for vertex in surface:
            val += 1
            glColor3fv(colors[val])
            glVertex3fv(cube_vertices[vertex])
    glEnd()

    # glLineWidth(5)
    # glBegin(GL_LINES)
    # for edge in edges:
    #     for vertex in edge:
    #         glVertex3fv(cube_vertices[vertex])
    #         # glColor3f(1, 0, 0)
    # glEnd()


def main():
    pygame.init()
    display = (800, 800)  # width and height
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)  # What is this?
    gluPerspective(45, (display[0]/display[1]), 1.0, 50)
    # field of view; display width/height; near and far clipping plane

    glTranslatef(random.randrange(-5, 5), random.randrange(-5, 5), -40.0)  # Viewing zone: Moving back (z-axis) 5 units
    # glRotate(3, 2, 1, 1)

    x_move = 0
    y_move = 0

    max_distance = 300
    cube_dict = {}
    for k in range(75):
        cube_dict[k] = set_vertices(max_distance)

    # crashed = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x_move = 0.3
                if event.key == K_RIGHT:
                    x_move = -0.3
                if event.key == K_DOWN:
                    y_move = 0.3
                if event.key == K_UP:
                    y_move = -0.3

            if event.type == pygame.KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    x_move = 0
                if event.key == K_DOWN or event.key == K_UP:
                    y_move = 0

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         glTranslatef(0.0, 0.0, 1.0)
            #     if event.button == 5:
            #         glTranslatef(0.0, 0.0, -1.0)

        # matrix_val = glGetDoublev(GL_MODELVIEW_MATRIX)

        # camera_x = matrix_val[3][0]
        # camera_y = matrix_val[3][1]
        # camera_z = matrix_val[3][2]
        # if camera_z < -1:
        #     object_pass = True

        # glRotatef(1, 3, 1, 1)

        glTranslatef(x_move, y_move, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)  # What is it?

        ground()

        for each_cube in cube_dict:
            new_cube = cube_dict[each_cube]
            cube(new_cube)

        pygame.display.flip()
        pygame.time.wait(10)


for x in range(10):
    main()
pygame.quit()
quit()


