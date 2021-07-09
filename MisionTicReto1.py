n=input().split()

ganadoSin= float(n[0]) + float(n[1])*(float(n[0])/171)*1.17+float(n[2])*0.088*float(n[0])
descuento = ganadoSin-ganadoSin*0.11
print(round(ganadoSin,1),round(descuento,1))











