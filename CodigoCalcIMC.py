pergunta_nome = input("Qual é o seu nome? " )
nome = ("Olá" , pergunta_nome)
peso = float(input("Qual seu peso (em KG)? "))
altura = float(input("Qual sua Altura (em CM)? "))

altura_metros = altura / 100  
imc = peso / (altura_metros ** 2)

print(pergunta_nome , (f"seu IMC é: {imc:.2f}"))

if imc < 17:
	print(" Abaixo do Peso")
elif imc < 18:
	print("Peso Ideal ")
elif imc < 25:
	print("Sobrepeso")
elif imc < 30:
	print("Obesidade Grau 1.")
elif imc < 35:
	print("Obesidade Grau 2")
elif imc < 40:
	print("Obesidade Grau 3")
