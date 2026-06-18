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
  






print("=== CRIAR PERSONAGEM ===")
nome_usuario = input("Qual o nome do personagem? ")
vida_usuario = int(input("Quanta vida ele vai ter? "))
tipo_classe = input("Escolha a classe (Mago ou Barbaro): ")








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

    
