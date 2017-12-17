import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

StepPins = [7,11,13,15]
for pin in StepPins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)

StepLoop = 8
Seq_ccw = []
Seq_ccw = list(range(0, StepLoop))
Seq_ccw[0] = [1,0,0,0]
Seq_ccw[1] = [1,1,0,0]
Seq_ccw[2] = [0,1,0,0]
Seq_ccw[3] = [0,1,1,0]
Seq_ccw[4] = [0,0,1,0]
Seq_ccw[5] = [0,0,1,1]
Seq_ccw[6] = [0,0,0,1]
Seq_ccw[7] = [1,0,0,1]
Seq_cw = []
Seq_cw = list(range(0, StepLoop))
Seq_cw[0] = [0,0,0,1]
Seq_cw[1] = [0,0,1,1]
Seq_cw[2] = [0,0,1,0]
Seq_cw[3] = [0,1,1,0]
Seq_cw[4] = [0,1,0,0]
Seq_cw[5] = [1,1,0,0]
Seq_cw[6] = [1,0,0,0]
Seq_cw[7] = [1,0,0,1]


def movestep_ccw(steps):
	StepLooper = 0
	StepCounter = 0
	while StepCounter < steps:
		#print(StepLooper)
		for pin in range(0, 4):
			xpin = StepPins[pin]
			if Seq_ccw[StepLooper][pin]!=0:
				GPIO.output(xpin, True)
			else:
				GPIO.output(xpin, False)
		StepLooper += 1
		
		if (StepLooper==StepLoop):
			StepLooper = 0
		time.sleep(0.0015)
		StepCounter += 1
		

	for pin in StepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)

def movestep_cw(steps):
	StepLooper = 0
	StepCounter = 0
	while StepCounter < steps:
		#print(StepLooper)
		for pin in range(0, 4):
			xpin = StepPins[pin]
			if Seq_cw[StepLooper][pin]!=0:
				GPIO.output(xpin, True)
			else:
				GPIO.output(xpin, False)
		StepLooper += 1
		
		if (StepLooper==StepLoop):
			StepLooper = 0
		time.sleep(0.0015)
		StepCounter += 1
		

	for pin in StepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)





if __name__ == '__main__':
	movestep_ccw(4096)
	time.sleep(1)
	movestep_cw(4096)