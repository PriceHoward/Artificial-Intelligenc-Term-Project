import RPi.GPIO as GPIO
import time

def GPIOPinSetup():
    GPIO.setmode(GPIO.BCM)
    greenLED = 17
    blueLED = 27
    redLED = 22
    sensorS1 = 23
    sensorS2 = 24
    sensorOut = 25
    GPIO.setup(greenLED, GPIO.OUT)
    GPIO.setup(blueLED, GPIO.OUT)
    GPIO.setup(redLED, GPIO.OUT)
    GPIO.setup(sensorOut, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(sensorS2, GPIO.OUT)
    GPIO.setup(sensorS1, GPIO.OUT)
    



def colorPicker(color):
    if(color == 'red' or color == 'RED'):
        GPIO.output(redLED, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(redLED, GPIO.LOW)

    elif(color == 'blue' or color == 'BLUE'):
        GPIO.output(blueLED, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(blueLED, GPIO.LOW)

    elif(color == 'green' or color == 'GREEN'):
        GPIO.output(greenLED, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(greenLED, GPIO.LOW)
#def writeFile(color):
 #   outFile = open('projectDataFile.txt', 'a')
  #  for line in color:
   #     outFile.write(color)
    #    outFile.write(' ')
def main():
    GPIoPinSetup()
    color = input('Please input the color you would like to be displayed: ')
    colorPicker(color)
   # writeFile(color)
    GPIO.cleanup()
    

main()
