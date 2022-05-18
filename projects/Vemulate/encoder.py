from pynput.keyboard import Listener, Key
from extras import *
import threading

encoderPercent = 0
encoderSpeed = 1

def on_press(key):
	global encoderPercent, encoderSpeed
	if key == Key.right:
		encoderPercent += encoderSpeed
		print(f'position: {encoderPercent}')
	if key == Key.left:
		encoderPercent -= encoderSpeed
		print(f'position: {encoderPercent}')
	if key == Key.up:
		encoderSpeed += 1
		print(f'rpm: {encoderSpeed}')
	if key == Key.down:
		encoderSpeed -= 1
		print(f'rpm: {encoderSpeed}')

def listen():
	with Listener(on_press=on_press) as listener:
		listener.join()

threading.Thread(target=listen).start()

def set_position(number, unit):
	whileLoopAntiCrash()
	global encoderPercent
	if unit == 'DEGREES':
		encoderPercent = number
	else:
		print('incorrect unit')

def position(unit):
	whileLoopAntiCrash()
	global encoderPercent
	if unit == 'DEGREES':
		return encoderPercent
	else:
		print('incorrect unit')

def velocity(unit):
	whileLoopAntiCrash()
	global encoderSpeed
	if unit == 'DPS':
		return encoderSpeed
