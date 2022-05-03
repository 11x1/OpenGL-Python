from OpenGL.GL import *
from OpenGL.GLUT import *
import random

import pixels

width = 200
height = 200

pixelData = pixels.Pixels(width, height)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    pixelData.randomize()
    glDrawPixels(width, height, GL_RGB, GL_UNSIGNED_BYTE, pixelData.get_pixels())

    glutSwapBuffers()


def setup():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(height, width)
    window = glutCreateWindow("haha lol aken")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    setup()