numero = int(input("Digite um número: "))
fatorial = 1
cont = numero #aqui atribui-se o valor numero à cont para que vá apenas até
#onde for o tamanho do número
for i in range(numero - 1):
    fatorial = fatorial * cont
    print(cont, end=" * ")
    cont -= 1
print("1 = ", fatorial)
