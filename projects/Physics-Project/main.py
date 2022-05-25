import pyaudio, os, threading, csv, sys, time, urllib.request
import numpy as np

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def delayPrint(string):
	for a in string:
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(0.025)

p = pyaudio.PyAudio()
clear()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 10.0  # in seconds, may be float
f = 256.0        # sine frequency, Hz, may be float
environments = [['water', 1480], ['air', 345], ['steel', 5960], ['rock', 4470.4], ['vacuum', 0]]
c = 1480

if os.name == 'nt':
	name = __file__.replace('.py', '').split('\\')[len(__file__.replace('.py', '').split('\\'))-1]
else:
	name = __file__.replace('.py', '').split('/')[len(__file__.replace('.py', '').split('/'))-1]

print(name)

ignoreUpdate = True

if ignoreUpdate == False:
	try:
		writeFile = urllib.request.urlopen('https://s107807.github.io/projects/Physics-Project/main.py')
		readFile = open(f'{name}.py', 'w')
		for line in writeFile:
			readFile.write(str(line.decode("utf-8")))
		readFile.close()
		writeFile.close()
	except:
		#temp lol
		name = name

mode = 'menu'
modes = ['menu', 'play-sound', 'song-player', 'environment-changer']
while True:
	if mode == 'menu':
		delayPrint('The Frequency of Sines - A Physics Interpretation on Music\n\nBy Will Hellinger & John Bieberich:\n\n')
		environmentFound = False
		for s in range(len(environments)):
			if environments[s][1] == c:
				environmentFound = True
				delayPrint(f'1. Play a specific frequency\n2. Play a song(csv file)\n3. Change Medium - (Current Medium - {environments[s][0]})\n\n')
		if environmentFound == False:
			delayPrint('1. Play a specific frequency\n2. Play a song(csv file)\n3. Change Medium - (Current Medium - unknown)\n\n')
		try:
			delayPrint('Please select a choice: ')
			mode = modes[int(input(''))]
			clear()
		except:
			delayPrint('Please enter a real number\n ')
	elif mode == 'play-sound':
		delayPrint('Sound Player\n\n')
		while True:
			stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs,output=True)
			try:
				delayPrint('frequency: ')
				f = input('')
				if f == 'back':
					mode = 'menu'
					clear()
					stream.stop_stream()
					stream.close()
					break
				f = float(int(f))
				samples = (np.cos(2*np.pi*np.arange(fs*(duration/(c/345)))*f/fs)).astype(np.float32)
				stream.write(volume*samples)
			except:
				delayPrint('please input a valid number\n')
			stream.stop_stream()
			stream.close()
	elif mode == 'song-player':
		stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs,output=True)
		while True:
			delayPrint('song: ')
			song = str(input(''))
			if song == 'back':
				mode = 'menu'
				stream.stop_stream()
				stream.close()
				clear()
				break
			try:
				rows = []
				if os.name == 'nt':
					with open(f'.\\{song}.csv', 'r') as file:
						csvreader = csv.reader(file)
						header = next(csvreader)
						for row in csvreader:
							rows.append(row)
				else:
					with open(f'./{song}.csv', 'r') as file:
						csvreader = csv.reader(file)
						header = next(csvreader)
						for row in csvreader:
							rows.append(row)
				try:
					for s in range(len(rows)):
						samples = (np.cos((2*np.pi*np.arange(fs*(float(rows[s][1])/(c/345)))*float(rows[s][0])/fs))).astype(np.float32)
						stream.write(volume*samples)
				except:
					continue
				break
			except:
				delayPrint('please input a valid file\n')
		stream.stop_stream()
		stream.close()
	elif mode == 'environment-changer':
		environmentFound = False
		for s in range(len(environments)):
			if environments[s][1] == c:
				environmentFound = True
				delayPrint(f'Current Medium - {environments[s][0]}\n')
		if environmentFound == False:
			delayPrint('Current Medium - unknown\n')
		delayPrint('Available Mediums: ')
		for s in range(len(environments)):
			if s != len(environments)-1:
				delayPrint(f'{environments[s][0]}, ')
			else:
				delayPrint(f'and {environments[s][0]}.\n\n')
		while True:
			delayPrint('Please enter a new medium: ')
			environmentFound = False
			userInput = str(input(''))
			if userInput == 'back':
				mode = 'menu'
				clear()
				break
			for s in range(len(environments)):
				if environments[s][0] == userInput:
					c = float(environments[s][1])
					mode = 'menu'
					environmentFound = True
			if environmentFound == True:
				clear()
				break
