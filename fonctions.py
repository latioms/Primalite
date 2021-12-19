import sys, math    
from random import randrange
def afficherTab(tab):
   for elt in tab:
      print(str(elt), ", ");
   print()

def miller_rabin(n, k):
   """ en entree : n l'entier a tester
                           k le compteur
       en sortie: un booleen (True si premier)"""
   if n == 2 or n ==3 :
       return True
   if n % 2 == 0:
       return False
   r, s = 0, n - 1
   while s % 2 == 0:
       r += 1
       s //= 2                     
       # la partie non paire de n-1 / permet la factorisation en nombre premier
   for _ in range(k):
       a = randrange(2, n - 1)     
       x = pow(a, s, n)            
       if x == 1 or x == n - 1:
           continue                
       for _ in range(r - 1):      
           x = pow(x, 2, n)        
           if x == n - 1:
               break               
       else:
           return False            
   return True

def estCarmichael(c):
    m=c
    if m%2==0 or c==1: return 0
    q=3
    while m>1:
        if q**2>m:
            if m==c:
                return 0
            elif (c-1)%(m-1) != 0:
                return 0
            else:
                return 1
        elif m%q==0:
            m=m//q
            if m%q==0 or (c-1)%(q-1)!=0: return 0
        q+=2
    return 1

def ListeCharmichael(n):
    tab = []
    for i in range(1,n):
        if estCarmichael(i):
            tab.append(i)
    if len(tab) == 0:
        print("Il n'ya aucun nombre de Carmichael jusquá ce seuil")
    else:
        print("La liste des Nombres de Charmichael jusqu'a ce seuil est: \n")
        print(str(tab))
    return tab


def isPrime(n):
    if n == 1: return False
    return not [x for x in range(2,int(math.sqrt(n)))if n%x == 0]

def factorize(n):
    primes = []
    candidates = range(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes.append(candidate)
            primes = primes + factorize(int(n/candidate))
        candidate += 1
    print(str(primes))         
    return primes

def main():
    pass

if __name__ == '__main__':
    sys.exit(main())
