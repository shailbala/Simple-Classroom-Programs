from math import *

x1 = 1
x2 = 1
w1 = 0.5
w2 = 0.5
alpha = 0.5

## upto 5 decimal places, to reduce the number of iterations

def z(w1, w2):
    f = (x1*w1)+(x2*w2)
    return float(format(f, '.5f'))

def hx(z):
    f = 1/(1+exp(-z))
    return float(format(f, '.5f'))

def wnew(w, hx, x, y=1, alpha=0.5):
    f = w+alpha*(y-hx)*x
    return float(format(f, '.5f'))

znew = z(w1, w2)

h = hx(znew)
count = 0

while not hx(znew) == 1:
    print()
    print("x1: ",x1, "\tx2: ", x2, sep="")
    w1 = wnew(w1, h, x1)
    w2 = w1
    print("\tw1: ", w1, "\tw2: ", w2, sep="")
    znew = z(w1, w2)
    print("\tz: ", znew, sep="")
    print("\ta=h(x): ", hx(znew), sep="")
    count = count +1

print(count)

    
