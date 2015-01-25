__author__ = 'ubuntu'

myfile = open("example.log", "w")
print ("file name", myfile.name)
print ("Colse or not", myfile.closed)
print ("opening mode", myfile.mode)

myfile.write ('This is my fisrt write operation')
myfile.close()

myfile = open("example.log", "r")

text_in_file = myfile.read()
print (text_in_file)
myfile.close()
