n = int(raw_input('enter a number: '))
line = 'BW' * n

for i in range(0,n):
   if i % 2 == 0:
      print line[:n]
   else:
      print line[1:n+1]
