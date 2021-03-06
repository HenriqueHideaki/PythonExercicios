# -*- coding: utf-8 -*-
"""EstruturaDeDecisao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IDIXkAzhfO9iII8aRnqteLpiJ2SJU56W

1) Faça um Programa que peça dois números e imprima o maior deles.
"""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if(num1 > num2):
  print('O maior número é',num1)
elif(num1 < num2):
  print('O maior número é: ',num2)
else:
  print('São iguais')

"""2) Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

num = float(input('Digite um número:  '))
if(num % 2 == 0):
  print('Par')
else:
  print('Ímpar')

"""3) Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

letra = str(input('Digite uma letra'))

# if(letra == 'f' or letra == 'F'):
#   print('Sexo Feminino')
# elif(letra == 'm' or letra == 'M'):
#   print('Sexo Masculino')
# else:
#   print('Sexo Indefinido')

if(letra in 'fF'):
  print('Sexo Feminino')
elif(letra in 'mM'):
  print('Sexo Masculino')
else:
  print('Sexo Indefinido')

"""4) Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = str(input('Digite uma letra'))

print("Vogal" if letra.upper() in 'AEIOU' else "Consoante")

# if(letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U'):
#   print('Vogal')
# else:
#   print('Consoante')



# if(letra.upper() in 'AEIOU'):
#   print('Vogal')
# else:
#   print('Consoante')

"""5) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
"""

nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media = (nota1+nota2) / 2

print('Aprovado' if media >= 7 else 'Reprovado')

# if media >=7 :
#   print('Aprovado')
# else:
#   print('Reprovado')

"""6) Faça um Programa que leia três números e mostre o maior deles."""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

if(num1 >= num2 and num1>= num3):
  print('O maior número é : ', num1)

elif(num2 >= num1 and num2>= num3):
  print('O maior número é : ', num2)

else:
  print('O maior número é : ', num3)

"""7) Faça um Programa que leia três números e mostre o maior e o menor deles."""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

if(num1 >= num2 and num1>= num3):
  maior = num1

elif(num2 >= num1 and num2>= num3):
  maior = num2

else:
  maior = num3


if(num1 <= num2 and num1 <= num3):
  menor = num1

elif(num2 <= num1 and num2<= num3):
  menor = num2

else:
  menor = num3

print('O maior número é {} e o menor número é {}'.format(maior,menor))

"""8) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

preco1 = float(input('Digite o preco do primeiro produto: '))
preco2 = float(input('Digite o preco do segundo produto: '))
preco3 = float(input('Digite o preco do terceiro produto: '))

if(preco1 <= preco2 and preco1 <= preco3):
  menor = preco1

elif(preco2 <= preco1 and preco2<= preco3):
  menor = preco2

else:
  menor = preco3

print('O menor preco é : ', menor)

"""9) Faça um Programa que leia três números e mostre-os em ordem decrescente."""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

if(num1 >= num2 >= num3):
  lista = [num1,num2,num3]
if(num1 >= num3 >= num2):
  lista = [num1,num3,num2]

if(num2 >= num1 >= num3):
  lista = [num2,num1,num3]
if(num2 >= num3 >= num1):
  lista = [num2,num3,num1]

if(num3 >= num2 >= num1):
  lista = [num3,num2,num1]
if(num3 >= num1 >= num2):
  lista = [num3,num1,num2]

print(f'Em ordem descrescente {lista}')

"""10) Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = str(input('Em que turno você estuda? Digite M-matutino ou V-Vespertino ou N- Noturno: '))

if turno.upper() == 'M':
  print('Bom Dia')
elif turno.upper() == 'V':
  print('Boa Tarde')
elif turno.upper() == 'N':
  print('Boa noite')
else:
  print('Valor Inválido')

"""as Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

*   salários até R$ 280,00 (incluindo) : aumento de 20%
*   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
*   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
*   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

        1.   o salário antes do reajuste;
        2.   o percentual de aumento aplicado;
        3.   o valor do aumento;
        4.   o novo salário, após o aumento.
"""

salario = float(input('Digite seu salario:  '))

if salario <= 280:
  ajuste = '20%'
  salario_novo = salario * 1.2
elif salario <= 700:
  ajuste = '15%'
  salario_novo = salario * 1.15
elif salario <= 1500:
  ajuste = '10%'
  salario_novo = salario * 1.1
else:
  ajuste = '5%'
  salario_novo = salario * 1.05

aumento = salario_novo - salario
print('O salario antes do reajuste de {} era {} agora é {}, ou seja, o aumento foi de {} '.format(ajuste,salario,salario_novo, aumento))

"""12) Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
"""

valor = float(input('Digite qual o valor da hora trabalhada : '))
horas = float(input('Digite quantas horas voce trabalha     : '))
bruto = valor * horas
ir = 0 
fgts = 0.11
inss = 0.10
if bruto <= 900:
  print('Isento')
elif bruto <= 1500:
  ir = 0.05
  str_ir = '5%'
elif bruto <= 2500:
  ir = 0.10
  str_ir = '10%'
else:
  ir = 0.2
  str_ir = '20%'

desconto = ( bruto * ir) + ( bruto * inss)
liquido = bruto - desconto

print('Salário Bruto: ({} * {})  :  R$ {}'.format(valor,horas, bruto))
print('(-) IR (5%)               :  R$ ',bruto*ir)
print('(-) INSS (10%)            :  R$ ',bruto*inss)
print('Total de descontos        :  R$', desconto )
print('\nSalario liquido         :  R$',liquido)

"""13) Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""

num = int(input('Digite um numero: '))

if num == 1:
  print('Domingo')
elif num == 2:
  print('Segunda')
elif num == 3:
  print('Terça')
elif num == 4:
  print('Quarta')
elif num == 5:
  print('Quinta')
elif num == 6:
  print('Sexta')
elif num == 7:
  print('Sábado')
else:
  print('Valor inválido')

"""14) Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:"""

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda  nota: '))
media = (nota1 + nota2)/2