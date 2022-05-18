from extras import *

#between 20-200MM
objectDistance = 20

#velocity in terms of m/s
objectVelocity = 10

#object size in either ObjectSizeType.(SMALL, MEDIUM, LARGE)
objectSize = ObjectSizeType.SMALL

#object detected (true or false)
objectDetected = False

def object_distance(unit):
	whileLoopAntiCrash()
	if unit == 'MM':
		return objectDistance
	else:
		print('incorrect unit')

def setObject_distance(number):
	whileLoopAntiCrash()
	if number >= 200:
		number = 200
	elif number <= 20:
		number = 20
	objectDistance = number

def object_velocity():
	whileLoopAntiCrash()
	return objectVelocity

def setObject_velocity(number):
	whileLoopAntiCrash()
	objectVelocity = number

def object_size():
	whileLoopAntiCrash()
	return objectSize

def setObject_size(size):
	whileLoopAntiCrash()
	objectSize = size

def is_object_detected():
	whileLoopAntiCrash()
	return objectDetected

def setObject_detected(boolean):
	whileLoopAntiCrash()
	if boolean == True or boolean == False:
		objectDetected = boolean
