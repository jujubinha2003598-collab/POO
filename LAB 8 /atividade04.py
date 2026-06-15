class Pessoa:
  def __init__ (self, nome: str, altura: float):
    self.nome = nome
    self.altura = float(altura)
  def __str__(self):
    return f"Nome : {self.nome} | Altura : {self.altura}"
  def __gt__(self, other): 
    return self.altura > other.altura
  def __lt__(self, other):
    return self.altura < other.altura
    
lst = []
D = int(input("Quantas pessoas serão cadastradas?"))
for i in range(D):
  name = input("Qual o nome da pessoa?")
  h = float("Qual a altura da pessoa?")
  p = Pessoa(name, h)
  lst.append(p)
print('MAIOR:', max(lst))
print('MENOR:', min(lst))
for pessoa in sorted(lst):
  print(pessoa)


