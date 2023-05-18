from loading import ft_progress 
from time import sleep

X = range(100)

def test_X(X):
    ret = 0
    for elem in ft_progress(X): 
        ret += (elem + 3) % 5 
        sleep(0.01)
    print()
    print(ret) 
