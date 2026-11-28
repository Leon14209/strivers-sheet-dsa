
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
k=pattern1(5)                

