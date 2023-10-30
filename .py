def __init__(self):
    '''
    Initialize the game
    '''
    pygame.init()
    self.WIDTH = 800
    self.HEIGHT = 400
    self.FPS = 60
    self.BLACK = (0, 0, 0)
    self.WHITE = (255, 255, 255)
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    pygame.display.set_caption("Pong Game")
    self.clock = pygame.time.Clock()
    self.PADDLE_WIDTH = 10
    self.PADDLE_HEIGHT = 60
    self.BALL_RADIUS = 10
    self.PADDLE_SPEED = 5
    self.BALL_SPEED_X = 3
    self.BALL_SPEED_Y = 3
    self.background_img = ImageTk.PhotoImage(
        Image.open("background.png").resize((self.WIDTH, self.HEIGHT))
    )
    self.ball_img = ImageTk.PhotoImage(
        Image.open("ball.png").resize((self.BALL_RADIUS * 2, self.BALL_RADIUS * 2))
    )
    self.paddle1_img = ImageTk.PhotoImage(
        Image.open("paddle1.png").resize((self.PADDLE_WIDTH, self.PADDLE_HEIGHT))
    )
    self.paddle2_img = ImageTk.PhotoImage(
        Image.open("paddle2.png").resize((self.PADDLE_WIDTH, self.PADDLE_HEIGHT))
    )
    self.paddle1 = pygame.Rect(
        0, self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT
    )
    self.paddle2 = pygame.Rect(
        self.WIDTH - self.PADDLE_WIDTH, self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT
    )
    self.ball = pygame.Rect(
        self.WIDTH / 2 - self.BALL_RADIUS / 2, self.HEIGHT / 2 - self.BALL_RADIUS / 2, self.BALL_RADIUS, self.BALL_RADIUS
    )
    self.ball_speed_x = self.BALL_SPEED_X * random.choice((1, -1))
    self.ball_speed_y = self.BALL_SPEED_Y * random.choice((1, -1))
    self.game_over = False