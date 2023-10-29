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
# Create the paddles
paddle1 = pygame.Rect(0, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
# Create the ball
ball = pygame.Rect(WIDTH / 2 - BALL_RADIUS / 2, HEIGHT / 2 - BALL_RADIUS / 2, BALL_RADIUS, BALL_RADIUS)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.y < HEIGHT - PADDLE_HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.y > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.y < HEIGHT - PADDLE_HEIGHT:
        paddle2.y += PADDLE_SPEED
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    # Ball collision with walls
    if ball.y > HEIGHT - BALL_RADIUS or ball.y < 0:
        ball_speed_y *= -1
    # Draw the game elements
    screen.blit(background_img, (0, 0))
    screen.blit(paddle1_img, (paddle1.x, paddle1.y))
    screen.blit(paddle2_img, (paddle2.x, paddle2.y))
    screen.blit(ball_img, (ball.x, ball.y))
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
# Quit the game
pygame.quit()