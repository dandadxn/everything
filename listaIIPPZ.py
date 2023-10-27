#a = int(input("insira 3 lados de um triangulo:\n"))
#b = int(input())
#c = int(input())
#if a + b <= c or b + c <= a or a + c <= b:
#	print("valores não formam um triangulo")
#elif a == b == c:
#	print("valores formam um triangulo equilatero")
#elif a != b != c:
#	print("valores formam um triangulo escaleno")
#else:
#	print("valores formam um triangulo isoceles")

#####################

#a = int(input("insira um ano:\n"))
#if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
#	print(f"{a} é um ano bissexto")
#else:
#	print(f"{a} não é um ano bissexto")

#####################

#peso = float(input("insira o peso da pesca:\n"))
#if peso > 50:
#	excesso = peso - 50
#	multa = excesso * 4.00
#	print(f"excesso: {excesso:.1f}kg\nmulta: R${multa:.2f}")
#else:
#	print(f"excesso: 0kg\nmulta: R$0")

############################

#a = int(input("insira 3 números:\n"))
#b = int(input())
#c = int(input())
#if a >= b and a >= c:
#	print(f"{a} é o maior número")
#elif b >= c:
#	print(f"{b} é o maior número")
#else:
#	print(f"{c} é o maior número")

#if a <= b and a <= c:
#	print(f"{a} é o menor número")
#elif b <= c:
#	print(f"{b} é o menor número")
#else:
#	print(f"{c} é o menor número")

###############################

#salario = float(input("quanto você ganha por hora?\n"))
#horas = int(input("por quantas horas trabalhou nesse mês?\n"))

#a = salario * horas
#b = a * 11 / 100 
#c = a * 8 / 100
#d = a * 5 / 100
#e = a - b - c - d

#print(f"+Salario bruto: R${a:.2f}\n-IR(11%): R$:{b}\n-INSS(8%): R${c}\n-Sindicato(5%): R${d}\n=Salario liquido: R${e}")

###############################

#m2 = int(input("insira quantos m² serão pintados:\n"))
#if m2 % 54 != 0:
#	latas = int(m2 / 54) + 1
#	valor = latas * 80
#	print(f"voce vai precisar de {latas} latas de tinta, custando no total:\nR${valor:.2f}")
#else:
#	latas = m2 / 54
#	valor = latas * 80
#	print(f"voce vai precisar de {latas:.0f} latas de tinta, custando no total:\nR${valor:.2f}")

##################################

#m2 = int(input("metros:\n"))
#if m % 54 == 0:
#	latas = m2 / 54
#else:
#	latas = int(m2 / 54) + 1

#valor = latas * 80
#print(f"com um tamanho de {m}, será necessário {latas} latas, custando no total:\nR${valor:.2f}")
