a = 5

def alteraValor():
# dizemos para a funcao que a variavel 'a' eh global
  global a
  a = 7
  print("Dentro da funcao 'a vale: ", a)
  

print("'a' antes da chamada da funcao: ", a)
alteraValor()
print("'a' depois da chamada da funcao", a)