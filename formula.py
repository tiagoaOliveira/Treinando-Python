# V= D/T

def conta(formula):
    valores = formula.replace(' ', '')
    V = valores[0]
    D = valores[2]
    T= valores[4]

    if D.isnumeric() and T.isnumeric():
        if valores[3] == '+':
            print(f'V = {float(D) + float(T)}')
        elif valores[3] == '-':
            print(f'V = {float(D) - float(T)}')
        elif valores[3] == '*':
            print(f'V = {float(D) * float(T)}')
        elif valores[3] == '/':
            print(f'V = {float(D) / float(T)}')

    elif V.isnumeric() and D.isnumeric():
        if valores[3] == '+':
            print(f'T = {float(V) - float(D)}')
        elif valores[3] == '-':
            print(f'T = {-float(V) + float(D)}')
        elif valores[3] == '*':
            print(f'T = {float(V) / float(D)}')
        elif valores[3] == '/':
            if V > D:
                print(f'T = {float(D) / float(V)}')
            else:
                print(f'T = {float(V) * float(D)}')

    elif V.isnumeric() and T.isnumeric():
        if valores[3] == '+':
            print(f'D = {float(V) - float(T)}')
        elif valores[3] == '-':
            print(f'D = {float(V) + float(T)}')
        elif valores[3] == '*':
            print(f'D = {float(V) / float(T)}')
        elif valores[3] == '/':
            print(f'D = {float(V) * float(T)}')

conta(input('Digite a fórmula').upper())