#questão 01

primeiro_nome = input("Digite seu primeiro nome: ").strip()
sobrenome = input("Digite seu sobrenome: ").strip()
print(f"Bem-vinda, {primeiro_nome} {sobrenome}!")

#questão 02

frase = input("Digite a frase: ")
contador = 0
for caractere in frase:
    if caractere == " ":
        contador = contador + 1
print("Espaços em branco:", contador)

#questão 03

nome = input("Digite seu nome: ")
escada = ""
for letra in nome:
    escada = escada + letra
    print(escada)
