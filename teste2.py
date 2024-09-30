def fibonacci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def pertence_fibonacci(num):

    fib = 0
    while fib <= num:
        if fib == num:
            return True
        fib = fibonacci(fib + 1)
        return False
    
    numero = int(input("Digite um número: "))

    if pertence_fibonacci(numero):
        print(f'O número {numero} pertence à sequência de Fibonnacci.')
    else:
        print(f'O número {numero} não pertence à sequência de Fibonacci.')
