"""
Price Howard
11/30/2020
CS 470 Artificial Intelligence Term Project
"""
"""
Snipits of code for the loop function and the GPIO ports were found here. That code was written by: elktros the Administrator of electronicshub.org
https://www.electronicshub.org/raspberry-pi-color-sensor-tutorial/
"""

import RPi.GPIO as GPIO
import time
import random

"""
This section is used to create the lists and variables
"""

listOfAvailabaleColors = ['RED','BLUE', 'GREEN']
colorAList = []
colorBList = []
colorCList = []
colorGuessedByAI = []
wasColorCorrect = []
flag = 0
breakFlag = 0
guessedCorrect = ''
s2 = 5
s3 = 6
signal = 13
NUM_CYCLES = 10
GPIO.setwarnings(False)

"""
Name: writeToFile
Purpose: To write the data that has been guessed to a file to show the training data and how fast the AI caught on to the data.
Input: colorA (float), colorB (float), colorC (float), guessedColor (String), correctColor (Boolean)
Return: N/A
"""

def writeToFile(colorA, colorB, colorC, guessedColor, correctColor ):
    f = open("RGBColorData.txt", 'a')
    f.write(str(colorA)+'\n')
    f.write(str(colorB)+'\n')
    f.write(str(colorC)+'\n')
    f.write(guessedColor+'\n')
    f.write(str(correctColor) + '\n')
    f.close()

"""
Name: setup
Purpose: To setup the GPIO ports on a Raspberry Pi.
Input: N/A
Return: N/A
"""


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("Setup Complete")

"""
Name: guessColor
Purpose: To have the AI guess the color given to it by the sensor on the breadboard by taking in three values and guessing the RGB color. The values are stored into lists.
Input: colorA, colorB, colorC
Return: N/A
"""

