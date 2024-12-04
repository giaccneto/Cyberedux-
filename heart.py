'''

size = 15

for a in range(int(size / 2), size + 1, 2): 

    for b in range(1, size - a, 2):
        print(" ", end = "")

    for b in range (1, a + 1):
        print("A", end="")
    for b in range(1, (size - a) + 1):
        print(" ", end = "")
    for b in range(1, a):
        print("A", end = "")
    print("")

for a in range(size,-1, -1):
    for b in range(a, size):
        print(" ", end = "")
    for b in range(1, (a * 2)):
        print("B", end = "")
    print("")
   
def somar_numeros_pares():
    try:
        entrada = input("Digite uma lista de números separados por espaço: ")
        
        numeros = [int(num) for num in entrada.split()]
        
        soma_pares = sum(num for num in numeros if num % 2 == 0)
        
        print(f"A soma dos números pares é: {soma_pares}")
    except ValueError:
        print("Erro: Por favor, insira apenas números separados por espaço.")
        somar_numeros_pares()  

somar_numeros_pares()

for i in range(5):
    if i == 3:
        break
    print(i)
     '''


# 1

amigos = ["Ana", "Carlos", "Beatriz", "João", "Mariana"]

print("Meus amigos são:", amigos)

amigos.append("Lucas")
print("Minha lista de amigos atualizada:", amigos)

amigos.sort()
print("Minha lista de amigos em ordem alfabética:", amigos)

# 2 

cores_arco_iris = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta")
print("As cores do arco-íris são:", cores_arco_iris)

quantidade_azul = cores_arco_iris.count("azul")
print(f"A cor 'azul' aparece {quantidade_azul} vez(es) na tupla.")


#3

numeros = list(range(1, 11))

numeros_multiplicados = [numero * 2 for numero in numeros]

print("Lista original:", numeros)
print("Lista com números multiplicados por 2:", numeros_multiplicados)

#4 

vogais = ("a", "e", "i", "o", "u", "a", "e", "i",  "u")

quantidade_a = vogais.count("a")


print(f"A vogal 'a' aparece {quantidade_a} vez(es) na tupla.")

# 5
frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

frutas.pop()

frutas.insert(0, "morango")

print("Lista de frutas atualizada:", frutas)
