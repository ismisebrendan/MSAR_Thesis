expr = 'L_1 = & 8 ab d K_1 left(t+2 z_0-tau_1+2 z_0 ln{left(frac{t-tau_1}{-2 z_0}right)}right)    &+Ka_1 left(-Eileft(b z_0right)+E_1+e^{b z_0} ln{left(frac{2 z_0}{-t+tau_1}right)}right)    L_2 = &8 ab d K_2 left(t+2 z_0-tau_2+2 z_0 ln{left(frac{t-tau_2}{-2 z_0}right)}right)    &+Ka_2 left(-Eileft(b z_0right)+E_2+e^{b z_0} ln{left(frac{2 z_0}{-t+tau_2}right)}right)'


expr = expr.replace('{', '(')
expr = expr.replace('}', ')')
for i in range(10):
    print(i)
    if '  ' in expr:
        expr = expr.replace('  ', ' ')
    else:
        break

expr = expr.replace('left.', '')
expr = expr.replace('left', '')
expr = expr.replace('right.', '')
expr = expr.replace('right', '')

for i in range(10):
    expr = expr.replace(f'{i} (', f'{i}(')    
    expr = expr.replace(f') {i}', f'){i}')

while True:
    expr = expr.replace('( ', '(')
    if '( ' not in expr:
        break

while True:
    expr = expr.replace(' )', ')')
    if ' )' not in expr:
        break

expr = expr.replace('_', '')
expr = expr.replace('&', '')
expr = expr.replace(' + ', '+')
expr = expr.replace('+ ', '+')
expr = expr.replace(' +', '+')
expr = expr.replace(' +', '+')
expr = expr.replace(' - ', '-')
expr = expr.replace('- ', '-')
expr = expr.replace(' -', '-')
expr = expr.replace(' = ', '=')
expr = expr.replace('= ', '=')
expr = expr.replace(' =', '=')
expr = expr.replace('^', '**')
expr = expr.replace(' ', ' * ')
expr = expr.replace('Log', 'np.log')
expr = expr.replace('ln', 'np.log')
expr = expr.replace('cos', 'np.cos')
expr = expr.replace('sin', 'np.sin')
expr = expr.replace('pi', 'np.pi')
expr = expr.replace('Theta', 'np.heaviside')
expr = expr.replace('delta(', 'dirac_delta(t, ')
expr = expr.replace('-', ' - ')
expr = expr.replace('+', ' + ')


print(expr)