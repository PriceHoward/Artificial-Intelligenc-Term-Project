import RPi.GPIO as GPIO
import time as time
import random
sensorS2 = 6   #Global Variables used for GPIO port clarification.
sensorS3 = 13
signal = 5
NUM_CYCLES = 10

#Global Array Variables.
ClassificationColorList = {'BLUE','RED','RED','GREEN','BLUE','GREEN','BLUE','RED','GREEN'}
listOfAvailabaleColors = {'RED','BLUE', 'GREEN'}
colorAList = {}
colorBList = {}
colorCList = {}
colorGuessedByAI = {}
wasColorCorrect = {}


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(sensorS2,GPIO.OUT)
  GPIO.setup(sensorS3,GPIO.OUT)
  print("GPIO has been Setup.")


def pickColor(colorA, colorB, colorC):
    if(len(colorGuessedByAI) == 0):
        guessedColor = random.choice(listOfAvailabaleColors)
        if(guessedColor = ClassificationColorList{0}):
            colorAList.append(colorA)
            colorBList.append(colorB)
            colorCList.append(colorC)
            colorGuessedByAI.append(guessedColor)
            wasColorCorrect.append(True)
        else:
            colorAList.append(colorA)
            colorBList.append(colorB)
            colorCList.append(colorC)
            colorGuessedByAI.append(guessedColor)
            wasColorCorrect.append(False)
    elif(len(colorGuessedByAI) > 0):
    #compare colorA from the list to see if the number given.
    #Do the same for colorB and colorC
    #check color by 5 to 10 thousand more to 5 thousand less
    #Guess the color by the compared numbers.
    #Pray that it guesses the correct numbers.



        

def loop():
  temp = 1
  while(1):  

    GPIO.output(sensorS2,GPIO.LOW)
    GPIO.output(sensorS3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start 
    colorA  = NUM_CYCLES / duration   
   
    GPIO.output(sensorS2,GPIO.LOW)
    GPIO.output(sensorS3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    colorB = NUM_CYCLES / duration
    

    GPIO.output(sensorS2,GPIO.HIGH)
    GPIO.output(sensorS3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    colorC = NUM_CYCLES / duration
    

    
    
    if colorA<7000 and colorB<7000 and colorC12000:
      print("red")
      temp=1
    elif colorA<12000 and  colorB<12000 and colorC>12000:
      print("green")
      temp=1
    elif colorC<7000 and colorA<7000 and colorB>12000:
      print("blue")
      temp=1
    elif colorA>10000 and colorC>10000 and colorB>10000 and temp==1:
      print("place the object.....")
      temp=0




def main():
    print("Here just to save")

main()







      
