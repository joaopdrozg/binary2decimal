numero = input('Informe um número binário com até 8 digitos: ')

numero.split(",")

i = 0
soma = 0
expo = (len(numero) - 1)

if (len(numero) <= 8):

    while (i<= len(numero) - 1):
        if (int(numero[i]) == 0 or int(numero[i]) == 1):
            valor = int(numero[i]) * 2**expo
            soma = soma + valor
            i = i + 1
            expo = expo - 1
        else:
            print('Foi informado um digito diferente de 0 ou 1!')
            soma = " "
            break
    
else:
    print('Foi informado um número com mais de 8 digitos!')

print(soma)