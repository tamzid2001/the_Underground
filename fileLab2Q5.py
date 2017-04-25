txtfile = raw_input("scramble: ")
txt = open(txtfile, 'r')

newtxt = txt.read()
txt.close()

txt = open(txtfile, 'w')

'''
coding = {' ': '*', 'a': 'u', 'e': 'i'}

for k, v in coding.items():
    newtxt = newtxt.replace(k, v)
'''

coding = [[' ','*'],['a','u'],['e','i']]

for code in coding:
    newtxt = newtxt.replace(code[0], code[1])

txt.write(newtxt)
txt.close()
