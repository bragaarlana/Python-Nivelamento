#Atividade 4
vetor = []
v2 = []
i=0

while True:
    print("1 - Adicionar um número ao vetor.\n2 - Remover um número do vetor.\n3 - Exibir o vetor completo.\n4 - Encontrar e exibir o maior e o menor número no vetor.\n5 - Calcular e exibir a soma de todos os números no vetor.\n6 - Sair.\n")
    op = int(input("Escolha uma opção: "))

    match op:
        case 1:
            num = int(input("Digite um número: "))
            vetor.append(num)
        case 2:
            num = int(input("Digite um número: "))
            if num not in vetor:
                print("Elemento não encontrado no vetor.")
            else:
                vetor.remove(num)
        case 3:
            print(vetor)
        case 4:
            v2 = vetor[:]
            v2.sort()
            print(f"Menor elemento: {v2[0]}\nMaior elemento: {v2[-1]}")
        case 5:
            for i in vetor:
                soma = sum(vetor)
                print(f"A soma dos elementos do vetor é: {soma}.")
        case 6:
            break
        case _:
            print("OPÇÃO INVÁLIDA")
