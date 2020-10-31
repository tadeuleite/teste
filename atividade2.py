def calcularComissao():
    nome = str(input('Digite seu nome: '))
    valorVenda = float(input('Digite a valor da venda: '))

    if valorVenda >= 50000:
        comissao = valorVenda * 0.12
        valorTotal = valorVenda + comissao
    elif valorVenda >= 30000 and valorVenda <= 50000:
        comissao = valorVenda * 0.095
        valorTotal = valorVenda + comissao
    else:
        comissao = valorVenda * 0.07
        valorTotal = valorVenda + comissao

    print(f'Olá, {nome} o valor total da sua venda foi R${valorTotal} e sua comissão foi de R${comissao}')

def diasVividos():
    numeroAnos = int(input('Digite sua idade: '))
    numeroDiasEmAnos = numeroAnos * 365
    print(f'Você viveu {numeroDiasEmAnos} de dias')

def somarValores():
    numeroA = int(input('Digite o valor de A: '))
    numeroB = int(input('Digite o valor de B: '))
    numeroC = int(input('Digite o valor de C: '))

    isMaiorIgualC = (numeroA + numeroB) == numeroC

    if isMaiorIgualC:
        print(f'O valor de A + B é maior ou igual que C')
    else:
        print(f'O valor de A + B é menor que C')
    
def notasTroco():
    pagamento = int(input(f'Valor a pagar: '))
    notasCem = int(pagamento/100)
    notasDez = int((pagamento%100)/10)
    notasUm = int((pagamento%10)/1)

    print(f'Valor da compra: R${pagamento},00 de 100: {notasCem} | Notas de 10: {notasDez} | Notas de 1: {notasUm}')
    

def pecasMecanicas():
    nome = str(input(f'Digite seu nome: '))
    parafusoPagar = float(input(f'Valor a pagar parafuso: '))
    porcaPagar = float(input(f'Valor a pagar porca: '))
    arruelaPagar = float(input(f'Valor a pagar arruela: '))

    parafusoDesconto = float(parafusoPagar/0.10 + parafusoPagar)
    porcaDesconto = float(porcaPagar/0.20 + porcaPagar)
    arruelaDesconto = float(arruelaPagar/0.30 + arruelaPagar)
    
    valorTotal = parafusoDesconto + porcaDesconto + arruelaDesconto
    
    print(f'Olá {nome}, o valor total da compra foi: {valorTotal}')


calcularComissao()
diasVividos()
somarValores()
notasTroco()
pecasMecanicas()