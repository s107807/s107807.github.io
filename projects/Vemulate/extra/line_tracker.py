from extras import *

#between 1-100%
reflectivityValue = 10

def reflectivity(unit):
	whileLoopAntiCrash()
	global reflectivityValue
	if unit == 'PERCENT':
		return reflectivityValue
	else:
		print('incorrect unit')

def setReflectivity(number):
	whileLoopAntiCrash()
	global reflectivityValue
	if number >= 100:
		number = 100
	elif number <= 0:
		number = 0
	reflectivityValue = number
