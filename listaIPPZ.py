#n1 = int(input("insira um número inteiro:\n"))
#n2 = int(input("Agora insira outro número inteiro:\n"))
#print(f"A soma dos dois números que você escolheu é:\n{n1 + n2}")

#########

#metros = int(input("insira o valor que deseja ser convertido:\n"))
## vc = metros * 1000
#print(f"O valor inserido convertido para milimetros é igual a:\n{metros * 1000}") 

#########

#d = int(input("insira o numero de dias:\n"))
#h = int(input("agora insira o numero de horas:\n")) 
#m = int(input("agora insira o numero de minutos:\n"))
#s = int(input("agora insira o numero de segundos:\n"))

#total = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s * 60 

#print (f"O total em segundos de tudo isso equivale a:\n{total}")

##########

#sali = float(input("salario atual:\n"))
#desejo = float(input("% de aumento desejado:\n"))

#aumento = sali * desejo / 100
#salf = sali + aumento
#print(f"aumento de:R${aumento:.2f}\nSalario final ficando em:R${salf:.2f}")

##########

#prei = float(input("valor mercadoria:\n"))
#desconto = float(input("% de desconto dessa mercadoria:\n"))

#valordes = desconto / 100 * prei 
#pref = prei - valordes
#print(f"com um desconto de R${valordes:.2f}, o preço final do produto é:\nR${pref:.2f}")

##########

#s = float(input("qual será a distancia da viagem?\n"))
#vm = float(input("qual a velocidade media prevista durante a viagem?\n"))

#d = s / vm 

#print(f"a duração da viagem será de {d}h prevista")

##########

## F = 9 * c / 5 + 32

#cel = float(input("qual a temperatura em celsius hoje?\n"))
#far = cel * 9 / 5 + 32
#print (f"a temperatura hoje em fahrenheit é de {far:.1f}")

########### 

## C = (F - 32) * 5 / 9 

#far = float(input("qual a temperatura em fahrenheit hoje?\n"))
#cel = (far - 32) * 5 / 9 
#print (f"a temperatura em celsius hoje é de {cel:.0f}")
 
##########

#km = int(input("insira quilomretros rodados:\n"))
#d = float(input("agora insira por quantos dias foi utilizado:\n"))

#total = d * 60.00 + km * 0.15

#print (f"o total a se pagar pelo carro alugado é de: R${total:.2f}")

###########

#cd = int(input("quantos cigarros você fuma por dia?\n"))
#af = int(input("por quantos anos você já fumou?\n"))

## 1 ano = 365 dias, 1 dia = 24h, 1h = 60min, 1 min = 60s #
## 1 dia = 60 * 24 = 1440min                              #		
## perde 10 min de vida por cigarro
#a = cd * 365
#b = a * af
#c = (b * 10) / 1440

#print (f"perdeu {c:.0f} dias por causa do cigarro")

###########

#print (len(str(2**1000000)))



