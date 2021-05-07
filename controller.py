#IMPORTS
import pygame
import UI
import time

#INIT
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tetris!")
ui = UI.UI(screen)

running = True

while running:
    eventList = pygame.event.get()
    inputList = []
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                inputList.append('LEFT')
            if event.key == pygame.K_RIGHT:
                inputList.append('RIGHT')
            if event.key == pygame.K_UP:
                inputList.append('UP')
            if event.key == pygame.K_DOWN:
                inputList.append('DOWN')
    ui.play(inputList)

    ui.buttonsGroup.draw(screen)
    ui.buttonsGroup.update(eventList)
    pygame.display.update()
    time.sleep(0.5)