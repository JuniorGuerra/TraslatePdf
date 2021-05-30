with open('file.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)