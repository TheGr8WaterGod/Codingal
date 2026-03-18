file1 = open('Codingal.txt', 'r')
file2 = open('Codingalupdated.txt ','w')



for line in file1.readlines():


    if not line.startswith('Coding'):


        file2.write(line)


file1.close()
file2.close()