file_read = open('Codingal.txt', 'r')
print ("file in read mode -")
print (file_read.read())
file_read.close()




file_write = open('Codingal.txt', 'w')
file_write.write( "file in write mode ")
file_write.write("Hi i am penguin and i am 1 years old")
file_write.close()



file_append = open ('codingal.txt', 'a')
file_append.write("\n file in appaend mode ")
file_append.write("\n Hi i am penguin and i am 1 years old")
file_append.close()




