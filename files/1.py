file_read = open('white.txt', 'r')
print("File in read mode-")
print(file_read.read())
file_read.close()

file_write = open('white.txt', 'w')
file_write.write("File in write mode- \n")
file_write.write("I am a Penguin")
file_write.close()

file_append = open('white.txt', 'a')
file_append.write("File in append mode- \n")
file_append.write("I am 1 year old \n")
file_append.close()