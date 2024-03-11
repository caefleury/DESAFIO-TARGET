"""

Nessa abordagem eu criei uma função que recebe uma string e retorna a string invertida.
A função reverse_string(text) recebe uma string e retorna a string invertida.
Para inverter a string, eu criei uma variável reversed_string que recebe a string invertida.
A cada iteração, eu pego um caractere da string e coloco ele na frente (esquerda) da reversed_string.

"""


def reverse_string(text):
    reversed_string = ""
    for char in text:
        reversed_string = char + reversed_string
    return reversed_string


def main():
    string = input("Digite a string a ser invertida: ")
    print(reverse_string(string))

if __name__ == "__main__":
    main()
