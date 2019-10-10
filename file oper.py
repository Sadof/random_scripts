file = open("input.txt")
file1 = open("output.txt", 'w')
arr = []
string = ''
a = 0
for line in file:
    arr.append(line)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != '\n':
            a = int(arr[i][j])+1
            string += str(a)
        else:
            string += '\n'
    file1.write(string)
    string = ''
file.close()
file1.close()
