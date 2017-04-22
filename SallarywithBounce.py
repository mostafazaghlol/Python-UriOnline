name=input()
fixedsallary=float(input())
sold=float(input())
bounce=(sold*15)/100
finalsallary=fixedsallary+bounce
print("TOTAL = R$","{0:.2f}".format(finalsallary))
