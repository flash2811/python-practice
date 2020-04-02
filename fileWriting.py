text = "sample Text to Save\n new line!"

#file is created
saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()

#appending
appendMe = '\nNew bit of information'
appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close()

#reading from a file
readMe = open('exampleFile.txt', 'r').read()
print(readMe)
