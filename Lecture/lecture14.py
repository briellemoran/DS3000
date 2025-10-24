import autograd.numpy as np
from autograd import grad
from autograd.numpy import exp, log2, log

# Problem 1
def f1(x):
    return 1.0*x + 2.0*x + 3.0*x

df1 = grad(f1)
print("Problem 1 manual derivative:", 6)
print("Problem 1 autograd derivative at x=2:", df1(1.0))

# Problem 2
def f2(x):
    return (2.0*x + 1.0)**2.0 + 3.0*x - 2.0

df2 = grad(f2)
print("Problem 2 manual derivative:", 8*1 + 7)
print("Problem 2 autograd derivative at x=2:", df2(1.0))


# Problem 3
def f3(x): 
    return (2.0*x + 1.0) * exp(-2.0*x) - log2(x**2.0)

def manual3(x):
	return 2*exp(-2*x) - 2 * (2*x + 1)*exp(-2*x) - 2/(x * log(2))

df3 = grad(f3)
print("\nProblem 3 manual derivative at x=1:", manual3(1.0))
print("Problem 3 autograd derivative at x=1.0:", df3(1.0))

# Problem 4
def f4(x):
    return (exp(2.0 * x) + 1.0)**3 + log(x**2)

def manual4(x):
	return 6*exp(2*x)*(exp(2*x) + 1)**2 + 2/x

df4 = grad(f4)
print("\nProblem 4 manual derivative at x=1:", manual4(1.0))
print("Problem 4 autograd derivative at x=1.0:", df4(1.0))

