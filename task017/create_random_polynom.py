from random import randint

def create_random_polynom(x_max_degree):
    degrees = []
    for i in range(1, x_max_degree+1):
        degrees.append(i)

    coeffs = []
    for i in range(x_max_degree):
        coeffs.append(randint(0, 10))

    # expression = 0
    expression_string = ''
    c = randint(0, 10)

    for i in range(x_max_degree):
        if coeffs[i] > 0:
            expression_string += f'{coeffs[i]}*x^{degrees[i]} + '
        # expression += coeffs[i]*x**degrees[i]

    if expression_string != '':
        if c != 0:
            expression_string += f'{c}'
        else:
            expression_string = expression_string[:-3]
        expression_string += ' = 0'
        # print(expression_string)
    else:
        expression_string = 'Все коэффиценты многочлена равны 0'
    # expression += c
    return expression_string