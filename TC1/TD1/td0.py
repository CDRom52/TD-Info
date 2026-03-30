import math
import random
import matplotlib.pyplot as plt
import numpy as np

"""
a = int(input('Donner un entier'))
if a % 2 == 0:
    print('pair')
else:
     print('impair')
"""
     
def quadratique(a, b, c):
    delta = b**2 - 4*a*c
    if delta >= 0:
        return (-b-math.sqrt(delta)) / 2*a, (-b+math.sqrt(delta)) / 2*a
    else:
        return 'pas de racines'
    
echantillon=[random.gauss(16,2) for n in range(100)]    
def moyenne(echantillon):
    m = 0
    for i in echantillon:
        m += i
    return m/len(echantillon)

def ecart_type(echantillon):
    m = moyenne(echantillon)
    L = [(i-m)**2 for i in echantillon]
    variance = moyenne(L)
    return math.sqrt(variance)

def ecart_type2(echantillon):
    s = 0
    m = moyenne(echantillon)
    for x in echantillon:
        s += x**2
    s = 1/len(echantillon) * s - m**2
    return math.sqrt(abs(s))

def convertir(S):
    assert(S.isdigit())
    if S[0]=="-":
        return (-1)*int(S[1:])
    else:
        return int(S)
    
def convertir2r(S):
    if S[0] == "-":
        return (-1)*float(S[1:])
    else:
        return float(S)
    
def empile(p, a):
    p.append(a)
    
def depile(p):
    try:
        p.pop()
        return p
    except:
        print("La pile est vide !")
        return None
    
def top(p):
    try:
        return p[0]
    except:
        print("La pile est vide !")
        return None
    
def est_vide(p):return p==[]

def init(*args):
    p = []
    if not args: return p
    for elem in args: p.append(elem)
    return list(p)

def factorielle(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def e(n):
    res = 0
    for i in range(n+1):
        res += 1/factorielle(i)
    return res
        
def nombre_premier(N):
    if N==1 or N==2:
        return True
    else:
        if N%2 == 0:
            return False
        elif math.sqrt(N)%1!=0:
            return False
        else:
            for i in range(1, math.sqrt(N)+1):
                if N%i==0:
                    return False
        return True
    
def div_propre(N):
    div = []
    res = True
    for i in range(2, N):
        if N%i==0:
            div.append(i)
            res = False
    return res, div, len(div)

def somDiv(N):
    a, b, c = div_propre(N)
    return sum(b)

def estParfait(N):
    return N == somDiv(N)

def estPremier(N):
    a, b, c = div_propre(N)
    return a

def estChanceux(a):
    for i in range(1, a-1):
        if not estPremier(a+i+i**2):
            return False
    return True
    

def moyennes(V1):
    N = len(V1)
    return [sum(V1[:i+1])/(i+1) for i in range(N)]

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

L = [(random.gauss(50, 50), random.gauss(50, 50)) for i in range(100)]

def kmeans(L, eps):
    m1 = L[random.randint(0, len(L))]
    m2 = L[random.randint(0, len(L))]
    fini = False
    old_m1, old_m2 = m1, m2
    while not fini:
        L1 = []
        L2 = []
        for i in L:
            if dist(i, m1) < dist(i, m2):
                L1.append(i)
            else:
                L2.append(i)
        m1 = (sum([i[0] for i in L1])/len(L1), sum([i[1] for i in L1])/len(L1))
        m2 = (sum([i[0] for i in L2])/len(L2), sum([i[1] for i in L2])/len(L2))
        if dist(m1, old_m1)<eps or dist(m2, old_m2)<eps:
            fini = True
        old_m1 = m1
        old_m2 = m2
        L = L1 + L2
    return m1, m2, L1, L2

m1, m2, L1, L2 = kmeans(L, 0.1)
plt.plot([i[0] for i in L], [i[1] for i in L], 'o')
plt.plot([i[0] for i in L1], [i[1] for i in L1], 'o')
plt.plot([i[0] for i in L2], [i[1] for i in L2], 'o')

def table(N):
    for x in range(1, N):
        print('{0:2d} {1:3d} {2:4f}'.format(x, x*x, math.sqrt(x)))

def proba(N):
    p = 0
    for i in range(N):
        if True:
            p = p + 1
    return p/N

def recherche_dicho(L):
    if L == []:
        return False
    N = len(L)
    m = L[N//2]
    if L[m]==L[N//2]:
        return True
    elif L[m]>L[N//2]:
        return recherche_dicho(L[N//2+1:])
    else:
        return recherche_dicho(L[:N//2])
