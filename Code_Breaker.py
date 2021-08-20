import random
import os


hint_numbers = []

def one_right_IN_place(code):
		possiveis = [0,1,2,3,4,5,6,7,8,9]
		lista = []
		for i in range(len(possiveis)):
			if possiveis[i] not in code:
				lista.append(possiveis[i])

		index1 = random.randint(0,2)
		hint_number = ['x','x','x']

		for i in range(3):
			if i == index1:
				hint_number[i] = code[i]
			else:
				hint_number[i] = lista[random.randint(0,len(lista)-1)]

		
		global hint_numbers
		for i in range(3):
			hint_numbers.append(hint_number[i])

		return hint_number


def one_right_OUT_place(code):
		possiveis = [0,1,2,3,4,5,6,7,8,9]
		hint_number = []
		code_index = random.randint(0,2)
		code_number = code[code_index]

		count = 0
		removidos = 0
		while True:
			if possiveis[count] in code:
				possiveis.remove(possiveis[count])
				removidos += 1
				count -= 1
			count += 1
			if removidos == 3:
				break



		for i in range(3):
			if i == code_index:
				x = code_number
			else:
				x = possiveis[random.randint(0,len(possiveis)-1)]
			hint_number.append(x)

		while hint_number[code_index] == code_number:
			random.shuffle(hint_number)

		global hint_numbers
		for i in range(3):
			hint_numbers.append(hint_number[i])
		return hint_number


def all_wrong(code):
		possiveis = [0,1,2,3,4,5,6,7,8,9]
		hint_number = []
		for i in range(3):
			possiveis.remove(code[i])

		for i in range(3):
			x = possiveis[random.randint(0,len(possiveis)-3)]
			hint_number.append(x)
			possiveis.remove(x)

		global hint_numbers
		for i in range(3):
			hint_numbers.append(hint_number[i])

		return hint_number



def two_right_OUT_place(code):
	possiveis = [0,1,2,3,4,5,6,7,8,9]
	for i in range(3):
		if possiveis[i] in code:
			possiveis.remove(possiveis[i])

	code_index_1 = random.randint(0,2)
	hint_number_1 = code[code_index_1]

	code_index_2 = random.randint(0,2)
	while code_index_2 == code_index_1:
		code_index_2 = random.randint(0,2)
	hint_number_2 = code[code_index_2]

	hint_extra = possiveis[random.randint(0,len(possiveis)-1)]

	hint_number = [hint_number_1,hint_number_2,hint_extra]
	while (hint_number[code_index_1] == code[code_index_1] or hint_number[code_index_2] == code[code_index_2]):
		random.shuffle(hint_number)
	
	global hint_numbers
	for i in range(3):
		hint_numbers.append(hint_number[i])

	return hint_number
	

def create_code():
	code = []
	possiveis = [0,1,2,3,4,5,6,7,8,9]
	leng = len(possiveis)

	for i in range(3):
		
		x = possiveis[random.randint(0,len(possiveis)-1)]
		possiveis.remove(x)
		code.append(x)

	return code

def create_game():
		global code
		code = create_code()
		hint1 = one_right_IN_place(code)
		hint2 = all_wrong(code)
		hint3 = one_right_OUT_place(code)
		hint4 = two_right_OUT_place(code)
		hint5 = one_right_OUT_place(code)

		remake = False
		for i in range(3):
			if code[i] not in hint_numbers:
				remake = True
		if remake:
			create_game

		print(hint2,end=' ')
		print("Tudo errado")
		print(hint1,end=' ')
		print("Um certo no lugar")
		print(hint3,end=' ')
		print("Um certo e fora do lugar")
		print(hint4,end=' ')
		print("Dois certos e fora do lugar")
		print(hint5,end=' ')
		print("Um certo e fora do lugar")

		


while True:
	
	create_game()

		


	cont = input("Digite ENTER para ver o codigo\n")
	print(f'O código é {code}')


	cont = input("Deseja jogar novamente?(S/N)\n")
	if cont == "n":
		break
	else:
		print("\n" * 30)
		