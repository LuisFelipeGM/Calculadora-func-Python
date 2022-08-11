#Calculadora Simples
#Operações: adição, subtração, multiplicação e divisão

# menu()
# entrada_de_dados()
# adicao()
# subtracao()
# multiplicacao()
# divisao()
# imprimir()
# controlador()
# Funcao Menu()
def menu():
    print("*- Menu -*")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    op = int (input("Operarção: "))
    return op

# -----------------------------------------------------------------------------------------------------------------------
# Funcao entrada_de_dados()
def entrada_de_dados():
    num = int(input("Número: "))
    return num

# -----------------------------------------------------------------------------------------------------------------------
# Funcao adição()
def adicao(num1, num2):
    print("*- Adição -*")
    soma = num1 + num2
    return soma

# -----------------------------------------------------------------------------------------------------------------------
# Funcao subtração()
def subtracao(num1, num2):
    print("*- Subtração -*")
    sub = num1 - num2
    return sub

# -----------------------------------------------------------------------------------------------------------------------
# Funcao multiplicação()
def multiplicacao(num1, num2):
    print("*- Multiplicação -*")
    mult = num1 * num2
    return mult

# -----------------------------------------------------------------------------------------------------------------------
# Funcao divisão()
def divisao(num1, num2):
    print("*- Divisão -*")
    div = num1 / num2
    return div

# -----------------------------------------------------------------------------------------------------------------------
# Funcao imprimir()
def imprimir(res):
    print(f"\n*- Resultado -*")
    print(f"Resultado: {res}\n")
    

# -----------------------------------------------------------------------------------------------------------------------
# Funcao controlador()
def controlador(op, num1, num2):
    if op == 1:
        result = adicao(num1, num2)
    elif op == 2:
        result = subtracao(num1, num2)
    elif op == 3:
        result = multiplicacao(num1, num2)
    elif op == 4:
        result = divisao(num1, num2)
    else:
        result = "Operação inválida"
    return result

# -----------------------------------------------------------------------------------------------------------------------
# Programa principal
print("*- Calculadora simples -*")
op = menu()
num1 = entrada_de_dados()
num2 = entrada_de_dados()
res = controlador(op, num1, num2)
imprimir(res)