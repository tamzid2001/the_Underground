a = raw_input("string, plz: ")
reverse = ''

for char in a:
    reverse = char + reverse

if reverse == a:
    print a, "is a palindrome"
else:
    print a, "is not a palindrome"
