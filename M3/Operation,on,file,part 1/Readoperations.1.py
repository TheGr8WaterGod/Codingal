file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print("\n read in parts \n")
print(file.read(9))
file.close()

file = open('Codingal.txt', 'a')
file.write("\n Hi i am penguin and i am 1 yr old.")
file.close