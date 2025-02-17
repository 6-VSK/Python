
""" 
def hello(name="Bob"):
    print(f'Hello {name}')
    
hello()
"""

"""
def f(x,y,z):
    #pass
    result = 5*x+y+z/2
    #print(result)
    return result

print(f(2,5,10))

r1 = f(2,5,10)
print(r1)
"""

"""
def y(x):
    result = 5 * x + 2
    return result

print( y(0))
print( y(1))
print( y(2))

result1 = y(1)
"""

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
        
    return result

#print( factorial(5) )



def rootFinder(a=0,b=0,c=0):
    D = b**2 - 4*a*c
    print(f'D: {D}')
    x1 = (-b - D**0.5)/(2 * a)
    x2 = (-b + D**0.5)/(2 * a)
    return x1,x2

s1,s2 = rootFinder(3,4,1)
print(s1,s2)




















