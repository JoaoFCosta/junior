# A função soma() recebe dois números como parâmetros e retorna a soma deles
def soma(a, b):
  return a + b
# A função subtracao() recebe dois números como parâmetros e retorna a subtração deles
def subtracao(a, b):
  return a - b
# A função multiplicacao() recebe dois números como parâmetros e retorna a multiplicação deles
def multiplicacao(a, b):
  return a * b
# A função divisao() recebe dois números como parâmetros e retorna a divisão deles
def divisao(a, b):
  return a / b
# A função main() é a função principal do programa
def main():
  print("Selecione a operação desejada:")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")

  opcao = int(input())

  a = int(input("Digite o primeiro número: "))
  b = int(input("Digite o segundo número: "))

# O programa então chama a função correspondente à operação escolhida e imprime o resultado
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