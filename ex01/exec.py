import sys

def addargs(args):
    args = sys.argv[1:]
    x = " ".join(args)
    x = x.swapcase()
    return x

if __name__ == "__main__":
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 1:
        print(addargs(sys.argv)[::-1], end="\n")
