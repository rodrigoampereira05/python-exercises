carro = {
    "marca": "Seat",
    "modelo": "Ibiza",
    "ano": "2005",
    "cor": "preto"
}


print(carro)
print(carro["marca"])
carro["cor"] = "azul"
print(carro["cor"])

carro.pop("ano")
print(carro)

print(carro.keys())
print(carro.values())

carro["owner"] = "Rodrigo"
print(carro["owner"])
