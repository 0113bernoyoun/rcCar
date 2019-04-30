import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

class wheelControl:
	wheelOne=None
	wheelTwo=None
	wheelPwm=None
	PwmFlag=None
	def addWheel(self,one,two,pwm):
		GPIO.setup(one,GPIO.OUT)
		GPIO.setup(two,GPIO.OUT)
		GPIO.setup(pwm,GPIO.OUT)

		self.wheelOne=one
		self.wheelTwo=two
		self.wheelPwm=pwm
		GPIO.output(self.wheelOne,False)
		GPIO.output(self.wheelTwo,False)

	def Go(self):

		GPIO.output(self.wheelOne,True)
		GPIO.output(self.wheelTwo,False)
		print(self.wheelOne)
		print(self.wheelTwo)
	def Stop(self):
		GPIO.output(self.wheelOne,False)
		GPIO.output(self.wheelTwo,False)
		print(self.wheelOne)
		print(self.wheelTwo)





def remoteGo(back_right,back_left,front_left,front_right):
	back_left.Go()
	back_right.Go()
	front_right.Go()
	front_left.Go()
def remoteStop(back_right,back_left,front_left,front_right):
	back_left.Stop()
	back_right.Stop()
	front_right.Stop()
	front_left.Stop()



front_left=wheelControl()
front_left.addWheel(8,25,7)

front_right=wheelControl()
front_right.addWheel(20,16,21)

back_left=wheelControl()
back_left.addWheel(5,6,13)

back_right=wheelControl()
back_right.addWheel(27,17,22)

pwm1=GPIO.PWM(7,30)
pwm1.start(30)
pwm2=GPIO.PWM(21,30)
pwm2.start(30)
pwm3=GPIO.PWM(13,30)
pwm3.start(30)
pwm4=GPIO.PWM(22,30)
pwm4.start(30)


while True:
	remoteGo(back_right,back_left,front_left,front_right)
	sleep(5)
	remoteStop(back_right,back_left,front_left,front_right)

	sleep(5)
