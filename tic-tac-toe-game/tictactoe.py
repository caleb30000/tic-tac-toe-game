# IMPORTING THE IMPORTANT MODULES
import pygame, sys #pygame is a module designed for building interactive games.pygame module contains the functionality needed to make a game. sys module would be used to exit the game when the player quits
import numpy as np #this module helps us provide arrays, and also provides better algebraic calculations.

# INITIALIZES PYGAME WITH THE KEYWORD .init which also means `initialize`
pygame.init()

# GLOBAL CONSTANTS
# They are called global constants because they are fixed and wouldn't change. They can be called directly into any block of code at ant point of the game.
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200	
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# COLORS (rgb: red green blue)
RED = (255, 0, 255)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (75, 145, 135)
CIRCLE_COLOR = (240, 240, 240)
CROSS_COLOR = (100, 60, 100)

# SCREEN
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
# We call pygame.display.set_mode() to create a display window called `screen`, on which we’ll draw all of the game’s graphical elements.
# The argument (WIDTH, HEIGHT) is a tuple that consists of constants which defines the dimensions of the game window.
# By passing these dimensions to pygame.display.set_mode(), we create a game window 600 pixels wide by 600 pixels high.

pygame.display.set_caption( 'TIC TAC TOE' ) #the game name/title
screen.fill( BG_COLOR ) #pygame creates a black screen by default so with the help of our color combination by constants above, BG_COLOR fills the game background with the desired color. the .fill() method helps us to fill the background. it takes only one argument; a color. that is why we has to declare them earlier as constants.

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros( (BOARD_ROWS, BOARD_COLS) ) #returns an array of given shape and type, filled with zeros to be manipulated later on.

# ---------
# FUNCTIONS
# ---------
def draw_lines():
	# 1 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
	# 2 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

	# 1 vertical
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	# 2 vertical
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

# this function basically marks a square in the console board
def mark_square(row, col, player): #this function takes 3 parameters
	board[row][col] = player

# this function returns true or false depending on whether a square is available or not
def available_square(row, col):
	return board[row][col] == 0 #this return statement checks whether a square is available to be clicked or not

# this function returns true if our board is full
def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False

	return True

def check_win(player):
	# vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win cheCk
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

draw_lines()

# ---------
# VARIABLES
# ---------
player = 1
game_over = False

# MAINLOOP
#The game is controlled by a while loop which we'd call the mainloop that contains an event loop and code that manages screen updates.
#An `event` is an action that the user performs while playing the game, such as pressing a key or moving the mouse.
#To make our program respond to events, we’ll write an `event` loop to listen for an event and perform an appropriate
# task depending on the kind of event that occurred. 

while True:
    #Watching for keyboard and mouse events.
	for event in pygame.event.get(): #This for loop is an `event` loop.The pygame.event.get() method is used to access the events detected by pygame. Any keyboard or mouse event would trigger the for loop and it runs.
    #the if statement below responds to specific events. For example, when the player clicks the game window’s close button, a
    #pygame.QUIT event is detected and we call on sys.exit() to exit the game.
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			if available_square( clicked_row, clicked_col ):

				mark_square( clicked_row, clicked_col, player )
				if check_win( player ):
					game_over = True
				player = player % 2 + 1

				draw_figures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()