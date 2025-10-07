def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario >= 1100 and salario <= 2500):
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario

valor_salario = float(input ("Digite o salário: "))
valor_beneficio = float(input ("Digite o valor do benefício: "))

valor_imposto = calcular_imposto(valor_salario)

saida = (valor_salario - valor_imposto) + valor_beneficio

print(f"Salário Líquido Estimado: {saida:.2f}")

