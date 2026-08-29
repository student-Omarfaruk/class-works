class math:
    def __init__(self,a,b,c):
        import math
        d=(b**2)-(4*a*c)
        if (d<0):
            print("roots are imaginary")
        else:
            x1=(-b+math.sqrt(d)/(2*a))
            x2=(-b-math.sqrt(d)/(2*a))
            print(x1,x2)
            print("roots are real")
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
qrdeq=math(a,b,c)




