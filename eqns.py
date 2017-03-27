import pysmt.shortcuts as SMT
from pysmt.typing import INT

variables = []
cap = 4
for n in range(1,cap+1):
    variables.append(SMT.Symbol("a" + str(n), INT))
    variables.append(SMT.Symbol("b" + str(n), INT))
    variables.append(SMT.Symbol("c" + str(n), INT))
variables.append(SMT.Symbol("S", INT))
print(variables)

constraints = []
for var in variables:
    string = var.__repr__()
    if string[0] == "a" or string[0] == "c":
        constraints.append(SMT.GT(var, SMT.Int(-1)))
    else:
        constraints.append(SMT.GT(var, SMT.Int(0)))

for i in range(0, 3*cap, 3):
    constraints.append(SMT.Or(SMT.Equals(variables[i], SMT.Int(0)), SMT.Equals(variables[i+2], SMT.Int(0))))
    constraints.append(SMT.Or(SMT.Or(SMT.GT(variables[i], SMT.Int(0)), SMT.GT(variables[i+2], SMT.Int(0))), SMT.Equals(variables[i+1], SMT.Int(1))))

print(constraints)
solver = SMT.Solver(name="z3")
for c in constraints:
    solver.add_assertion(c)

solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(75235), variables[1]), 
    SMT.Times(SMT.Int(24727), variables[0])), SMT.Times(SMT.Int(50508), variables[2]))))
solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(125743), variables[4]), 
    SMT.Times(SMT.Int(75235), variables[3])), SMT.Times(SMT.Int(176251), variables[5]))))
solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(301994), variables[7]),
    SMT.Times(SMT.Int(125743), variables[6])), SMT.Times(SMT.Int(16785921), variables[8]))))
solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(17087915), variables[10]),
    SMT.Times(SMT.Int(301994), variables[9])), SMT.Times(SMT.Int(85137581), variables[11]))))

print(solver.solve())
for var in variables:
    print(str(var) + " := " + str(solver.get_value(var)))

