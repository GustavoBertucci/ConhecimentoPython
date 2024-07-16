# nome = input("Digite o nome do seu refrigerante: ")
# empresa = input("Digite o nome da sua empresa: ")
# serial = input("DIgite o  número de EAN13 inicial da produção")
# sabor = input("Digite o sabor desse refrigerante")
# kcal = input("Digite a cáloria total do refrigerante")
# desing = input("Digite o desing de como será a garrafa do seu refrigerante")
# fabricacao = input("Descreva a sua fabricação do refrigerante")
# validade = input("Digite a validade do seu primeiro lote")
# receita = input("Digite a receita do seu refrigerante")
# armaz =  input("Como você armazena seus refrigerantes?")
# embalagem = input("Como são suas embalagens?")
# preco = int(input("qual o preço do seus refrigerantes"))
# transporte = input("Como você transporta seus refrigerantes")

Produto = input("Digite o que irá ser comprado: ")
preco = float(input("Digite o valor desse produto: "))
pagamento = int(input("Informe sua forma de pagamento \n [1]- Dinheiro \n [2]-Crédito \n [3]-Débito \n [4]-Pix \n Digite aqui: "))

limite = 300
saldo = 400
senha = "123456"

if pagamento == 1:
    dinnheiro = float(input("Qual o valor em espécie? "))
    if (dinnheiro > preco):
        print("Parabéns pela compra, seu troco é de R$", dinnheiro - preco)
    elif (dinnheiro == preco):
        print("Parabéns pela compra")
    else:
        print("Esse valor é insuficiente")

elif pagamento == 2:
    if limite >= preco:
        op = input("Deseja parcelar sua compra digite S - sim ou N - não: ")
        senhadigitar = input("Digite sua senha: ")
        if (senha == senhadigitar):
            print("Senha correta")
            if (op == "n"):
                print("Parabéns pela sua compra")
            elif (op == "s"):
                nparcela = int(input("Em quantas parcelas você deseja fazer? (Zero não é um valor válido)"))
                print("Parabéns pela compra, suas parcelas serão de R$", preco/nparcela)
            else:
                print("Digite um valor válido")
        else:
            print("Senha inválida")
    else:
        print("Desculpe, seu limite é insuficiente")

elif pagamento == 3:
    if (saldo >= preco):
        senhadigitar2 = input("Digite sua senha")
        if (senhadigitar2 == senha):
            print("Senha correta")
            print("Parabéns pela compra")
        else:
            print("Senha inválida")
    else:
        print("Seu saldo é insuficiente")

elif pagamento == 4:
    if (saldo >= preco):
        print("Parabéns pela compra")
    else:
        print("Seu saldo é insuficiente")
else:
    print("Valor ínvalido")