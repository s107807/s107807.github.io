import time, pygame, os

SECONDS = 'SECONDS'
PERCENT = 'PERCENT'
MM = 'MM'
DEGREES = 'DEGREES'

def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def whileLoopAntiCrash():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

def wait(waitTime, unit):
	whileLoopAntiCrash()
	if unit == 'SECONDS':
		time.sleep(waitTime)
	else:
		print('incorrect unit')

def readConfig():
	f = open("controls.config", "r")
	config = f.read()
	f.close()
	config = config.replace('\n', ': ')
	config = config.split(': ')
	return config

def appendConfig(fileName):
	f = open("controls.config", "a")
	key = input(str(f'no key configuration has been set for "{fileName}" yet, please set the input (extras are (space, left, right, up, down)):'))
	f.write(f'\n{fileName}: {key.lower()}')
	f.close()

class VelocityUnits():
	DPS = 'DPS'
	RPM = 'RPM'

class ObjectSizeType():
	SMALL = 'SMALL'
	MEDIUM = 'MEDIUM'
	LARGE = 'LARGE'

class Color():
	BLACK = "BLACK"
	WHITE = "WHITE"
	RED = "RED"
	GREEN = "GREEN"
	BLUE = "BLUE"
	YELLOW = "YELLOW"
	ORANGE = "ORANGE"
	PURPLE = "PURPLE"
	CYAN = "CYAN"
	TRANSPARENT = "TRANSPARENT"

class FontType():
	MONO12 = "Arial"
	MONO15 = "Arial"
	MONO20 = "Arial"
	MONO30 = "Arial"
	MONO40 = "Arial"
	MONO60 = "Arial"
	PROP20 = "Arial"
	PROP30 = "Arial"
	PROP40 = "Arial"
	PROP60 = "Arial"
