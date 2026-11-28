#PALINDROMESSSS
"""n=str(n)[::-1] if this is true then palindrome"""
#FACTORIAL IG
"""n = 5
k=n-1
g=n
while k!=0:
    g=g*(k)
    k=k-1
print((g))"""
#ARMSTRONG NO
"""n =153
s=0
k=len(str(n))
for i in str(n):
    s+=int(i)**k
if s==n:
    print(True)    
else:
    print(False)"""
#PERFECT NO
"""n=6
s=0
for i in range(1,(n//2)+1):
    if n%i==0:
        s+=i
if s==n:
    print(True) """
#PRIME NO CHECK
"""n=85768547
s=True
for i in range(2,(n//2)+1):
    if n%i==0:
        s=False
        break

print(s) """
#COUNT NO OF PRIMES
"""do 2 for loops """
#DO GCD

"""n1=9
n2=4
s=1
k=max(n1,n2)
for i in range(2,(k//2)+1):
    if n1%i==0 and n2%i==0:
        s=i
print(s)"""
#DO LCM
"""n1=9
n2=99
i=1
k=max(n1,n2)
while i%n1!=0 or i%n2!=0:
    i+=1
print(i)"""
#