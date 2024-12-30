file = open("Nature.txt" ,"r")
print("File is running in reading Mode")
print(file.read())
file.close()

file = open("Nature.txt" ,"w")
print("File is running in writing Mode")
file.write("Nature is very Good Thing")
file.close()

file = open("Nature.txt" ,"a")
print("File is running in append Mode")
file.write(" \n Nature is very Good Thing it is good for our body")
file.close()