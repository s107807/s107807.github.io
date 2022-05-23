import os
try:
	import csv, pygame, time, numpy
except:
	os.system('pip install pygame')
	os.system('pip install numpy')
	os.system('pip install csv')
	import csv, pygame, time, numpy

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def find_nearest(array, value):
	for s in range(len(array)):
		if array[s] == 'none':
			array[s] = 0
	array = numpy.asarray(array)
	idx = (numpy.abs(array - value)).argmin()
	return array[idx]

pygame.init()
clear()

screenReslution = [500, 500]
#Dont edit this unless you know what you're doing
screenScale = 1
penWidth = 10
spacer = 10
penColor = 'WHITE'

surface = pygame.display.set_mode([(screenReslution[1] * screenScale), (screenReslution[0] * screenScale)])
pygame.display.set_caption("Sunrise-Sunset Project")


monthOrder = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
yearsOrder = ['2005', '2006']

def drawGraph():
	surface.fill('BLACK')
	pygame.draw.line(surface, penColor,[(spacer * screenScale), (spacer * screenScale)], [(spacer * screenScale), (screenReslution[0]-spacer * screenScale)], (int(penWidth/10) * screenScale))
	pygame.draw.line(surface, penColor,[(spacer * screenScale), (screenReslution[0]-spacer * screenScale)], [(screenReslution[1]-spacer * screenScale), (screenReslution[0]-spacer * screenScale)], (int(penWidth/10) * screenScale))
	for s in range(len(monthOrder)):
		pygame.draw.line(surface, penColor,[((((screenReslution[1]-spacer)-spacer)/int(len(monthOrder)))*(s+1))+spacer, (((screenReslution[0]-spacer) * screenScale)-5)], [((((screenReslution[1]-spacer)-spacer)/int(len(monthOrder)))*(s+1))+spacer, (((screenReslution[0]-spacer) * screenScale)+5)], (int(penWidth/10) * screenScale))
	#hours in a day
	for s in range(24):
		pygame.draw.line(surface, penColor,[spacer-5, ((((screenReslution[0]-spacer)-spacer)/24)*s)+spacer], [spacer+5, ((((screenReslution[0]-spacer)-spacer)/24)*s)+spacer], (int(penWidth/10) * screenScale))
	pygame.display.flip()


