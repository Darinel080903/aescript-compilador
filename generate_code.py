import re

python_code = ""
variables = []
value_variables = []
functions = []
for_result = []
function_bodies = {}


def operators(op, left, right):
    if op == '>':
        return int(left) > int(right)
    elif op == '<':
        return int(left) < int(right)


def generate_python_code(parsed_output):
    global python_code, variables, value_variables, functions
    for statement in parsed_output:
        print(statement)
        if statement[0] == 'print_statement':
            python_code = ""
            print(statement[1])
            if type(statement[1]) == int: #imprimir(1);
                python_code += f"{statement[1]}"
            elif type(statement[1]) == str: #imprimir("hola"); | imprimir(suma)
                print("ENTRE")
                print(statement[1])
                if statement[1] in variables:
                    index = variables.index(statement[1])
                    python_code += f"{value_variables[index]}"
                elif statement[1][0] == '"':
                    python_code += f"{statement[1]}"
                else:
                    python_code += f"VARIABLE NO DEFINIDA"
            elif type(statement[1]) == tuple:
                try:
                    if statement[1][1] in variables and statement[1][2]:  # suma + suma;
                        print("Entre3")
                        index1 = variables.index(statement[1][1])
                        index2 = variables.index(statement[1][2])
                        python_code += f"{value_variables[index1]} {statement[1][0]} {value_variables[index2]}"
                    elif statement[1][1][0] == '"' and statement[1][2][0] == '"':
                        print("Entre4")
                        python_code += f"{statement[1][1]}{statement[1][2]}"
                    elif statement[1][1] in variables and statement[1][2][0] == '"':
                        match = re.search(r'\".*?\"', statement[1][1])
                        print("Entre5")
                        index = variables.index(match.group(0)[1:-1])
                        python_code += f"{value_variables[index]}{statement[1][2]}"
                    elif statement[1][1][0] == '"' and statement[1][2] in variables:
                        match = re.search(r'\".*?\"', statement[1][1])
                        print("Entre6")
                        index = variables.index(statement[1][2])
                        python_code += f"{match.group(0)[1:-1]}{value_variables[index]}"
                    elif type(statement[1][1]) == int and type(statement[1][2]) == int:  # 1 + 1;
                        print("Entre7")
                        python_code += f"{statement[1][1]} {statement[1][0]} {statement[1][2]}"
                    else:
                        python_code += f"VARIABLE NO DEFINIDA"
                except:
                    python_code += f"ERROR EN COMPATIBILIDAD DE TIPOS"
        elif statement[0] == 'declaration':
            print(f"flat{statement[1]}")
            print(variables)
            python_code = ""
            if statement[1] in variables:
                print("hay doble")
                python_code += "VARIABLE DOBLE"
                break
            else:
                variables.append(statement[1])
                if type(statement[2]) != int:
                    match = re.search(r'\".*?\"', statement[2])
                    value_variables.append(match.group(0)[1:-1])
                else:
                    value_variables.append(statement[2])
        elif statement[0] == 'function_declaration':
            print("FUNCTION DECLARATION")
            print(statement[2])
            if statement[2] == 'correr':
                generate_python_code(statement[4])
            else:
                python_code = ""
                functions.append(statement[1])
                function_bodies[statement[1]] = statement[3]
        elif statement[0] == 'iterate_statement':
            for_result.clear()
            for i in range(statement[1]):
                generate_python_code(statement[2])
                 
                left = value_variables[variables.index(statement[1])]
            else:
                left = statement[1]
            if statement[3] in variables:
                right = value_variables[variables.index(statement[3])]
            else:
                right = statement[3]
            if operators(statement[2], left, right):
                new_statement = [statement[4]]
                generate_python_code(new_statement)
            else:
                python_code = "CARACTERES INCORRECTOS"
        elif statement[0] == 'call_function':
            print(functions)
            if statement[1] in functions:
                generate_python_code(function_bodies[statement[1]])
            else:
                python_code = "FUNCION NO DEFINIDA"
    if len(for_result) > 0:
        return for_result
    else:
        return python_code
