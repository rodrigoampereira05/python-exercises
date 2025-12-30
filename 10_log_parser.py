"""with open("access.log", "w") as file:
    file.write("192.168.1.1 - GET /index.html\n")
    file.write("192.168.1.2 - GET /about.html\n")
    file.write("192.168.1.1 - POST /login\n")
    file.write("10.0.0.5 - GET /index.html\n")
    file.write("192.168.1.1 - GET /dashboard\n")
    file.write("192.168.1.2 - GET /contact.html\n")
    file.write("10.0.0.5 - POST /submit\n")
    file.write("192.168.1.1 - GET /logoutn")"""


"""with open("access.log", "r") as file:
    content = file.read()
    print(content)
"""
contagem = {}

def read_ips():
    try:
        with open("access.log", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Ficheiro nao encontrado")
        return False

#vai separar a linha em por espaços
    for line in lines:
        parts = line.split(" ")
        ip = parts[0]
        if ip in contagem:
            contagem[ip] = contagem[ip] +1
        else:
            contagem[ip] = 1
    return True

def ip_mais_usado():
    maior_numero = 0
    ip_maior = ""
    
    for chave, valor in contagem.items():
        if valor > maior_numero:
            maior_numero = valor
            ip_maior = chave
    
    return ip_maior, maior_numero

if read_ips():  
    print(f"Os ips usados sao: {contagem}")


    ip, numero = ip_mais_usado()
    print(f"O ip mais usado foi: {ip} com {numero} acessos ")

