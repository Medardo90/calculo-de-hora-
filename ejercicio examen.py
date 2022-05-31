num = int(input("Ingrese un número: "))
while num == 1 or num < 1:
    num = int(input("Error el número debe ser mayo a 1, Ingrese un número mayor a 1: "))
if num == 2:
    print ("El 2 Es el primer número primo")
def generar_primo():
    numero = num
    yield numero
    while True:
        temp = numero + 1
        while True:
            temp += 1
            contador = 1
            contador_divisores = 0
            while contador <= temp:
                if temp % contador == 0: 
                    contador_divisores += 1
                if contador_divisores >2:
                    break
                contador += 1
            if contador_divisores ==2:
                yield temp
g = generar_primo()
primos = [next(g) for _ in range (20)]
print ("primos")            



 

  