import pygame
import requests
import rembg
from io import BytesIO
import pieces

#Game Screen

pygame.init()
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Chess Game')

font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(
            status_text[pieces.turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))

# draw pieces onto board
def draw_pieces():
    for i in range(len(pieces.white_pieces)):
        index = pieces.piece_list.index(pieces.white_pieces[i])
        if pieces.white_pieces[i] == 'pawn':
            screen.blit(
                pieces.white_pawn, (pieces.white_locations[i][0] * 100 + 22, pieces.white_locations[i][1] * 100 + 30))
        else:
            screen.blit(pieces.white_images[index], (pieces.white_locations[i]
                                              [0] * 100 + 10, pieces.white_locations[i][1] * 100 + 10))
        if pieces.turn_step < 2:
            if pieces.selection == i:
                pygame.draw.rect(screen, 'red', [pieces.white_locations[i][0] * 100 + 1, pieces.white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(pieces.black_pieces)):
        index = pieces.piece_list.index(pieces.black_pieces[i])
        if pieces.black_pieces[i] == 'pawn':
            screen.blit(
                pieces.black_pawn, (pieces.black_locations[i][0] * 100 + 22, pieces.black_locations[i][1] * 100 + 30))
        else:
            screen.blit(pieces.black_images[index], (pieces.black_locations[i]
                                              [0] * 100 + 10, pieces.black_locations[i][1] * 100 + 10))
        if pieces.turn_step >= 2:
            if pieces.selection == i:
                pygame.draw.rect(screen, 'blue', [
                                 pieces.black_locations[i][0] * 100 + 1, pieces.black_locations[i][1] * 100 + 1,                               100, 100], 2)






