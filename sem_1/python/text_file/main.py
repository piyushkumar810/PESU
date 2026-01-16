file=open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\text_file\\file.txt","w")
# read_file=file.read()
# read_file=file.read(-1)
# read_file=file.read(100)
# read_file=file.readline(4)
# read_file=file.readlines(30)
# read_file=file.readlines(31)

#--------------------------- writing to a file
# read_file=file.write("i love you")
read_file=file.writelines(["i love \n","yes i know"])


print(read_file)
print(type(read_file))
file.close()
print(file.closed)