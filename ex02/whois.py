import sys


if (len(sys.argv) != 2):
    if (len(sys.argv) > 2):
        print('Error: More than one argument are provided.')    
        exit()
    print("Error: You must provide one integer as an argument.")
    exit()

try:
    assert sys.argv[1].isnumeric()
except AssertionError:
    print("Error: argument is not an integrer")
    exit()

if (sys.argv[1] == "0"):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")