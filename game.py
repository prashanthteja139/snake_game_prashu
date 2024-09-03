import pygame
import time
import random

# Initialize the pygame library
pygame.init()

# Define colors using RGB values
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the width and height of the game window
display_width = 800
display_height = 600

# Create the game window with the specified dimensions
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game By Prashu')

# Set the clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Define the size of each snake segment and the speed of the snake
snake_block = 20
snake_speed = 15

# Define fonts for displaying text on the screen
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score on the screen
def show_score(score):
    value = score_font.render(f"Your Score: {score}", True, white)
    dis.blit(value, [0, 0])

# Function to draw the snake on the screen
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display a message on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

# Function to generate a new food position
def generate_food():
    return round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0, round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0

# Main function to run the game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Initial change in position (direction of movement)
    x1_change = 0
    y1_change = 0

    # List to store the snake's segments
    snake_list = []
    length_of_snake = 1

    # Initial position of the food
    foodx, foody = generate_food()

    # Main game loop
    while not game_over:
        # Loop to handle game over state
        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for collisions with the game window boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)  # Fill the screen with blue color
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  # Draw the food
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Maintain the length of the snake
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake and show the score
        draw_snake(snake_block, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            length_of_snake += 1

        clock.tick(snake_speed)  # Control the speed of the snake

    pygame.quit()  # Quit the game
    quit()

# Start the game
gameLoop()
