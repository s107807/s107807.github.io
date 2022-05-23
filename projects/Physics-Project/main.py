import pyaudio, os, threading, csv, sys, time
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
		time.sleep(0.05)

p = pyaudio.PyAudio()
clear()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 10.0  # in seconds, may be float
f = 256.0        # sine frequency, Hz, may be float
environments = [['water', 1480], ['air', 345], ['steel', 5960], ['rock', 4470.4]]
c = 1480

mode = 'menu'
modes = ['menu', 'play-sound', 'song-player', 'environment-changer']
while True:
	if mode == 'menu':
		delayPrint('The Frequency of Sines - A Physics Attempt on Music\n\nBy Will Hellinger & John Bieberich:\n\n')
		environmentFound = False
		for s in range(len(environments)):
			if environments[s][1] == c:
				environmentFound = True
				delayPrint(f'1. Play a specific frequency\n2. Play a song(csv file)\n3. Change Environment - (Current Environment - {environments[s][0]})\n\n')
		if environmentFound == False:
			delayPrint('1. Play a specific frequency\n2. Play a song(csv file)\n3. Change Environment - (Current Environment - unknown)\n\n')
		try:
			delayPrint('Please select a choice: ')
			mode = modes[int(input(''))]
			clear()
		except:
			delayPrint('Please enter a real number')
	elif mode == 'play-sound':
		delayPrint('Sound Player\n\n')
		while True:
			stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs,output=True)
			stop = False
			try:
				delayPrint('frequency: ')
				f = input('')
				if f == 'back':
					mode = 'menu'
					clear()
					break
				f = float(f)
			except:
				stop = True
				delayPrint('please input a valid number\n')
			if stop == False:
				samples = (np.cos((2*np.pi*np.arange(fs*(f/(c/345)))*duration/fs))).astype(np.float32)
				stream.write(volume*samples)
			stream.stop_stream()
			stream.close()
	elif mode == 'song-player':
		stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs,output=True)
		while True:
			delayPrint('song: ')
			song = str(input(''))
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
				break
			except:
				delayPrint('please input a valid file')
		try:
			for s in range(len(rows)):
				samples = (np.cos((2*np.pi*np.arange(fs*(float(rows[s][1])/(c/345)))*float(rows[s][0])/fs))).astype(np.float32)
				stream.write(volume*samples)
		except:
			continue
		stream.stop_stream()
		stream.close()
	elif mode == 'environment-changer':
		environmentFound = False
		for s in range(len(environments)):
			if environments[s][1] == c:
				environmentFound = True
				delayPrint(f'Current Environment - {environments[s][0]}\n')
		if environmentFound == False:
			delayPrint('Current Environment - unknown\n')
		delayPrint('Available Environments: ')
		for s in range(len(environments)):
			if s != len(environments)-1:
				delayPrint(f'{environments[s][0]}, ')
			else:
				delayPrint(f'and {environments[s][0]}.\n\n')
		while True:
			delayPrint('Please enter a new environment: ')
			environmentFound = False
			userInput = str(input(''))
			for s in range(len(environments)):
				if environments[s][0] == userInput:
					c = float(environments[s][1])
					mode = 'menu'
					environmentFound = True
			if environmentFound == True:
				break
			
