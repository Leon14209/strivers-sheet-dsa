#count sum of n nos
"""def reccount(n):
    if n==0:
        return 0
    return n+ reccount(n-1)"""


#FACTORIAL
"""def recfac(n):
    if n==0:
        return 1
    return n*recfac(n-1)
print(recfac(5))"""


#ARRAYSUM USING RECURSION
"""def recarrsum(n):
    if len(n)==0:
        return 0
    k=n.pop
    return n.pop()+recarrsum(n)
print(recarrsum([2,3,4,89,90,1]))"""


#REVERSE STR RECURSIVELY
""""def recrevstr(n):
    if len(n)==0:
        return ""
    k=list(n)
    return k.pop()+recrevstr(n[:-1])
print(recrevstr("leon")"""


#PALINDROME CHECK
"""def recpalincheck(n):
    if len(n)==0:
        return True
    elif len(n)==1:
        return True
    elif n[0]==n[-1]:
        return recpalincheck(n[1:-1])
    else:
        return False    
print(recpalincheck("leonoel")"""


#PRIME CHECK
"""def recprimecheck(n,i=2):
    if (n)<2:
        return False
    elif (n**0.5)<i:
        return True
    elif n%i!=0:
        return recprimecheck(n,i+1)
    else:
        return False    
print(recprimecheck(8087))"""




#REVERSE ARR OF NUMS
"""def recrevstr(n):
    if len(n)==0:
        return []
    k=list(n)
    return [k.pop()]+recrevstr(n[:-1])
print(recrevstr([1,2,3,4,5,6]))"""


#CHECK IF SORTED
"""def recsorted(n):

    if len(n)==1:
        return True
    if n[0]<n[1]:
       return recsorted(n[1:])
    else:
        return False
print(recsorted([1,2,3,4,7,6]))"""


#SUM TILL ONE DIGIT
"""def sumdigits(n):
    if n < 10:
        return n
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return sumdigits(s)
print(sumdigits(9875))"""

#FIB
"""def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(10))"""

