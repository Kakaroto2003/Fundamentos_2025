a = 5

def alteraValor():
# variavel local da funcao alteraValor()
  a = 7
  print("Dentro da funcao 'a vale: ", a)
  return a

print("'a' antes da chamada da funcao: ", a)
alteraValor()
print("'a' depois da chamada da funcao", a)