#Using file interface in Python which wraps an underlying interface


#write to a file call temp.txt
fileObject = open("temp.txt", 'w')
fileObject.write('hello world')
fileObject.close()


#open temp.txt and read from it
fileObject = open("temp.txt", 'r')
print(fileObject.read())
fileObject.close()