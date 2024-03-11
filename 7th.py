n=int(input("Enter number:"))

sum=0
def fact(n):
  if(n == 0 or n == 1):
    return 1
  return n*fact(n-1)

for i in range(1,n+1):
  sum+=i/fact(i)

print("sum of series:",sum)