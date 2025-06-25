print ('calculapy')

print ('escolha as seguintes operações matemáticas :')
print ('[1*]para somar.\n[2*] para dividir.\n[3*] para multiplicar.\n[4*]para subtrair')
choose = input('escolha uma operação :').strip()

if choose == '1':
    print('escolhestes somar')
    n =int(input('digite um numero :'))
    n1 =int(input('digite outro '))
    s = n + n1
    print(f'{n} + {n1} = {s}')


if choose == '2':
    print('escolhestes dividir')
    n =float(input('digite um numero'))
    n1 =float(input('digite outro'))
    d = n / n1     
    print(f'{n} / {n1} = {d}')


if choose == '3':
        print('escolhestes multiplicar')
        n =int(input('digite um numero'))
        n2 =int(input('digite outro'))
        m = n * n2
        print(f'{n} * {n2} = {m}')


if choose == '4':
    print('escolhestes subtrair')
    n =int(input('digite um numero'))
    n2 =int(input('digite outro'))
    r = n - n2
    print(f'{n} - {n2} = {r}')
