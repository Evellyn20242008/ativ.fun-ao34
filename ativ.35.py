#Ler uma lista de 10 números reais e mostre-os na ordem inversa.
numeros = [] 
for i  in range (10):
    numero = float(input(f"digite o numero { i + 1}"))
    numeros.append(numero)
    numeros.reverse()
    
print("Números na ordem inversa:")
for numero in numeros:
    print(numero)
