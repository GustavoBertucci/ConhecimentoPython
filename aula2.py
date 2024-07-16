# # Algoritimo --> sequência de passos para executar uma tarefa

# # 3 estruturas possiveis no algoritimo:

# # 1 Estrutural (sequencia de passos continuos)
# # 2 Condicional (DECISAO - vou executar um script diferente se acontecer X e outro se Y)
# # 3 Repetição (Permite executar varias vezes  o mesmo código)

# # variaveis --> espaços de memória que podem conter diversas informações

# # Int --> numeros inteiros (1, 2, 3, 3, ...)
# # Str --> cadeia de caracteres (nomes, ruas, palavras, CPF, ... tudo escrtiro entre " " ou ' ')
# # Float --> numeros fracionados (1.2, 43.56, 2.344, ...)
# # Boolean --> True or False (verdadeiro ou falso)

# curso = "Manufatura Digital"
# # a variavel "curso" recebeu o valor "Manufatura Digital" 


# # exibir --> comando Print
# print("Usuario eu sou seu py")

# # para conversar com o usuario eu uso o input
# altura = float(input("Digite sua altura "))
# # a variavel altura recebe um valor quebrado dada pelo usuario

# print(f"sua altura é de {altura}")

# print("Cadastro de uma pessoa")
# nm = input("Digite seu nome ")
# idd = input("Digite sua idade ")
# edc = input("Digite seu endereço ")
# cpf = input("digite seu CPF ")
# km = input("Digite a distancia percorrida no dia ")
# an = input("Digite seu ano de nascimento ")
# print (nm, idd, edc, cpf, km, an)

salario = float(input("Digite seu salário"))

if(salario => 1500):
    print(f"seu salário é de {salario + 500}")

elif(salario => 2000):
    print(f"seu salário é de {salario + 400}")

elif(salario => 3000):
    print(f"seu salário é de {salario + 300}")
