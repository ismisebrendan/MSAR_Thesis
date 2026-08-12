expr = ''



expr = expr.replace('HeavisideTheta[\[Tau]1-\[Tau]2]', '0')
expr = expr.replace('HeavisideTheta[-\[Tau]1+\[Tau]2]', '')
expr = expr.replace('^\[Prime]', '\'')
expr = expr.replace('\[', '\\')
expr = expr.replace('Pi]', 'pi')
expr = expr.replace('Xi]', 'xi')
expr = expr.replace('Tau]', 'tau_')
expr = expr.replace('Omega]', 'omega')
expr = expr.replace('tprime', 't\'')
expr = expr.replace('Abs[z0]', '|z_0|')
expr = expr.replace('z0', 'z_0')
expr = expr.replace('Rho]0', 'rho_0')
expr = expr.replace('DiracDelta', '\delta')
expr = expr.replace('HeavisideTheta', '\Theta')
expr = expr.replace('SinIntegral', 'Si')
expr = expr.replace('CosIntegral', 'Ci')
expr = expr.replace('ExpIntegralEi', 'Ei')
expr = expr.replace('[', '(')
expr = expr.replace('(', '\left(')
expr = expr.replace(']', ')')
expr = expr.replace(')', '\\right)')
expr = expr.replace('+\\tau1 0', '')
expr = expr.replace('-\\tau1 0', '')
expr = expr.replace('+\\tau2 0', '')
expr = expr.replace('-\\tau2 0', '')
expr = expr.replace('tau1 1', 'tau1')
expr = expr.replace('tau2 1', 'tau2')


print(expr)