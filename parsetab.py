
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNACION CORRER FUNCION ID IMPRIMIR ITERAR LLAVE_DERECHA LLAVE_IZQUIERDA MAS MAYOR_QUE MENOR_QUE MENOS NUMERO OPERADOR_FLUJO PARENTESIS_DERECHO PARENTESIS_IZQUIERDO PUNTO_Y_COMA REALIZA SI STRING VARIABLE VECES\n    program : program declaration\n            | declaration\n    \n    function_declaration : FUNCION ID OPERADOR_FLUJO LLAVE_IZQUIERDA program LLAVE_DERECHA\n    | FUNCION ID CORRER OPERADOR_FLUJO LLAVE_IZQUIERDA program LLAVE_DERECHA\n    \n    iterate_statement : ITERAR NUMERO VECES OPERADOR_FLUJO program\n    \n    expressionop : expression MAS expression\n               | expression MENOS expression\n               | expression MAYOR_QUE expression\n    \n    conditional_statement : SI expression MAYOR_QUE expression REALIZA LLAVE_IZQUIERDA declaration LLAVE_DERECHA\n                        | SI expression MENOR_QUE expression REALIZA LLAVE_IZQUIERDA declaration LLAVE_DERECHA\n    \n    print_statement : IMPRIMIR PARENTESIS_IZQUIERDO expressionop PARENTESIS_DERECHO PUNTO_Y_COMA\n                    | IMPRIMIR PARENTESIS_IZQUIERDO expression PARENTESIS_DERECHO PUNTO_Y_COMA\n    \n    declaration : variable_declaration\n                | function_declaration\n                | iterate_statement\n                | print_statement\n                | conditional_statement\n                | call_function\n                | expressionop\n                | expressionop PUNTO_Y_COMA\n    \n    call_function : OPERADOR_FLUJO ID PUNTO_Y_COMA\n    \n    variable_declaration : VARIABLE ID ASIGNACION expression PUNTO_Y_COMA\n    \n    expression : NUMERO\n               | ID\n               | STRING\n    '
    
