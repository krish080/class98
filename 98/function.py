#how to read the entirle file usingfunctions

#openFile = open("sample.txt")

#fileLines = openFile.readlines()

#for line in fileLines:
  #      print(line)


#introString ="Hey!, My name is Coding. I am 12 years old. I like python"
#words = introString.split(".")
#print(words)


#def functionName():
#    block of Conten

#def functionName(variable):
    #block of coding

#def greet(name):
 #   #print("Hello," +name+ "How are you?")


#greet("Krish")

#countWords from file


def testfile():
    fileName = input("enter the file name: ")
    
    numwod=0

    file = open(fileName, 'r')
    for line in file:
         words=line.split()
         numwod = numwod +len(words)
 
        
    print("Number of words: " )
    print(numwod)
testfile()

