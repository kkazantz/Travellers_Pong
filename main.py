'''
Pong Game
'''
import pygame
import random
from tkinter import *
from PIL import Image, ImageTk
# Initialize the game
pygame.init()
# Set up the game window
WIDTH = 800
HEIGHT = 400
FPS = 60
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()
# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
# Ball dimensions
BALL_RADIUS = 10
# Paddle speed
PADDLE_SPEED = 5
# Ball speed
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
# Load images
background_img = ImageTk.PhotoImage(Image.open("background.png").resize((WIDTH, HEIGHT)))
ball_img = ImageTk.PhotoImage(Image.open("ball.png").resize((BALL_RADIUS * 2, BALL_RADIUS * 2)))
paddle1_img = ImageTk.PhotoImage(Image.open("paddle1.png").resize((PADDLE_WIDTH, PADDLE_HEIGHT)))
paddle2_img = ImageTk.PhotoImage(Image.open("paddle2.png").resize((PADDLE_WIDTH, PADDLE_HEIGHT)))
button_0_img = ImageTk.PhotoImage(Image.open("button_0.png").resize((256, 256)))
button_1_img = ImageTk.PhotoImage(Image.open("button_1.png").resize((256, 256)))
button_2_img = ImageTk.PhotoImage(Image.open("button_2.png").resize((256, 256)))
button_3_img = ImageTk.PhotoImage(Image.open("button_3.png").resize((256, 256)))
button_4_img = ImageTk.PhotoImage(Image.open("button_4.png").resize((256, 256)))
button_5_img = ImageTk.PhotoImage(Image.open("button_5.png").resize((256, 256)))
button_6_img = ImageTk.PhotoImage(Image.open("button_6.png").resize((256, 256)))
button_7_img = ImageTk.PhotoImage(Image.open("button_7.png").resize((256, 256)))
button_8_img = ImageTk.PhotoImage(Image.open("button_8.png").resize((256, 256)))
button_9_img = ImageTk.PhotoImage(Image.open("button_9.png").resize((256, 256)))
button_add_img = ImageTk.PhotoImage(Image.open("button_add.png").resize((256, 256)))
button_clear_img = ImageTk.PhotoImage(Image.open("button_clear.png").resize((256, 256)))
button_delete_img = ImageTk.PhotoImage(Image.open("button_delete.png").resize((256, 256)))
button_divide_img = ImageTk.PhotoImage(Image.open("button_divide.png").resize((256, 256)))
button_equal_img = ImageTk.PhotoImage(Image.open("button_equal.png").resize((256, 256)))
button_multiply_img = ImageTk.PhotoImage(Image.open("button_multiply.png").resize((256, 256)))
button_subtract_img = ImageTk.PhotoImage(Image.open("button_subtract.png").resize((256, 256)))
class PongGame:
    def __init__(self):
        # Create the paddles
        self.paddle1 = pygame.Rect(0, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle2 = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        # Create the ball
        self.ball = pygame.Rect(WIDTH / 2 - BALL_RADIUS / 2, HEIGHT / 2 - BALL_RADIUS / 2, BALL_RADIUS, BALL_RADIUS)
        self.ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        self.ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
    def run(self):
        # Game loop
        running = True
        while running:
            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Move the paddles
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.paddle1.y > 0:
                self.paddle1.y -= PADDLE_SPEED
            if keys[pygame.K_s] and self.paddle1.y < HEIGHT - PADDLE_HEIGHT:
                self.paddle1.y += PADDLE_SPEED
            if keys[pygame.K_UP] and self.paddle2.y > 0:
                self.paddle2.y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and self.paddle2.y < HEIGHT - PADDLE_HEIGHT:
                self.paddle2.y += PADDLE_SPEED
            # Move the ball
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y
            # Ball collision with paddles
            if self.ball.colliderect(self.paddle1) or self.ball.colliderect(self.paddle2):
                self.ball_speed_x *= -1
            # Ball collision with walls
            if self.ball.y > HEIGHT - BALL_RADIUS or self.ball.y < 0:
                self.ball_speed_y *= -1
            # Draw the game elements
            screen.blit(background_img, (0, 0))
            screen.blit(paddle1_img, (self.paddle1.x, self.paddle1.y))
            screen.blit(paddle2_img, (self.paddle2.x, self.paddle2.y))
            screen.blit(ball_img, (self.ball.x, self.ball.y))
            screen.blit(button_0_img, (0, 0))
            screen.blit(button_1_img, (256, 0))
            screen.blit(button_2_img, (512, 0))
            screen.blit(button_3_img, (0, 256))
            screen.blit(button_4_img, (256, 256))
            screen.blit(button_5_img, (512, 256))
            screen.blit(button_6_img, (0, 512))
            screen.blit(button_7_img, (256, 512))
            screen.blit(button_8_img, (512, 512))
            screen.blit(button_9_img, (0, 768))
            screen.blit(button_add_img, (256, 768))
            screen.blit(button_clear_img, (512, 768))
            screen.blit(button_delete_img, (0, 1024))
            screen.blit(button_divide_img, (256, 1024))
            screen.blit(button_equal_img, (512, 1024))
            screen.blit(button_multiply_img, (0, 1280))
            screen.blit(button_subtract_img, (256, 1280))
            # Update the display
            pygame.display.flip()
            clock.tick(FPS)
        # Quit the game
        pygame.quit()
if __name__ == "__main__":
    game = PongGame()
    game.run()