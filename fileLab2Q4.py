txtfile = raw_input("edit: ")
txt = open(txtfile, 'r')

newtxt = txt.read()
txt.close()

txt = open(txtfile, 'w')

txt.write(newtxt.replace(' ',''))
txt.close()
