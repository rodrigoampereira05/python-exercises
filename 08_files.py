with open("notes.txt", "w") as file:
    file.write("Medio\n")
    file.write("Vitor Ferreira\n")
    file.write("Psg\n")

#Append (adicionar sem apagar o que já existe):
with open("notes.txt", "a") as file:
    file.write("Melhor do Mundo\n")

with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines[1])

with open("notes.txt", "r") as file:   
    content = file.read()
    print(content)


#(o "a" é de append, o "w" apagava tudo e escrevia de novo)

#Substituir uma linha específica:

with open("notes.txt", "r") as file:
    lines = file.readlines()

lines[1] = "Vitinha Ferreira\n" #Muda a segunda linha

with open("notes.txt", "w") as file:
    file.writelines(lines)

with open("notes.txt", "r") as file:
    print(file.read())


#Apagar Linha

with open("notes.txt", "r") as file:
    lines = file.readlines()

del lines[0]  # apaga a primeira linha

with open("notes.txt", "w") as file:
    file.writelines(lines)

with open("notes.txt", "r") as file:
    print(file.read())