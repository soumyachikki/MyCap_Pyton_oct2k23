n3=int(input("Enter the value of n3:"))
n1=0
n2=1
print("Fibonacci Series:",n1,n2,end=" ")
for i in range(2,n3):
      n3=n1+n2
      n1=n2
      n2=n3
      print(n3,end=" ")
