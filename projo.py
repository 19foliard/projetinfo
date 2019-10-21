import autograd
from autograd import numpy as np
import matplotlib.pyplot as plt

def find_seed(g, c=0, eps = 2**(-26)) :
    # On cherche le réel t tq f(0,t) = c par dichotomie
    a = 0
    b = 1
    if not (g(a) <= c <= g(b) or g(a) >= c >= g(b)) :
        return None
    while b-a > 2*eps :
        t = (b+a) / 2
        if g(t) > c :
            b = t
        elif g(t) < c :
            a = t
        elif g(t) == c :
            return t
    return (b+a) / 2

#NB : Ici la condition "raisonnable" provient du TVI : c compris entre f(0,1) et f(0,0) => t existe

def distance2(a, b) :
    return (a[0] - b[0])**2 + (a[1]-b[1])**2

def perpendicular( a ) :
    b = np.array([-a[1], a[0]])
    c = np.array([a[1], -a[0]])
    return b, c


def simple_contour(f, c=0.0, delta=0.01) :

    def g(y) :
        return f(0, y)

    if find_seed(g, c) == None :
        return None

    X = [0]
    Y = [find_seed(g, c)]
    tg_tuple = perpendicular(grad_f(X[0], Y[0]))
    if tg_tuple[0][0] >= 0 :
        X.append(tg_tuple[0][0])
        Y.append(tg_tuple[0][1])
    else :
        X.append(tg_tuple[1][0])
        Y.append(tg_tuple[1][1])

    while False :
        gradient = grad_f(X[-1], Y[-1])
        tg_tuple = perpendicular(gradient)
        adernier = [X[-2], Y[-2]]
        dernier = [X[-1],Y[-1]]

        if distance2(adernier, tg_tuple[])


# Attention on a un pb si le gradient devient nul : comment tu définis la tangente ?

def grad_f(x,y) :
    g = autograd.grad
    return np.r_[g(f, 0)(x, y), g(f, 1)(x, y)]

def f(x, y) :
    return np.sin(x) + 2.0 * np.sin(y)