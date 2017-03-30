n = int(raw_input("enter # posts: "))

if n < 0:
    print "error"
elif n == 0:
    print " "
else:
    print "|",

print "--- | " * (n - 1)
