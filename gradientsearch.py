import sympy as sym
t=sym.symbols('t')

def dertoX(f,g):    #input values
    x , y = sym.symbols('x y')      # defining function variables for sym
    func=(3*x**2)+(3*x*y)+(y**2)+3*x
    partderx = sym.diff(func,x)       # partial derivative according to x
    partderivx = partderx.subs([(x, f), (y, g)])    # calculating result with input values (f,y)
    return partderivx

def dertoY(h,j):    #input values
    x , y = sym.symbols('x y') #defining function variables for sym
    func=(3*x**2)+(3*x*y)+(y**2)+3*x
    pardery = sym.diff(func,y)      # partial derivative according to y
    partderivy = pardery.subs([(x, h), (y, j)])     # calculating result with input values (f,y)
    return partderivy

def tvalue(o,u):    #input values
    x , y = sym.symbols('x y')
    funct=((3*x**2)+(3*x*y)+(y**2)+3*x)
    fsol=funct.subs([(x, o), (y, u)])       # calculating result with input values (f,y)
    fder=sym.diff(fsol,t)       ## partial derivative according to y
    eq1=sym.Eq(fder)
    sol=sym.solve(eq1)
    return sol[0]

#initialization
e=10**-5 
n,m=0,0
n2,m2=0,0

while abs(dertoX(n2,m2))>e or abs(dertoY(n2,m2))>e:
    
    n=n2-(t*dertoX(n2,m2)) #first step for x
    m=m2-(t*dertoY(n2,m2)) #first step for y
    crp=tvalue(n,m)
    
    n=n.subs(t,crp)
    m=m.subs(t,crp)
    
    n2=n.subs(t,crp) #answer part x
    m2=m.subs(t,crp) #answer part y

print('X value:' ,round(n2,7), '\n', 'Y value:' ,round(m2,7))