def guessColor(colorA, colorB, colorC):
    flag = 0
    breakFlag = 0
    if(len(colorGuessedByAI) == 0):
        guessedColor = random.choice(listOfAvailabaleColors) #AI choses a random color to guess form the list of colors.
        print("Guess Color: " + guessedColor)
        print("Guessed Correct? (Input Yes or No)")
        guessedCorrect = raw_input()
        colorAList.append(colorA)
        colorBList.append(colorB)
        colorCList.append(colorC)
        colorGuessedByAI.append(guessedColor)
        if(guessedCorrect == 'Yes' or guessedCorrect == 'YES' or guessedCorrect == 'yes'):
            wasColorCorrect.append(True)
            writeToFile(colorA, colorB, colorC, guessedColor, True)
        elif(guessedCorrect == 'No' or guessedCorrect == 'NO' or guessedCorrect == 'no'):
            wasColorCorrect.append(False)
            writeToFile(colorA, colorB, colorC, guessedColor, False)

    else:
        for i in range (len(wasColorCorrect)): # AI checks for previously matching data.
            if(wasColorCorrect[i] == True and breakFlag == 0):
                if(colorGuessedByAI[i] == "RED"):
                    flag = 1
                    if(colorA >= (colorAList[i] - 2000) and colorA <= (colorAList[i] + 2000)):
                        guessedColor = colorGuessedByAI[i]
                        print("Guessed Color: " +  colorGuessedByAI[i])
                        print("Guessed Correct? (Input Yes or No)")
                        guessedCorrect = raw_input()
                        print("Red test")
                        colorAList.append(colorA)
                        colorBList.append(colorB)
                        colorCList.append(colorC)
                        colorGuessedByAI.append(colorGuessedByAI[i])
                        if(guessedCorrect == 'Yes' or guessedCorrect == 'YES' or guessedCorrect == 'yes'):
                            wasColorCorrect.append(True)
                            breakFlag = 1
                            writeToFile(colorA, colorB, colorC, guessedColor, True)
                        elif(guessedCorrect == 'No' or guessedCorrect == 'NO' or guessedCorrect == 'no'):
                            wasColorCorrect.append(False)
                            breakFlag = 1
                            writeToFile(colorA, colorB, colorC, guessedColor, False)
                    else:
                        flag = 0

                if(colorGuessedByAI[i] == "BLUE"):
                    flag = 1
                    if(colorB >= (colorBList[i] - 2000) and colorB <= (colorBList[i] + 2000)):
                        guessedColor = colorGuessedByAI[i]
                        print("Guessed Color: " +  colorGuessedByAI[i])
                        print("Guessed Correct? (Input Yes or No)")
                        guessedCorrect = raw_input()
                        print("Blue Test")
                        colorAList.append(colorA)
                        colorBList.append(colorB)
                        colorCList.append(colorC)
                        colorGuessedByAI.append(colorGuessedByAI[i])
                        if(guessedCorrect == 'Yes' or guessedCorrect == 'YES' or guessedCorrect == 'yes'):
                            wasColorCorrect.append(True)
                            breakFlag = 1
                            writeToFile(colorA, colorB, colorC, guessedColor, True)
                        elif(guessedCorrect == 'No' or guessedCorrect == 'NO' or guessedCorrect == 'no'):
                            wasColorCorrect.append(False)
                            breakFlag = 1
                            writeToFile(colorA, colorB, colorC, guessedColor, False)
                    else:
                        flag = 0
                        
                if(colorGuessedByAI[i] == "GREEN"):
                    flag = 1
                    if(colorC >= (colorCList[i] - 1500) and  colorC <= (colorCList[i] + 1500)):
                        print(colorCList[i] - 1500)
                        guessedColor = colorGuessedByAI[i]
                        print("Guessed Color: " +  colorGuessedByAI[i])
                        print("Guessed Correct? (Input Yes or No)")
                        guessedCorrect = raw_input()
                        print("Green Test")
                        colorAList.append(colorA)
                        colorBList.append(colorB)
                        colorCList.append(colorC)
                        colorGuessedByAI.append(colorGuessedByAI[i])
                        if(guessedCorrect == 'Yes' or guessedCorrect == 'YES' or guessedCorrect == 'yes'):
                            wasColorCorrect.append(True)
                            breakFlag = 1
                            writeToFile(colorA, colorB, colorC, guessedColor, True)
                        elif(guessedCorrect == 'No' or guessedCorrect == 'NO' or guessedCorrect == 'no'):
                            wasColorCorrect.append(False)
                            breakFlag = 1
                            writeToFile(colorA, colorB, colorC, guessedColor, False)
                    else:
                        flag = 0



        if(flag == 0 and breakFlag != 1): # Used if the AI could not find any previously matching data.
           guessedColor = random.choice(listOfAvailabaleColors)
           print("Guess Color: " + guessedColor)
           print("Guessed Correct? (Input Yes or No)")
           guessedCorrect = raw_input()
           print("Guessed Random")
           colorAList.append(colorA)
           colorBList.append(colorB)
           colorCList.append(colorC)
           colorGuessedByAI.append(guessedColor)
           if(guessedCorrect == 'Yes' or guessedCorrect == 'YES' or guessedCorrect == 'yes'):
               wasColorCorrect.append(True)
               writeToFile(colorA, colorB, colorC, guessedColor, True)
           elif(guessedCorrect == 'No' or guessedCorrect == 'NO' or guessedCorrect == 'no'):
               wasColorCorrect.append(False)
               writeToFile(colorA, colorB, colorC, guessedColor, False)

"""
Name: loop
Purpose: To continue looping and grabbing the set of three floats from the sensor then calling the guessColor function.
Input: N/A
Return: N/A
"""

def loop():
  temp = 1
  while(1):  

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start 
    colorA  = NUM_CYCLES / duration   
    print("Color A: " + str(colorA))

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    colorB = NUM_CYCLES / duration
    print('Color B: ' + str(colorB)) 

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    colorC = NUM_CYCLES / duration
    print("Color C: " + str(colorC))
    print("------------------------------")
      
    if colorA<12000 and colorB<12000 and colorC<12000:
      print("place the object.....")
      time.sleep(6)

    else:
        guessColor(colorA, colorB, colorC)



def main():
    setup()
    loop()
main()
