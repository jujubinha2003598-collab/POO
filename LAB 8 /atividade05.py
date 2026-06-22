class Onibus:
    def __init__(self, placa, nome, num_assentos):o
        self.placa = placa
        self.nome_motorista = nome
        self.assentos = [False] * num_assentos

    def __len__(self):

        return len(self.assentos)

    def __getitem__(self, indice):
        if indice < 0 or indice >= len(self.assentos):
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
        return self.assentos[indice]

    def __setitem__(self, indice, valor):
        if not isinstance(valor, bool):
            raise TypeError(f"Valor deve ser booleano (True/False)")
        

        if indice < 0 or indice >= len(self.assentos):
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
        
        self.assentos[indice] = valor

    def __str__(self):
        ocupados = self.assentos.count(True)
        livres = self.assentos.count(False)

        return (
            f"Ônibus (Placa: {self.placa}) - Motorista: {self.nome_motorista}\n"
            f"Assentos totais: {len(self.assentos)}\n"
            f"Assentos ocupados: {ocupados}\n"
            f"Assentos livres: {livres}"
        )


onibus = Onibus("ABC-1234", "João Silva", 10) 
print(len(onibus)) 
onibus[0] = True 
print(onibus) 
