print ('calculadora')

print ('escolha as seguintes operações...')
print ('[1*]para soma.\n[2*] para divisao.\n[3*] para multiplicaçao.\[4*]para subtraçao...')
escolha = input('digite uma operaçao').strip().lower()

if escolha == '1':

    n =int(input('digite o numero'))
    n1 =int(input('digite outro'))
    s = n + n1
    print(f'{n} + {n1} = {s}')


if escolha == '2':
    n =float(input('digite um numero'))
    n1 =float(input('digite outro'))
    d = n / n1     
    print(f'{n} / {n1} = {d}')


if escolha == '3':
        n =int(input('digite um numero'))
        n2 =int(input('digite outro'))
        m = n * n2
        print(f'{n} * {n2} = {m}')


if escolha == '4':
    n =int(input('digite um numero'))
    n2 =int(input('digite outro'))
    r = n - n2
    print(f'{n} - {n2} = {r}')
