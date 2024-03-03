def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  return a / b

def main():
  print("Selecione a operação desejada:")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")

  opcao = int(input())

  a = int(input("Digite o primeiro número: "))
  b = int(input("Digite o segundo número: "))

  if opcao == 1:
    print(soma(a, b))
  elif opcao == 2:
    print(subtracao(a, b))
  elif opcao == 3:
    print(multiplicacao(a, b))
  elif opcao == 4:
    print(divisao(a, b))

if __name__ == "__main__":
  main()