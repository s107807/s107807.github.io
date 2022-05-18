from pynput.keyboard import Listener, Key
from extras import *
import threading

currentlyPressing = False
name = __file__.replace('.py', '').split('\\')
name = name[len(name)-1]

config = readConfig()

try:
	buttonKey = config[config.index(name)+1]
except:
	appendConfig(name)
config = readConfig()
buttonKey = config[config.index(name)+1]
 
def on_press(key):
	global currentlyPressing, buttonKey
	if buttonKey ==  'space':
		if key == Key.space:
			currentlyPressing = True
	elif buttonKey ==  'up':
		if key == Key.up:
			currentlyPressing = True
	elif buttonKey ==  'down':
		if key == Key.down:
			currentlyPressing = True
	elif buttonKey ==  'left':
		if key == Key.left:
			currentlyPressing = True
	elif buttonKey ==  'right':
		if key == Key.right:
			currentlyPressing = True
	else:
		if key.char == buttonKey:
			currentlyPressing = True

def on_release(key):
	global currentlyPressing, buttonKey
	if buttonKey ==  'space':
		if key == Key.space:
			currentlyPressing = False
	elif buttonKey ==  'up':
		if key == Key.up:
			currentlyPressing = False
	elif buttonKey ==  'down':
		if key == Key.down:
			currentlyPressing = False
	elif buttonKey ==  'left':
		if key == Key.left:
			currentlyPressing = False
	elif buttonKey ==  'right':
		if key == Key.right:
			currentlyPressing = False
	else:
		if key.char == buttonKey:
			currentlyPressing = False

def listen():
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

threading.Thread(target=listen).start()

def pressing():
	global currentlyPressing
	return currentlyPressing