drawGraph()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
			break
	date = input('enter date: ')
	try:
		if int(date) <= 31 and int(date) >= 1:
			clear()
			if int(date) == 31:
				print('WARNING: unable to tell accurate daylight savings data due to it being the 31st day')
			for a in range(len(yearsOrder)):
				drawGraph()
				dlsBoolean = False
				dlsArray = []
				daylightsSavings = []
				sunsets = []
				sunrises = [].
				for b in range(len(monthOrder)):
					rows = []
					try:
						if os.name == 'nt':
							with open(f'.\\monthLogs\\{monthOrder[b]}-{yearsOrder[a]}-log.csv', 'r') as file:
								csvreader = csv.reader(file)
								header = next(csvreader)
								for row in csvreader:
									rows.append(row)
						else:
							with open(f'./monthLogs/{monthOrder[b]}-{yearsOrder[a]}-log.csv', 'r') as file:
								csvreader = csv.reader(file)
								header = next(csvreader)
								for row in csvreader:
									rows.append(row)
						daylightsSavings.append((int(rows[int(date)-1][2].replace(" pm", "").split(":")[0])*60)+int(rows[int(date)-1][2].replace(" pm", "").split(":")[1]))
						sunsets.append((int(rows[int(date)-1][2].replace(" pm", "").split(":")[0])*60)+int(rows[int(date)-1][2].replace(" pm", "").split(":")[1]))
						sunrises.append((int(rows[int(date)-1][1].replace(" am", "").split(":")[0])*60)+int(rows[int(date)-1][1].replace(" am", "").split(":")[1]))
						try:
							if int(date) >= 29 and int(date) << 30:
								if int(daylightsSavings[b-2]) - ((int(rows[int(date)-1][2].replace(" pm", "").split(":")[0])*60)+int(rows[int(date)-1][2].replace(" pm", "").split(":")[1])) >= 70:
									print('daylights savings ended')
									dlsBoolean = False
								elif ((int(rows[int(date)-1][2].replace(" pm", "").split(":")[0])*60)+int(rows[int(date)-1][2].replace(" pm", "").split(":")[1])) - int(daylightsSavings[b-2]) >= 70:
									print('daylights savings started')
									dlsBoolean = True
							else:
								if int(daylightsSavings[b-1]) - ((int(rows[int(date)-1][2].replace(" pm", "").split(":")[0])*60)+int(rows[int(date)-1][2].replace(" pm", "").split(":")[1])) >= 60:
									print('daylights savings ended')
									dlsBoolean = False
								elif ((int(rows[int(date)-1][2].replace(" pm", "").split(":")[0])*60)+int(rows[int(date)-1][2].replace(" pm", "").split(":")[1])) - int(daylightsSavings[b-1]) >= 60:
									print('daylights savings started')
									dlsBoolean = True
						except:
							b=b
						print(f'{monthOrder[b]} {yearsOrder[a]}: sunrise: {rows[int(date)-1][1]}, sunset: {rows[int(date)-1][2]}, daylight total: {rows[int(date)-1][3]}')
					except:
						print(f'{monthOrder[b]} {yearsOrder[a]}: unable to find date')
						sunsets.append('none')
						sunrises.append('none')
					dlsArray.append(dlsBoolean)
				for c in range(len(sunsets)):
					if sunsets[c] != 'none':
						sunsets[c] += 660
						if dlsArray[c] == False:
							sunsets[c] += 60
						pygame.draw.circle(surface, 'PURPLE', (((((screenReslution[1]-spacer)-spacer)/int(len(monthOrder)))*(c+1))+spacer, (screenReslution[0]-spacer)-((((screenReslution[0]-spacer)-spacer)/24)*((sunsets[c])/60))), 3)
				for c in range(len(sunrises)):
					if sunrises[c] != 'none':
						if dlsArray[c] == False:
							sunrises[c] += 60
						pygame.draw.circle(surface, 'RED', (((((screenReslution[1]-spacer)-spacer)/int(len(monthOrder)))*(c+1))+spacer, (screenReslution[0]-spacer)-((((screenReslution[0]-spacer)-spacer)/24)*((sunrises[c])/60))), 3)
				pygame.display.flip()
				print(f'{str(sunsets)}\n{str(dlsArray)}\n{str(date)} - {yearsOrder[a]}')
				#solve for max and min (has to do it itself to not break after the 28th day)
				lowest,greatest = sunsets[0],sunsets[0]
				for c in range(len(sunsets)):
					if sunsets[c] != 'none':
						if sunsets[c] >= greatest:
							greatest = sunsets[c]
						if sunsets[c] <= lowest:
							lowest = sunsets[c]
				print(f'sunset equation: y={round((greatest-lowest)/2)}sin({round(360/12)}(x+{((sunsets.index(find_nearest(sunsets, ((greatest+lowest)/2))))+1)*-1}))+{round((greatest+lowest)/2)}')
				print(f'sunset equation: y={round((greatest-lowest)/2)}cos({round(360/12)}(x+{((sunsets.index(find_nearest(sunsets, ((greatest+lowest)/2))))+1)*-1})-90)+{round((greatest+lowest)/2)}')
				lowest,greatest = sunrises[0],sunrises[0]
				for c in range(len(sunrises)):
					if sunrises[c] != 'none':
						if sunrises[c] >= greatest:
							greatest = sunrises[c]
						if sunrises[c] <= lowest:
							lowest = sunrises[c]
				print(f'sunrise equation: y={round((greatest-lowest)/2)}sin({round(360/12)}(x+{((sunrises.index(find_nearest(sunrises, ((greatest+lowest)/2))))+1)*-1}))+{round((greatest+lowest)/2)}')
				print(f'sunrise equation: y={round((greatest-lowest)/2)}cos({round(360/12)}(x+{((sunrises.index(find_nearest(sunrises, ((greatest+lowest)/2))))+1)*-1})-90)+{round((greatest+lowest)/2)}')
				input('\nPress enter to continue')
		else:
			print('Please input a vaild date')
	except:
		print('Please input a valid number')
