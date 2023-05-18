import sys

if len(sys.argv) == 1:
    print("Error1: Any number is provided. You should enter two numbers.")
    sys.exit

elif len(sys.argv) > 3:
    print("Error2: You provided more than two arguments. You should enter two numbers.")
    sys.exit()

elif len(sys.argv) == 2:
    print("Error3: You can not provide one argument. You should enter two numbers.")
    sys.exit()

# elif (sys.argv[1]).isnumeric() == False or (sys.argv[2]).isnumeric() == False:
#     print("Error4: You can not provide a string. You should enter a numbers.")
#     sys.exit()

else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except Exception:
        print("Error4: You can not provide a incorrect argument. You should enter two numbers.")
        exit()
    print("Suma:\t\t", a+b)
    print("Diferencia:\t", a-b)
    print("Multiplicación:\t", a*b)
    try:
        print("Cociente:       ",    a/b)
    except ZeroDivisionError:
            print("Cociente:\t Error5: Zero Division.")
    try:
        print("Resto:          ",   a%b)
    except ZeroDivisionError:
        print("Resto:\t\t Error6: Zero Module.")

    sys.exit()