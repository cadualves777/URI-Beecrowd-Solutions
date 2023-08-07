def main():
    numeros_pares = []
    numeros_impares = []
    count_pares = 0
    count_impares = 0

    for _ in range(15):
        numero = int(input())
        if numero % 2 == 0:
            if count_pares < 5:
                numeros_pares.append(numero)
                count_pares += 1
            else:
                imprimir_vetor("par", numeros_pares)
                numeros_pares = [numero]
                count_pares = 1
        else:
            if count_impares < 5:
                numeros_impares.append(numero)
                count_impares += 1
            else:
                imprimir_vetor("impar", numeros_impares)
                numeros_impares = [numero]
                count_impares = 1

    imprimir_vetor("impar", numeros_impares)
    imprimir_vetor("par", numeros_pares)


def imprimir_vetor(tipo, vetor):
    for i in range(len(vetor)):
        print(f"{tipo}[{i}] = {vetor[i]}")


if __name__ == "__main__":
    main()
