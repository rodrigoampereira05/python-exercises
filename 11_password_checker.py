import string

password = input("Password:  ")
print("\n")

pass_check = []
resultado = 0

def password_caracteres(password):
    
    tamanho_password = len(password)

    if tamanho_password >= 8:
        pass_check.append("[✓] Pelo menos 8 caracteres.")
        return  True

    else:
        pass_check.append("[X] Pelo menos 8 caracteres.")
        return False

def letra_maiuscula(password):

    for i in password:
        if i.isupper():
            pass_check.append("[✓] Letra maiúscula.")
            return True
        
    pass_check.append("[X] Letra maiúscula.")
    return False

def letra_minuscula(password):
    for i in password:
        if i.islower():
            pass_check.append("[✓] Letra minúscula.")
            return True
        
    pass_check.append("[X] Letra minúscula.")
    return False

def numero(password):
    for i in password:
        if i.isnumeric():
            pass_check.append("[✓] Número.")
            return True
    
    pass_check.append("[X] Número.")
    return False

def caracters_diferentes(password):
    caracteres_especiais = string.punctuation
    for char in password:
        if char in caracteres_especiais:
            pass_check.append("[✓] Caractere especial.")
            return True
        
    pass_check.append("[X] Caractere especial.")
    return False

def classificacao(resultado):
    if 0 <= resultado <= 2:
        print("Classificaçáo: Fraca")
    if 2 < resultado <= 4:
        print("Classificação: Média")
    if resultado >= 5:
        print("Classificação: Forte")

        

if password_caracteres(password):
    resultado += 1

if letra_maiuscula(password):
    resultado += 1

if letra_minuscula(password):
    resultado += 1

if numero(password):
    resultado += 1

if caracters_diferentes(password):
    resultado += 1


for x in pass_check:
    print(x)

print(f"\nPontuação: {resultado}/5")
(classificacao(resultado))