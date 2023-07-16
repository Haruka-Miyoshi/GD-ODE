"""差分方程式"""
class Difference(object):
    def __init__(self):
        pass

    # 前進差分
    def forward(self, func, x0, x1):
        h=x1-x0
        df=func(x1)-func(x0)
        df/=h
        return df
    
    # 後退差分
    def backward(self, func, x0, x1):
        h=x0-x1
        df=func(x0)-func(x1)
        df/=h
        return df