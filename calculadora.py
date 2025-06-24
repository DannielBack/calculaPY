print ('calculadora')

print ('escolha as seguintes operações...')
print ('soma, divisao,multiplicaçao,subtraçao...')
escolha = input('digite uma operaçao').strip().lower()

if escolha == 'soma':

    n =int(input('digite o numero'))
    n1 =int(input('digite outro'))
    s = n + n1
    print(f'{n} + {n1} = {s}')


if escolha == 'divisao':
    n =float(input('digite um numero'))
    n1 =float(input('digite outro'))
    d = n / n1     
    print(f'{n} / {n1} = {d}')


if escolha == 'multiplicaçao':
        n =int(input('digite um numero'))
        n2 =int(input('digite outro'))
        m = n * n2
        print(f'{n} * {n2} = {m}')


if escolha == 'subtraçao':
    n =int(input('digite um numero'))
    n2 =int(input('digite outro'))
    r = n - n2
    print(f'{n} - {n2} = {r}')
