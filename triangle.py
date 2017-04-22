A,B,C=map(float,input().split())

if(((A+B)>C ) and ((B+C)>A) and ((C+A)>B)):
    Perimetro = A + B + C
    print("Perimetro =",Perimetro)
else:
    Area = ((A + B) / 2) * C
    print("Area =",Area)

