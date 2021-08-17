import random


for i in range(50):
	code = []

	for i in range(3):
		x = random.randint(0,9)
		if x in code:
			x = random.randint(0,9)
			if x in code:
				x = random.randint(0,9)
		code.append(x)

	# 1 numero certo e no lugar
	possiveis = [0,1,2,3,4,5,6,7,8,9]
	lista = []
	for i in range(len(possiveis)):
		if possiveis[i] not in code:
			lista.append(possiveis[i])

	index1 = random.randint(0,2)
	hint1_number = ['x','x','x']

	for i in range(3):
		if i == index1:
			hint1_number[i] = code[i]
		else:
			hint1_number[i] = lista[random.randint(0,len(lista)-1)]
	
	

	print(code,end='')
	print("Codigo")
	print(hint1_number,end='')
	print("Dica")


#
#
#
#