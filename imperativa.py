# Imperative Algorithms Practice
# Francisco Marques - Biomedical Engineering @ IST
# December 2024
def maior2(w):
    maior=w[0]
    segundo=w[1]
    for num in w:
        if num>maior:
            segundo=maior
            maior=num
        elif num>segundo and num!=maior:
            segundo=num
    return segundo

print(maior2([1,4,2,3,5]))
#####################################
def is_palindrome(s):
    strip.s
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    else:
        return True
#####################################
def conta_pal(w):
    contagem={}
    for palavra in w:
        if palavra in contagem:
            contagem[palavra]+=1
        else:
            contagem[palavra] = 1
    return contagem
###################################
def filtra(d,x):
    w={}
    for chave, valor in d.items():
        if valor>x:
            w[chave]=valor
    return w
###################################
def inverte(w):
    d={}
    for chave, valor in w.items():
        d[valor]=chave 
    return d
################################
def merge(d1,d2):
    w={}
    for chave, valor in d1.items():
        w[chave]=valor
    for chave, valor in d2.items():
        if chave in w:
            w[chave]+=valor
        else: 
            w[chave]=valor
    return w
#################################
def agrupa_anagramas(w):
    d={}
    for palavra in w:
        chave="".join(sorted(palavra))
        if chave in d:
            d[chave]+=[palavra]
        else:
            d[chave]=[palavra]
    return list(d.values())
#################################
def agrupa_por_tamanho(w):
    d={}
    for palavra in w:
        chave=len(palavra)
        if chave in d:
            d[chave]+=[palavra]
        else:
            d[chave]=[palavra]
    return d
##############################
def duplicados(w):
    r=[]
    for i in range(len(w)):
        if w[i] not in r:
            for j in range(i+1,len(w)):
                if w[i] == w[j]:
                    r.append(w[i])
                    break
    return r
#############################
def intersecao(lista1, lista2):
    r=[]
    for i in range(len(lista1)):
        if lista1[i] not in r:
            for j in range(len(lista2)):
                if lista2[j]==lista1[i]:
                    r.append(lista1[i])
                    break
    return r 
################################
def remove_duplicados(w):
    r=[]
    for i in w:
        if i not in r:
            r.append(i)
    return r 
############################
def roda(w,n):
    if w==[]:
        return w
    n=n%len(w)  #eliminar rotações extra
    r=[]
    for i in range(len(w)-n,len(w)):
        r.append(w[i])
    for i in range(len(w)-n):
        r.append(w[i])
    return  r
##############################
def fib_iterativo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    anterior=0
    atual=1
    for i in range(2,n+1):
        próximo=anterior+atual
        anterior=atual
        atual=próximo
    return atual
########################
def inverte(w):
    if not w:
        return w
    r=[]
    for i in range(len(w)-1,-1,-1):
        r.append(w[i])
    return r
######################
def pares_inverso(w):
    r=[]
    for i in range(len(w)-1,-1,-1):
        if w[i]%2==0:
            r.append(w[i])
    return r
###################
def largest_substring(m,n):
    r=""
    for posição_m in range(len(m)):
        for tamanho in range(1,len(m)+1): #string has to be at least len=1
            substring = m[posição_m : posição_m + tamanho]
            if substring in n:
                if len(substring) > len(r):
                    r=substring
    return r
##################
#Longest Increasing Subsequence (lis)
def lis(w):
    au=len(w)*[1]
    for i in range(len(w)):
        for j in range(i): #prior position
            if w[j]<w[i]:
                au[i] = max(au[i], au[j] + 1)
    return max(au)
######################
#Coin Change
min_coins([1, 2, 5], 11)
# → 3
# Explanation: 5 + 5 + 1 = 11 (3 coins)
min_coins([2], 3)
# → -1
# Explanation: Impossible (can't make 3 with only 2-value coins)
min_coins([1, 3, 4], 6)
# → 2
# Explanation: 3 + 3 = 6 (2 coins)
min_coins([1, 5, 10, 25], 63)
# → 6
# Explanation: 25 + 25 + 10 + 1 + 1 + 1 = 63
def min_coins(coins,amount):
    dp=[float("inf")] * (amount+1) #creates a list with amount+1 positions all filled with "inf"
    dp[0]=0 #for 0 amount I nedd 0 coins
    for coin in coins:
        for i in range(1,amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[i]






                

            



                   
            

