class Carteira:
    def __init__ ( self, moeda:str, saldo:float):
        self.moeda = moeda.upper()
        self.saldo = float(saldo)
    def __add__(self, valor_yuan):
        if self.moeda == "USD":
            Valor_Convertido = valor_yuan * 0.14
        elif self.moeda == "BRL":
            Valor_Convertido = valor_yuan * 0.85
        else:
            Valor_Convertido = valor_yuan
        return self.saldo + Valor_Convertido
    def __sub__(self, valor_yuan):
        if self.moeda == "USD":
            Valor_Convertido = valor_yuan * 0.14
        elif self.moeda == "BRL":
            Valor_Convertido = valor_yuan * 0.85
        else:
            Valor_Convertido = valor_yuan
        return self.saldo - Valor_Convertido


