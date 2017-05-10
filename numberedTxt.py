f = open("data.txt", 'r')
newtxt = open("new_data.txt", 'w')

def numberedTxt():
    count = 1
    for line in f:
        newtxt.write(str(count) + ' ' + line)
        count += 1

numberedTxt()
newtxt.close()
