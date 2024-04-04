num1 = int(input("Digite seu primeiro numero:"))
num2 = int(input("Digite seu segundo numero:"))
operacao = input("Digite a operacao que dseja ralizar (+, -, *, /):")

if operacao == "+":
    print(num1+num2)
elif operacao == "-":
    print(num1-num2)
elif operacao == "*":
    print(num1*num2)
elif operacao == "/":
    print(num1/num2)
else:
    print("Operação inválida")