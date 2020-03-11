import sys
sys.setrecursionlimit(10**6) 

def f(x):
    return x**2


def derivada(x):
    h=0.000000000001
    return (f(x+h)-f(x))/h


def minimo(xvieja): 
    xr=derivada(xvieja)
    a1=xvieja + 0.5
    a2=xvieja - 0.5
    x1=derivada(xvieja + 0.5)
    x2=derivada(xvieja - 0.5)
    if((xr>-0.1 and xr<0.1) and f(xvieja)< 0.01):
        return xvieja
            
    else:
        if(xr>0):
            if(x1<xr):
                return minimo(a1)
            elif(x2<xr):
                return minimo(a2)
        if(xr<0):
            if(x1>xr):
                return minimo(a1)              
                
            elif(x2>xr):
                return minimo(a2)


   

        

    

