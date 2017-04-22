A,B,C=map(float,input().split())
spam=[A,B,C]
spam.sort()
A=spam[2]
B=spam[1]
C=spam[0]
print(spam)
print(A)
print(B)
print(C)
if(A>= (B+C)):
    print('NAO FORMA TRIANGULO')
elif((A**2)==((B**2)+(C**2))):
    print('TRIANGULO RETANGULO')
elif((A**2)>((B**2)+(C**2))):
    print('TRIANGULO OBTUSANGULO')
elif((A**2)<((B**2)+(C**2))):
    print('TRIANGULO ACUTANGULO')
if(A==C and C==B and A==B):
    print('TRIANGULO EQUILATERO')
if((A==C and C!=B) or (A==B and C!=B) or (B==C and A!=B)):
    print('TRIANGULO ISOSCELES')
