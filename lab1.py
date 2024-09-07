my_file = open('./test.txt', 'w')

for i in range(0, 2000):
    stroke = str(i + 1)
    my_file.write(stroke + '\n')
    my_file.close()