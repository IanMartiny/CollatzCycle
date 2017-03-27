import pysmt.shortcuts as SMT
from pysmt.typing import INT

variables = []
cap = 4
# add a_i, b_i, c_i variables for each equation
for n in range(1,cap+1):
    variables.append(SMT.Symbol("a" + str(n), INT))
    variables.append(SMT.Symbol("b" + str(n), INT))
    variables.append(SMT.Symbol("c" + str(n), INT))
variables.append(SMT.Symbol("S", INT))
print(variables)

constraints = []
for var in variables:
    string = var.__repr__()
    # add requirement that all a_i, c_i > -1
    if string[0] == "a" or string[0] == "c":
        constraints.append(SMT.GT(var, SMT.Int(-1)))
    # add requirement that b_i > 0
    else:
        constraints.append(SMT.GT(var, SMT.Int(0)))

for i in range(0, 3*cap, 3):
    # add requirement that either a_i =0 or c_i = 0
    constraints.append(SMT.Or(SMT.Equals(variables[i], SMT.Int(0)), SMT.Equals(variables[i+2], SMT.Int(0))))
    # add requirement that if a_i = 0 and c_i = 0 then b_i = 1
    constraints.append(SMT.Or(SMT.Or(SMT.GT(variables[i], SMT.Int(0)), SMT.GT(variables[i+2], SMT.Int(0))), SMT.Equals(variables[i+1], SMT.Int(1))))

print(constraints)
solver = SMT.Solver(name="z3")
for c in constraints:
    solver.add_assertion(c)

# add equations

# 24727*a_1 + 75235*b_1 + 50508*c_1 = S
solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(75235), variables[1]), 
    SMT.Times(SMT.Int(24727), variables[0])), SMT.Times(SMT.Int(50508), variables[2]))))

# 75235*a_2 + 125743*b_2 + 176251*c_2 = S
solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(125743), variables[4]), 
    SMT.Times(SMT.Int(75235), variables[3])), SMT.Times(SMT.Int(176251), variables[5]))))

# 125743*a_3 + 301994*b_3 + 16785921*c_3 = S
solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(301994), variables[7]),
    SMT.Times(SMT.Int(125743), variables[6])), SMT.Times(SMT.Int(16785921), variables[8]))))

# 301994*a_4 + 17087915*b_4 + 85137581*c_4 = S
solver.add_assertion(SMT.Equals(variables[-1], SMT.Plus(SMT.Plus(SMT.Times(SMT.Int(17087915), variables[10]),
    SMT.Times(SMT.Int(301994), variables[9])), SMT.Times(SMT.Int(85137581), variables[11]))))

print(solver.solve())
for var in variables:
    print(str(var) + " := " + str(solver.get_value(var)))

