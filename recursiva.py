def fatorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*fatorial(x-1)    
    
print(fatorial(3))

############################################

def reverse(x):
    if len(x)==1:
        return x
    else:
        return x[-1]+reverse(x[:-1])
    

print(reverse("world"))


############################################

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
#########################################
def soma(w):
     if w==[]:
        return 0
    else:
        return w[0]+soma(w[1:])

##########################################

def conta(w,n):
    if w==[]:
        return 0
    elif w[0]==n:
         return 1+conta(w[1:],n)
    else:
        return 0+conta(w[1:],n)
    
#######################################

def flatten(w):
    if w==[]:
        return []
    elif isinstance(w[0], list):
        return flatten(w[0]) + flatten(w[1:])
    else:
        return [w[0]]+flatten(w[1:])
    
####################

def power(x,n):
    if n==0:
        return 1
    elif x==1:
        return 1
    else: 
        return x*power(x,n-1)

    