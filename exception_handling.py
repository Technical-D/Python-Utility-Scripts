
try:
    f = open("data.txt", 'w')
    f.write("My text file is found!!!")

except Exception as e:
    print(e)
else:
    print("Text added in file sucessfully!!")
finally:
    f.close()