try:
    numero = float(input("Numero: "))
    valor = 100 / numero
    print(valor)
    
except ZeroDivisionError:
    print("Nao se pode dividir 100 por 0")
except ValueError:
    print("Insira um valor valido")