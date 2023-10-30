import pygame
from tkinter import *
from PIL import Image, ImageTk
class PongGame:
    def __init__(self):
        '''
        Initialize the game
        '''
        self.WIDTH = 800
        self.HEIGHT = 400
        self.FPS = 60
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.PADDLE_WIDTH = 10
        self.PADDLE_HEIGHT = 60
        self.BALL_RADIUS = 10
        self.PADDLE_SPEED = 5
        self.BALL_SPEED_X = 3
        self.BALL_SPEED_Y = 3
        self.game_over = False
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pong Game")
        self.background_img = None
        self.ball_img = None
        self.paddle1_img = None
        self.paddle2_img = None
        self.paddle1 = None
        self.paddle2 = None
        self.ball = None
        self.ball_speed_x = None
        self.ball_speed_y = None