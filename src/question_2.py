"""

Como o programa nos pede para verificar se um número pertence à sequência de Fibonacci, 
mas não nos pede para retornar a sequência de Fibonacci até o n-ésimo termo,
então, não precisamos salvar a sequencia até o n-ésimo termo.
Portanto, a função fibonacci(n) precisa apenas  encontrar o número pedido
ou um número maior que o pedido, mostrando assim que não pertence à sequência de Fibonacci.

"""

def fibonacci(n):
    fib = [0, 1]
    
    while True:
        next_value = fib[0] + fib[1]
        
        if next_value == n:
            print("O número", n, "pertence à sequência de Fibonacci")
            return 
        elif next_value > n:
            print ("O número", n, "não pertence à sequência de Fibonacci")
            return 
        
        fib = [fib[1],next_value]


def main():
    n = int(input("Digite o número a ser verificado: "))
    fibonacci(n)


if __name__ == "__main__":
    main()
