# Function reads data from the file and decides if the file is empty or has data.
def readFile():
    fileReader = []
    emptyFile = True
    inFile = open("projectDataFile.txt")
    for line in inFile:
        if(line != ""):
            emptyFile = False
        else:
            break
        fileReader.append(line.strip())
    inFile.close()
    return emptyFile,fileReader

#Function writes data to the File.
def writeFile(dataList):
    outFile = open("projectDataFile.txt", "a")
    for line in dataList:
        outFile.write(line)
        outFile.write("\n")

#Function will be used for the AI to guess the color of the light.
def guessRGBColor():
    dataList = ['1500','365','1','Red','Blue']
    writeFile(dataList)


def main():
    emptyFile,var = readFile()
    if(emptyFile == True):
        guessRGBColor()
    print(emptyFile)
    
main()