_lr_action_items = {'VARIABLE':([0,1,2,3,4,5,6,7,8,9,11,16,19,20,21,32,33,34,37,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[10,10,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,-6,-7,-8,-21,10,10,-22,10,10,10,-11,-12,-3,10,10,10,-4,-9,-10,]),'FUNCION':([0,1,2,3,4,5,6,7,8,9,11,16,19,20,21,32,33,34,37,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[13,13,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,-6,-7,-8,-21,13,13,-22,13,13,13,-11,-12,-3,13,13,13,-4,-9,-10,]),'ITERAR':([0,1,2,3,4,5,6,7,8,9,11,16,19,20,21,32,33,34,37,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[15,15,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,-6,-7,-8,-21,15,15,-22,15,15,15,-11,-12,-3,15,15,15,-4,-9,-10,]),'IMPRIMIR':([0,1,2,3,4,5,6,7,8,9,11,16,19,20,21,32,33,34,37,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[17,17,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,-6,-7,-8,-21,17,17,-22,17,17,17,-11,-12,-3,17,17,17,-4,-9,-10,]),'SI':([0,1,2,3,4,5,6,7,8,9,11,16,19,20,21,32,33,34,37,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[18,18,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,-6,-7,-8,-21,18,18,-22,18,18,18,-11,-12,-3,18,18,18,-4,-9,-10,]),'OPERADOR_FLUJO':([0,1,2,3,4,5,6,7,8,9,11,16,19,20,21,26,32,33,34,36,37,38,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[14,14,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,35,-6,-7,-8,45,-21,46,14,14,-22,14,14,14,-11,-12,-3,14,14,14,-4,-9,-10,]),'NUMERO':([0,1,2,3,4,5,6,7,8,9,11,15,16,18,19,20,21,23,24,25,29,31,32,33,34,37,41,42,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[16,16,-2,-13,-14,-15,-16,-17,-18,-19,-24,28,-23,16,-25,-1,-20,16,16,16,16,16,-6,-7,-8,-21,16,16,16,16,-22,16,16,16,-11,-12,-3,16,16,16,-4,-9,-10,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,16,18,19,20,21,23,24,25,29,31,32,33,34,37,41,42,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[11,11,-2,-13,-14,-15,-16,-17,-18,-19,22,-24,26,27,-23,11,-25,-1,-20,11,11,11,11,11,-6,-7,-8,-21,11,11,11,11,-22,11,11,11,-11,-12,-3,11,11,11,-4,-9,-10,]),'STRING':([0,1,2,3,4,5,6,7,8,9,11,16,18,19,20,21,23,24,25,29,31,32,33,34,37,41,42,44,46,51,52,53,54,55,56,59,60,61,62,63,66,67,],[19,19,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,19,-25,-1,-20,19,19,19,19,19,-6,-7,-8,-21,19,19,19,19,-22,19,19,19,-11,-12,-3,19,19,19,-4,-9,-10,]),'$end':([1,2,3,4,5,6,7,8,9,11,16,19,20,21,32,33,34,37,51,54,55,56,59,63,66,67,],[0,-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,-6,-7,-8,-21,-22,-5,-11,-12,-3,-4,-9,-10,]),'LLAVE_DERECHA':([2,3,4,5,6,7,8,9,11,16,19,20,21,32,33,34,37,51,52,54,55,56,59,60,63,64,65,66,67,],[-2,-13,-14,-15,-16,-17,-18,-19,-24,-23,-25,-1,-20,-6,-7,-8,-21,-22,59,-5,-11,-12,-3,63,-4,66,67,-9,-10,]),'PUNTO_Y_COMA':([9,11,16,19,27,32,33,34,43,47,48,],[21,-24,-23,-25,37,-6,-7,-8,51,55,56,]),'MAS':([11,12,16,19,40,],[-24,23,-23,-25,23,]),'MENOS':([11,12,16,19,40,],[-24,24,-23,-25,24,]),'MAYOR_QUE':([11,12,16,19,30,40,],[-24,25,-23,-25,41,25,]),'MENOR_QUE':([11,16,19,30,],[-24,-23,-25,42,]),'PARENTESIS_DERECHO':([11,16,19,32,33,34,39,40,],[-24,-23,-25,-6,-7,-8,47,48,]),'REALIZA':([11,16,19,49,50,],[-24,-23,-25,57,58,]),'PARENTESIS_IZQUIERDO':([17,],[29,]),'ASIGNACION':([22,],[31,]),'CORRER':([26,],[36,]),'VECES':([28,],[38,]),'LLAVE_IZQUIERDA':([35,45,57,58,],[44,53,61,62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,44,46,53,],[1,52,54,60,]),'declaration':([0,1,44,46,52,53,54,60,61,62,],[2,20,2,2,20,2,20,20,64,65,]),'variable_declaration':([0,1,44,46,52,53,54,60,61,62,],[3,3,3,3,3,3,3,3,3,3,]),'function_declaration':([0,1,44,46,52,53,54,60,61,62,],[4,4,4,4,4,4,4,4,4,4,]),'iterate_statement':([0,1,44,46,52,53,54,60,61,62,],[5,5,5,5,5,5,5,5,5,5,]),'print_statement':([0,1,44,46,52,53,54,60,61,62,],[6,6,6,6,6,6,6,6,6,6,]),'conditional_statement':([0,1,44,46,52,53,54,60,61,62,],[7,7,7,7,7,7,7,7,7,7,]),'call_function':([0,1,44,46,52,53,54,60,61,62,],[8,8,8,8,8,8,8,8,8,8,]),'expressionop':([0,1,29,44,46,52,53,54,60,61,62,],[9,9,39,9,9,9,9,9,9,9,9,]),'expression':([0,1,18,23,24,25,29,31,41,42,44,46,52,53,54,60,61,62,],[12,12,30,32,33,34,40,43,49,50,12,12,12,12,12,12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program declaration','program',2,'p_program','sintaxis.py',7),
  ('program -> declaration','program',1,'p_program','sintaxis.py',8),
  ('function_declaration -> FUNCION ID OPERADOR_FLUJO LLAVE_IZQUIERDA program LLAVE_DERECHA','function_declaration',6,'p_function_declaration','sintaxis.py',19),
  ('function_declaration -> FUNCION ID CORRER OPERADOR_FLUJO LLAVE_IZQUIERDA program LLAVE_DERECHA','function_declaration',7,'p_function_declaration','sintaxis.py',20),
  ('iterate_statement -> ITERAR NUMERO VECES OPERADOR_FLUJO program','iterate_statement',5,'p_iterate_statement','sintaxis.py',27),
  ('expressionop -> expression MAS expression','expressionop',3,'p_operations','sintaxis.py',34),
  ('expressionop -> expression MENOS expression','expressionop',3,'p_operations','sintaxis.py',35),
  ('expressionop -> expression MAYOR_QUE expression','expressionop',3,'p_operations','sintaxis.py',36),
  ('conditional_statement -> SI expression MAYOR_QUE expression REALIZA LLAVE_IZQUIERDA declaration LLAVE_DERECHA','conditional_statement',8,'p_conditional_statement','sintaxis.py',43),
  ('conditional_statement -> SI expression MENOR_QUE expression REALIZA LLAVE_IZQUIERDA declaration LLAVE_DERECHA','conditional_statement',8,'p_conditional_statement','sintaxis.py',44),
  ('print_statement -> IMPRIMIR PARENTESIS_IZQUIERDO expressionop PARENTESIS_DERECHO PUNTO_Y_COMA','print_statement',5,'p_print_statement','sintaxis.py',51),
  ('print_statement -> IMPRIMIR PARENTESIS_IZQUIERDO expression PARENTESIS_DERECHO PUNTO_Y_COMA','print_statement',5,'p_print_statement','sintaxis.py',52),
  ('declaration -> variable_declaration','declaration',1,'p_declaration','sintaxis.py',59),
  ('declaration -> function_declaration','declaration',1,'p_declaration','sintaxis.py',60),
  ('declaration -> iterate_statement','declaration',1,'p_declaration','sintaxis.py',61),
  ('declaration -> print_statement','declaration',1,'p_declaration','sintaxis.py',62),
  ('declaration -> conditional_statement','declaration',1,'p_declaration','sintaxis.py',63),
  ('declaration -> call_function','declaration',1,'p_declaration','sintaxis.py',64),
  ('declaration -> expressionop','declaration',1,'p_declaration','sintaxis.py',65),
  ('declaration -> expressionop PUNTO_Y_COMA','declaration',2,'p_declaration','sintaxis.py',66),
  ('call_function -> OPERADOR_FLUJO ID PUNTO_Y_COMA','call_function',3,'p_call_function','sintaxis.py',73),
  ('variable_declaration -> VARIABLE ID ASIGNACION expression PUNTO_Y_COMA','variable_declaration',5,'p_variable_declaration','sintaxis.py',80),
  ('expression -> NUMERO','expression',1,'p_expression_number','sintaxis.py',87),
  ('expression -> ID','expression',1,'p_expression_number','sintaxis.py',88),
  ('expression -> STRING','expression',1,'p_expression_number','sintaxis.py',89),
]