def readFile():
    fileReader = []
    inFile = open("projectDataFile.txt")
    for line in inFile:
        fileReader.append(line.split())
    inFile.close()
    return fileReader
#def writeFile():

def main():
    
    var = readFile()
    print(var[2])
    
main()
