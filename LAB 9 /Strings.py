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


#dicionario
#questao 1
def contagem_caracteres(texto):
    frequencia = {}
    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1
    return frequencia

texto_exemplo = "python programming"
resultado_final = contagem_caracteres(texto_exemplo)
print(resultado_final)

#questao 3
def mesclar_dict(dicio_a: dict, dicio_b: dict):
    dicio_mesclado = dicio_a
    for chave in dicio_b:
        if chave in dicio_mesclado:
            if dicio_b[chave] > dicio_mesclado[chave]:
                dicio_mesclado[chave] = dicio_b[chave]
        else:
            dicio_mesclado[chave] = dicio_b[chave]
    return dicio_mesclado
dados_1 = {'a': 1, 'b': 2, 'c': 3}
dados_2 = {'b': 4, 'd': 5}
resultado_mesclado = mesclar_dict(dados_1, dados_2)
print(resultado_mesclado)

#questao 4
def filtrar_dict(mapa_dados: dict, chaves_alvo: list):
    resultado_filtro = {}
    for chave in chaves_alvo:
        resultado_filtro[chave] = mapa_dados[chave]
    return resultado_filtro

valores_originais = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
lista_selecao = ['a', 'c', 'e']
resultado_filtrado = filtrar_dict(valores_originais, lista_selecao)
print(resultado_filtrado)

#questao 5 
def result_vota(dados_votacao: list):
    apuracao = {}
    soma_total = 0
    for lote_votos in dados_votacao:
        for politico in lote_votos:
            if politico in apuracao:
                apuracao[politico] += lote_votos[politico]
                soma_total += lote_votos[politico]
            else:
                apuracao[politico] = lote_votos[politico]
                soma_total += lote_votos[politico]

    for politico in apuracao:
        apuracao[politico] = (politico, apuracao[politico] / soma_total * 100)

    return apuracao

urnas_apuradas = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
placar_final = result_vota(urnas_apuradas)
print(placar_final)




