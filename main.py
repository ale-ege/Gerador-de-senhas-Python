# Definição dos caracteres
numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
alfabetominusculo = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z')
alfabetomaiusculo = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z')
especial = ('*', '#', '@', '$', "%", '!', '&', 'ç', 'Ç', '?')

# Parametros
lista = numeros + alfabetominusculo + alfabetomaiusculo + especial
caracteres = 2
inicio = ""
contador = 0
print(lista)
quantidadedecaracteres = len(lista)
print(quantidadedecaracteres)

# Função geradora de senha
def gerador(digito, car, num):
    if num > car:
        print("")
    else:
        for i in lista:
            senhagerada = digito + i
            print(senhagerada)
            with open('senha.txt', 'a') as arquivo:
                arquivo.write(str(senhagerada + "\n"))
                gerador(senhagerada, car, num + 1)

# Gerar senhas
gerador(inicio, caracteres, contador)