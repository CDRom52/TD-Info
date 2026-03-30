from math import sqrt;
# résolution équation quadratique
def trinome(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0.0:
        racine_delta = sqrt(delta)
        return (2, (-b-racine_delta)/(2*a), (-b+racine_delta)/(2*a))
    elif delta < 0.0: return (0,)
    else:
        return (1, (-b/(2*a)))
    
# --- Partie Principale ---------
if __name__ == "__main__":
    print(trinome(1.0, -3.0, 2.0))
    print(trinome(1.0, -2.0, 1.0))
    print(trinome(1.0, 1.0, 1.0))