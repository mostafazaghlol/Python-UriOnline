product1,num1,price1=map(float,input().split())
product2,num2,price2=map(float,input().split())
finalresult=(num1*price1)+(num2*price2)
print("VALOR A PAGAR: R$","{0:.2f}".format(finalresult))
