# recusion version
def fibonacci(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)

# stack version
def fibonacci_stack(n):
  stack=[(0,1)]
  i=1
  while stack:
    (x0, x1)= stack.pop()
    if i!=n:
      x = x0 + x1
      stack=stack+[(x1,x)]
      i+=1
    else:
      return(x)

def fib_iter(n):
    f=[0,1]
    if n==0:
      return 0
    elif n==1:
      return 1
    else:
      for i in range(1, n):
        temp=f[0]
        f[0]= f[1]
        f[1] = f[1]+temp
      return f[1]
      
      

