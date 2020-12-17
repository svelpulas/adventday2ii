f = open("adventday2.txt","r")
correct = 0
incorrect = 0
lines = f.readlines()
for x in range(0, len(lines)):
    count = 0
    newline1 = lines[x].split(' ')
    newline2 = newline1[0].split('-')
    firstnum = int(newline2[0])
    secnum = int(newline2[1])
    newline3 = newline1[1].split(':')
    alphabet = newline3[0]
    alplen = int(len(newline1[2]))
    if (alphabet == newline1[2][firstnum-1]) and (alphabet == newline1[2][secnum-1]):
        incorrect = incorrect + 1
    elif (alphabet == newline1[2][firstnum-1]):
        correct = correct + 1
    elif (alphabet == newline1[2][secnum-1]):
        correct = correct + 1
print(len(lines))
print(correct)
print(incorrect)