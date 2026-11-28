"""
def pattern1( n):
        for i in range(1,n):
            for j in range(i):
                if (j)%2==0:                            
                
                    
                  print(1,end="")
                
                print(0,end="")  
            print()    

        
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")

            for j in range(2*(i)+1):
                print("*", end="")    

            print()




        for i in range(n):
            for j in range(i):
                print(" ", end="")

            for j in range(2*(n-i-1)+1):
                print("*", end="")

            print()
k=pattern1(5)    ALL THESE WERE EASY ONLY. NOW WE ENTER INTO MEDIUM      """   


"""n = 5
PROB 11

for i in range(n):                                                #
    for j in range(i+1):
        print((i+j+1) % 2, end=" ")
    print()
1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1  """  

#12
"""n=5
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")       

    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")    
    print()


1        1
12      21
123    321
1234  4321
1234554321"""   

#13
"""n=5
k=1
for i in range(n+1) :
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
1 

2 3 

4 5 6 

7 8 9 10 

11 12 13 14 15"""

#14
"""
A

AB

ABC

ABCD

ABCDE
for i in range(n+1):
    for j in range(i):
        print(chr(ord("A")+j),end="")
    print()   """


#15
#same as above but with n-i in j
#16
"""k=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(k),end="")

    print()  
    k+=1 
A

BB

CCC

DDDD

EEEEE"""

#17
"""n = 5

for i in range(1, n+1):

    for j in range(n-i):
        print(" ", end="")

    for j in range(i):
        print(chr(65+j), end="")

    for j in range(i-2, -1, -1):
        print(chr(65+j), end="")

    print()
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA"""


#18
"""for i in range(1,n+1):
    for j in range(i,0,-1):
        print(chr(65+n-j),end="")
    print()  
E 

D E 

C D E 

B C D E 

A B C D E   """ 

#19 print statemt lo * pettu
"""for i in range(1,n+1):

    for j in range(n+1-i):
        print(j+1,end="")       

    for j in range(2*(i-1)):
        print(" ",end="")
    for j in range(n+1-i,0,-1):
        print(j,end="")    
    print()


for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")       

    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")    
    print()
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********  """  

#NOW CORE ANTA
#20
"""
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")       

    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")    
    print()
for i in range(1,n):

    for j in range(n-i):
        print(j+1,end="")       

    for j in range(2*(i)):
        print(" ",end="")
    for j in range(n-i,0,-1):
        print(j,end="")    
    print()
12      21
123    321
1234  4321
1234554321
1234  4321
123    321
12      21
1        1  """  

#21
"""for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        print("*",end="")
        for j in range(n-2):
            print(" ", end="")
        print("*",end="")      
        print() 

*****
*   *
*   *
*   *
*****"""

#22
"""for i in range(-n+1, n):
    for j in range(-n+1, n):
        print(max(abs(i), abs(j)) + 1, end=" ")
    print()


5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5"""
#AYYIPOYINDI YEEEEEY

