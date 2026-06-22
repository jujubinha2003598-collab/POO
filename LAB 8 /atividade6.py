class Personagem:
  def __init__ (self, nome:str, vida:int):
    self.nome = nome
    self.vida = vida
  def Tomar_dano(self, valor:int):
    self.vida -= valor 
class Mago(Personagem):
    def __init__(self, nome: str, vida: int, mana: float):
        super().__init__(nome, vida)
        self.mana = float(mana)
    def __str__(self):
      return f"Mago: {self.nome} | Vida: {self.vida} | Mana: {self.mana}"
    def __add__(self, valor: float): 
      self.mana += valor
      return self.mana
    def __sub__(self, valor: float): 
      self.mana -= valor
      if self.mana < 0:
        self.mana = 0.0
      return self.mana 
    def __mul__(self, fator:float): 
      self.mana *= fator
      return self.mana
      
    def __truediv__(self, valor:float): 
      if valor == 0:
        print("Erro: Não é possível dividir a mana por zero!")
        return self.mana 
      else:
        self.mana = self.mana / valor
        return self.mana
class Barbaro(Personagem):
  def __init__(self, nome: str, vida: int,  stamina: float, furia: bool):
    super().__init__(nome, vida)
    self.stamina = stamina
    self.furia = furia
  def __str__(self):
    return f"Bárbaro: {self.nome} | {self.vida} | stamina: {self.stamina} | furia: {self.furia}"
  def __add__(self, valor):
      self.furia = self.furia + valor
      return self.furia
  def __sub__(self, valor: float): 
    self.stamina = self.stamina - valor 
    if self.stamina == 0 and self.furia == false:
      self.furia == true 
      self.stamina = 5 
      print("🔥 O guerreiro entrou em FÚRIA! Stamina subiu para 5.")
    return self.stamina
  def __mul__(self, fator: float):
    self.furia = self.furia * fator
    return self.furia
  def __truediv__(self, valor: float):  

    
  






print("=== CRIAR PERSONAGEM ===")
nome_usuario = input("Qual o nome do personagem? ")
vida_usuario = int(input("Quanta vida ele vai ter? "))
tipo_classe = input("Escolha a classe (Mago ou Barbaro): ")
if tipo_classe == "mago" or tipo_classe == "Mago":
  mana_usuario = float(input("Quanta mana inicial? "))
    jogador = Mago(nome_usuario, vida_usuario, mana_usuario)
else:
    furia_usuario = float(input("Quanta fúria inicial? "))
    jogador = Barbaro(nome_usuario, vida_usuario, furia_usuario)

print("Personagem criado!")








#gandalf = Mago("Gandalf", 100, 50.0)
#print(gandalf)  
#gandalf.tomar_dano(20)
#gandalf + 25.0   
#print(gandalf)  
#gandalf - 80.0  
#print(gandalf)  
#gandalf + 10.0
#gandalf * 3.0   
#gandalf / 2.0   
#print(gandalf)

    
