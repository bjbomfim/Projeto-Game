from models.calcular import Calcular

def main() -> None:
	pontos = 0
	jogar(pontos)

def jogar(pontos: int) -> None:
	dificuldade = int(input('Informe a dificuldade [1, 2, 3 e 4]: '))
	calc = Calcular(dificuldade)

	print('Informe o resultado para a seguinte operação: ')
	calc. mostrar_operacao()
	resultado = int(input())

	if calc.checar_resultado(resultado):
		pontos += 1
		print(f"Voce tem {pontos}")

	continuar = int(input('Deseja continuar no jogo? '))
	if continuar:
		jogar(pontos)
	else:
		print(f'Voce finalizou com {pontos} pontos')

if __name__ == '__main__':
	main()