#list comprehension
if __name__ == '__main__':
    x = int(input())#1
    y = int(input())#1
    z = int(input())#1
    n = int(input())#2
    #for i in range(0,x+1):
     #   for j in range(0,y+1):
      #      for k in range(0,z+1):#000 001 010 100 101 110 
       #         if i+j+k!=n:
        #            print([i,j,k],end='')
    print ([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i + j + k != n ])
