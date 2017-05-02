import operator
op_one = int(raw_input("1: "))
op_two = int(raw_input("2: "))
oper = raw_input("oper: ")

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

print "{} {} {} = {}".format(op_one, oper, op_two, ops[oper](op_one, op_two))
