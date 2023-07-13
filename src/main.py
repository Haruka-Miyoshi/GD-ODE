# %%
import numpy as np
import matplotlib.pyplot as plt

"""常微分方程式"""
class ODE(object):
    def __init__(self):
        self.__n=None
        self.__x=None
        # 微分した結果
        self.__yn=[]
        
    def x(self, t, a0=0.4, a1=-1.0, b=10):
        return a0*t**2 + a1*t + b
    
    def diff(self, t, n, dt=0.01):
        dy=0.0
        for _ in range(n):
            dy+=self.x(t) + self.x(dt)
            self.__yn.append(dy)
        return self.__yn

t=np.linspace(0,10,1)
ode=ODE()
y=ode.diff(t, n=10)

for yn in y:
    plt.scatter(t, yn)
plt.show()
# %%
import numpy as np

def f(x):
    return x**2

"""差分方程式"""
class Difference(object):
    def __init__(self):
        self.__diff=None

    # 前進差分
    def forward(self, func, x0, x1):
        h=x1-x0
        df=func(x0)-func(x1)
        df/=h
        return df
    
    # 後退差分
    #def backward(f,)

x1=0
x2=1
selfDifference=Difference()
df=selfDifference.forward(f, x1, x2)
print(df)

"""
# 後退差分
x1=-1
x2=0
h=x1-x2
df=f(x1)-f(x2)
df/=h
print(df)
"""
# %%
from functools import partial

def func1(a, b):
    print(a, b)

def func2(f):
    f()

func2(partial(func1, 10)) # 10 None

# %%
def greet(name):
    print(f"Hello, {name}!")

def call_function(func, name):
    func(name)

# greet関数を引数として渡し、引数nameに値を指定する
call_function(greet, "Alice")

# %%
