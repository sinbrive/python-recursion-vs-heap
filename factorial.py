
# recursion
def factorial(n):
  if n == 1:
     return n
  elif n < 1:
     return ("??")
  else:
     return n*factorial(n-1)

# stack 
def factorial_stack(n):
  if n<1: return "??"
  stack=[1]
  i=1
  while stack:
    x0 = stack.pop()
    if i!=n:
      i+=1
      x = x0 * i
      stack=stack+[x]
    else:
      return(x)
