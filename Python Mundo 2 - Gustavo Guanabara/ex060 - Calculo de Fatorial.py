#from math import factorial
#n = int(input("Digite um numero: "))
#f = factorial(n)
#print("O fatorial de {} é {}".format(n, f))

num = int(input("Digite um número para calcular seu fatorial: "))

print("Calculando {}! = ".format(num), end='')
count = num
produto = 1
while count > 0:
    print("{}".format(count), end='')
    print(" x " if count > 1 else " = ", end='')
    produto *= count
    count -= 1
print("{}".format(produto))



