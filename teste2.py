def pertence_fibonacci(num):
    a = 0
    b = 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False


numero = int(input("Digite um número: "))


if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
