import os

f = open("D:\\study material\\Scarping\\SEC\\filing_urls.txt", 'r')

# Reading fixed or all number of charachter from file
print(f.read(50))

# Reading first line of file
print(f.readline())

# looping through file line by line
for i in f:
    print(i)

f.close() #closing file after using it

# Appending more content to it
f = open("D:\\study material\\Scarping\\SEC\\filing_urls.txt", 'a')
f.write("Now the file has more content!")
f.close()

# Open the file "demofile3.txt" and overwrite the content
f = open("filing_urls.txt", 'w')
f.write("Woops! I have deleted the content!")
f.close()

# "x" - Create - will create a file, returns an error if the file exist

# "w" - Write - will create a file if the specified file does not exist

f = open('mytxt.txt', 'w')
f.write('How are you? I am fine!!')
f.close()

# Reomving file from system
os.remove('filing_urls.txt')

# Remove the folder "myfolder":
os.rmdir("dumb")

# Addin folder
os.mkdir('dumb')

# Using with automatically closes the file
with open('data.txt', 'r') as file1:
    # data = file1.readlines()
    # data = file1.readline()
    data = file1.read()

    name = file1.name
    mode = file1.mode
    print(data)
    print(name)
    print(mode)

print(file1.closed)