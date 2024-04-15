pergunta_nome = input("Qual é o seu nome? " )
nome = ("Olá" , pergunta_nome)
peso = float(input("Qual seu peso (em KG)? "))
altura = float(input("Qual sua Altura (em CM)? "))

altura_cm = altura / 100  
imc = peso / (altura_cm ** 2)

print(pergunta_nome , (f"seu IMC é: {imc:.2f}"))

if imc < 18:
	print(" Abaixo do Peso")
elif imc < 24:
	print("Peso Ideal ")
elif imc < 29:
	print("Sobrepeso")
elif imc < 34:
	print("Obesidade Grau 1.")
elif imc < 39:
	print("Obesidade Grau 2")
elif imc < 45:
	print("Obesidade Grau 3")
