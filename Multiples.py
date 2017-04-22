a,b=map(int,input().split())
c=b%a
d=a%b
if(c ==0 or d==0):
    print('Sao Multiplos')
elif(c!=0 or d!=0):
    print('Nao sao Multiplos')