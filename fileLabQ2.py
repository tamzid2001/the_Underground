orig = raw_input("orig: ")
origtxt = open(orig, 'r')

copy = raw_input("copy: ")
copytxt = open(copy, 'w')

copytxt.write(origtxt.read().upper())

copytxt.close()
