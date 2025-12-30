with open("access.log", "w") as file:
    file.write("192.168.1.1 - GET /index.html\n")
    file.write("192.168.1.2 - GET /about.html\n")
    file.write("192.168.1.1 - POST /login\n")
    file.write("10.0.0.5 - GET /index.html\n")
    file.write("192.168.1.1 - GET /dashboard\n")
    file.write("192.168.1.2 - GET /contact.html\n")
    file.write("10.0.0.5 - POST /submit\n")
    file.write("192.168.1.1 - GET /logoutn")

print("\n")
print("\n")
print("\n")

with open("access.log", "r") as file:
    content = file.read()
    print(content)

contagem = {}

def read_ips():
    with open("access.log", "r") as file:
        lines = file.readlines()

#vai separar a linha em por espaços
    for line in lines:
        parts = line.split(" ")
        ip = parts[0]
        print(ip)
        if ip in contagem:
            contagem[ip] = contagem[ip] +1
        else:
            contagem[ip] = 1
read_ips()

print(contagem)
