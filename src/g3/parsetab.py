
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programleftPLUSMINUSleftMULDIVCATCH CLASS COLON COMMA DEBUG DIV DO DOT ELSE END EQUAL FLOAT FOR FUNCTION GLOBAL IDENTIFIER IF IN INT LB LBB LIST LMB LSB MINUS MUL NOTEQUAL PLUS PYTHON RB RBB REPEAT RMB RSB SEMI STRING TRY USE VAR WHILE\n    program : root\n    \n    root : root statement\n        | statement\n    \n    statement : if_statement\n        | while_statement\n        | variable_declaration SEMI\n        | variable_value_change SEMI\n        | function_declaration\n        | empty\n    statement : expression SEMI\n    expression : calculate\n        | string_calculate\n        | compare_expression\n        | function_call\n    \n    variable_declaration : VAR IDENTIFIER EQUAL expression\n    \n    variable_value_change : IDENTIFIER EQUAL expression\n    function_call : IDENTIFIER LSB function_call_parameter RSB\n    function_call_parameter : function_call_parameter COMMA calculate\n        | calculate\n        | empty\n    function_declaration : FUNCTION IDENTIFIER LSB function_parameter RSB LMB root RMB\n    function_parameter : function_parameter COMMA IDENTIFIER\n        | IDENTIFIER\n        | empty\n    while_statement : WHILE LSB compare_expression RSB LMB root RMB\n    if_statement : IF LSB compare_expression RSB LMB root RMB\n        | if_statement ELSE IF LSB compare_expression RSB LMB root RMB\n        | if_statement ELSE LMB root RMB\n    \n    compare_expression : compare_expression compare_operator calculate\n        | calculate\n    \n    compare_operator : LB\n        | RB\n        | LB EQUAL\n        | RB EQUAL\n        | EQUAL EQUAL\n        | NOTEQUAL EQUAL\n    \n    string_calculate : string_calculate stringoperator STRING\n        | STRING\n    \n    stringoperator : PLUS\n    \n    calculate : calculate baseoperator INT\n        | calculate baseoperator FLOAT\n    calculate : calculate baseoperator IDENTIFIERcalculate : INTcalculate : FLOAT\n    calculate : IDENTIFIER\n    \n    baseoperator : PLUS\n        | MINUS\n        | MUL\n        | DIV\n    empty : '
    
_lr_action_items = {'IF':([0,2,3,4,5,8,9,23,24,25,26,27,47,69,79,80,81,86,87,88,90,91,92,93,94,95,96,],[11,11,-3,-4,-5,-8,-9,-2,46,-6,-7,-10,11,11,-28,11,11,11,11,11,11,-26,-25,11,11,-21,-27,]),'WHILE':([0,2,3,4,5,8,9,23,25,26,27,47,69,79,80,81,86,87,88,90,91,92,93,94,95,96,],[13,13,-3,-4,-5,-8,-9,-2,-6,-7,-10,13,13,-28,13,13,13,13,13,13,-26,-25,13,13,-21,-27,]),'VAR':([0,2,3,4,5,8,9,23,25,26,27,47,69,79,80,81,86,87,88,90,91,92,93,94,95,96,],[14,14,-3,-4,-5,-8,-9,-2,-6,-7,-10,14,14,-28,14,14,14,14,14,14,-26,-25,14,14,-21,-27,]),'IDENTIFIER':([0,2,3,4,5,8,9,14,16,23,25,26,27,28,29,30,31,34,36,37,39,40,41,42,43,47,52,53,54,55,57,63,68,69,74,79,80,81,84,86,87,88,90,91,92,93,94,95,96,],[15,15,-3,-4,-5,-8,-9,35,38,-2,-6,-7,-10,50,50,-31,-32,50,58,50,66,-46,-47,-48,-49,15,-33,-34,-35,-36,58,75,50,15,50,-28,15,15,89,15,15,15,15,-26,-25,15,15,-21,-27,]),'FUNCTION':([0,2,3,4,5,8,9,23,25,26,27,47,69,79,80,81,86,87,88,90,91,92,93,94,95,96,],[16,16,-3,-4,-5,-8,-9,-2,-6,-7,-10,16,16,-28,16,16,16,16,16,16,-26,-25,16,16,-21,-27,]),'INT':([0,2,3,4,5,8,9,23,25,26,27,28,29,30,31,34,36,37,39,40,41,42,43,47,52,53,54,55,57,68,69,74,79,80,81,86,87,88,90,91,92,93,94,95,96,],[20,20,-3,-4,-5,-8,-9,-2,-6,-7,-10,20,20,-31,-32,20,20,20,64,-46,-47,-48,-49,20,-33,-34,-35,-36,20,20,20,20,-28,20,20,20,20,20,20,-26,-25,20,20,-21,-27,]),'FLOAT':([0,2,3,4,5,8,9,23,25,26,27,28,29,30,31,34,36,37,39,40,41,42,43,47,52,53,54,55,57,68,69,74,79,80,81,86,87,88,90,91,92,93,94,95,96,],[21,21,-3,-4,-5,-8,-9,-2,-6,-7,-10,21,21,-31,-32,21,21,21,65,-46,-47,-48,-49,21,-33,-34,-35,-36,21,21,21,21,-28,21,21,21,21,21,21,-26,-25,21,21,-21,-27,]),'STRING':([0,2,3,4,5,8,9,23,25,26,27,36,44,45,47,57,69,79,80,81,86,87,88,90,91,92,93,94,95,96,],[22,22,-3,-4,-5,-8,-9,-2,-6,-7,-10,22,67,-39,22,22,22,-28,22,22,22,22,22,22,-26,-25,22,22,-21,-27,]),'$end':([0,1,2,3,4,5,8,9,23,25,26,27,79,91,92,95,96,],[-50,0,-1,-3,-4,-5,-8,-9,-2,-6,-7,-10,-28,-26,-25,-21,-27,]),'RMB':([3,4,5,8,9,23,25,26,27,47,69,79,80,81,86,87,88,90,91,92,93,94,95,96,],[-3,-4,-5,-8,-9,-2,-6,-7,-10,-50,79,-28,-50,-50,91,92,-50,-50,-26,-25,95,96,-21,-27,]),'ELSE':([4,79,91,96,],[24,-28,-26,-27,]),'SEMI':([6,7,10,12,15,17,18,19,20,21,22,50,51,58,59,64,65,66,67,72,73,],[25,26,27,-13,-45,-11,-12,-14,-43,-44,-38,-45,-29,-45,-16,-40,-41,-42,-37,-15,-17,]),'LSB':([11,13,15,38,46,58,],[28,34,37,63,68,37,]),'LB':([12,15,17,20,21,48,49,50,51,56,58,64,65,66,78,],[30,-45,-30,-43,-44,30,-30,-45,-29,30,-45,-40,-41,-42,30,]),'RB':([12,15,17,20,21,48,49,50,51,56,58,64,65,66,78,],[31,-45,-30,-43,-44,31,-30,-45,-29,31,-45,-40,-41,-42,31,]),'EQUAL':([12,15,17,20,21,30,31,32,33,35,48,49,50,51,56,58,64,65,66,78,],[32,36,-30,-43,-44,52,53,54,55,57,32,-30,-45,-29,32,-45,-40,-41,-42,32,]),'NOTEQUAL':([12,15,17,20,21,48,49,50,51,56,58,64,65,66,78,],[33,-45,-30,-43,-44,33,-30,-45,-29,33,-45,-40,-41,-42,33,]),'PLUS':([15,17,18,20,21,22,49,50,51,58,61,64,65,66,67,82,],[-45,40,45,-43,-44,-38,40,-45,40,-45,40,-40,-41,-42,-37,40,]),'MINUS':([15,17,20,21,49,50,51,58,61,64,65,66,82,],[-45,41,-43,-44,41,-45,41,-45,41,-40,-41,-42,41,]),'MUL':([15,17,20,21,49,50,51,58,61,64,65,66,82,],[-45,42,-43,-44,42,-45,42,-45,42,-40,-41,-42,42,]),'DIV':([15,17,20,21,49,50,51,58,61,64,65,66,82,],[-45,43,-43,-44,43,-45,43,-45,43,-40,-41,-42,43,]),'RSB':([20,21,37,48,49,50,51,56,60,61,62,63,64,65,66,75,76,77,78,82,89,],[-43,-44,-50,70,-30,-45,-29,71,73,-19,-20,-50,-40,-41,-42,-23,83,-24,85,-18,-22,]),'COMMA':([20,21,37,50,60,61,62,63,64,65,66,75,76,77,82,89,],[-43,-44,-50,-45,74,-19,-20,-50,-40,-41,-42,-23,84,-24,-18,-22,]),'LMB':([24,70,71,83,85,],[47,80,81,88,90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'root':([0,47,80,81,88,90,],[2,69,86,87,93,94,]),'statement':([0,2,47,69,80,81,86,87,88,90,93,94,],[3,23,3,23,3,3,23,23,3,3,23,23,]),'if_statement':([0,2,47,69,80,81,86,87,88,90,93,94,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'while_statement':([0,2,47,69,80,81,86,87,88,90,93,94,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'variable_declaration':([0,2,47,69,80,81,86,87,88,90,93,94,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'variable_value_change':([0,2,47,69,80,81,86,87,88,90,93,94,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'function_declaration':([0,2,47,69,80,81,86,87,88,90,93,94,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'empty':([0,2,37,47,63,69,80,81,86,87,88,90,93,94,],[9,9,62,9,77,9,9,9,9,9,9,9,9,9,]),'expression':([0,2,36,47,57,69,80,81,86,87,88,90,93,94,],[10,10,59,10,72,10,10,10,10,10,10,10,10,10,]),'compare_expression':([0,2,28,34,36,47,57,68,69,80,81,86,87,88,90,93,94,],[12,12,48,56,12,12,12,78,12,12,12,12,12,12,12,12,12,]),'calculate':([0,2,28,29,34,36,37,47,57,68,69,74,80,81,86,87,88,90,93,94,],[17,17,49,51,49,17,61,17,17,49,17,82,17,17,17,17,17,17,17,17,]),'string_calculate':([0,2,36,47,57,69,80,81,86,87,88,90,93,94,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'function_call':([0,2,36,47,57,69,80,81,86,87,88,90,93,94,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'compare_operator':([12,48,56,78,],[29,29,29,29,]),'baseoperator':([17,49,51,61,82,],[39,39,39,39,39,]),'stringoperator':([18,],[44,]),'function_call_parameter':([37,],[60,]),'function_parameter':([63,],[76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> root','program',1,'p_program','main.py',1137),
  ('root -> root statement','root',2,'p_root','main.py',1145),
  ('root -> statement','root',1,'p_root','main.py',1146),
  ('statement -> if_statement','statement',1,'p_statement','main.py',1158),
  ('statement -> while_statement','statement',1,'p_statement','main.py',1159),
  ('statement -> variable_declaration SEMI','statement',2,'p_statement','main.py',1160),
  ('statement -> variable_value_change SEMI','statement',2,'p_statement','main.py',1161),
  ('statement -> function_declaration','statement',1,'p_statement','main.py',1162),
  ('statement -> empty','statement',1,'p_statement','main.py',1163),
  ('statement -> expression SEMI','statement',2,'p_statement_calculate','main.py',1168),
  ('expression -> calculate','expression',1,'p_expression','main.py',1175),
  ('expression -> string_calculate','expression',1,'p_expression','main.py',1176),
  ('expression -> compare_expression','expression',1,'p_expression','main.py',1177),
  ('expression -> function_call','expression',1,'p_expression','main.py',1178),
  ('variable_declaration -> VAR IDENTIFIER EQUAL expression','variable_declaration',4,'p_variable_declaration','main.py',1187),
  ('variable_value_change -> IDENTIFIER EQUAL expression','variable_value_change',3,'p_variable_value_change','main.py',1193),
  ('function_call -> IDENTIFIER LSB function_call_parameter RSB','function_call',4,'p_function_call','main.py',1200),
  ('function_call_parameter -> function_call_parameter COMMA calculate','function_call_parameter',3,'p_function_call_parameter','main.py',1205),
  ('function_call_parameter -> calculate','function_call_parameter',1,'p_function_call_parameter','main.py',1206),
  ('function_call_parameter -> empty','function_call_parameter',1,'p_function_call_parameter','main.py',1207),
  ('function_declaration -> FUNCTION IDENTIFIER LSB function_parameter RSB LMB root RMB','function_declaration',8,'p_function_declaration','main.py',1212),
  ('function_parameter -> function_parameter COMMA IDENTIFIER','function_parameter',3,'p_function_parameter','main.py',1217),
  ('function_parameter -> IDENTIFIER','function_parameter',1,'p_function_parameter','main.py',1218),
  ('function_parameter -> empty','function_parameter',1,'p_function_parameter','main.py',1219),
  ('while_statement -> WHILE LSB compare_expression RSB LMB root RMB','while_statement',7,'p_while_statement','main.py',1226),
  ('if_statement -> IF LSB compare_expression RSB LMB root RMB','if_statement',7,'p_if_statement','main.py',1233),
  ('if_statement -> if_statement ELSE IF LSB compare_expression RSB LMB root RMB','if_statement',9,'p_if_statement','main.py',1234),
  ('if_statement -> if_statement ELSE LMB root RMB','if_statement',5,'p_if_statement','main.py',1235),
  ('compare_expression -> compare_expression compare_operator calculate','compare_expression',3,'p_compare_expression','main.py',1244),
  ('compare_expression -> calculate','compare_expression',1,'p_compare_expression','main.py',1245),
  ('compare_operator -> LB','compare_operator',1,'p_compare_operator','main.py',1251),
  ('compare_operator -> RB','compare_operator',1,'p_compare_operator','main.py',1252),
  ('compare_operator -> LB EQUAL','compare_operator',2,'p_compare_operator','main.py',1253),
  ('compare_operator -> RB EQUAL','compare_operator',2,'p_compare_operator','main.py',1254),
  ('compare_operator -> EQUAL EQUAL','compare_operator',2,'p_compare_operator','main.py',1255),
  ('compare_operator -> NOTEQUAL EQUAL','compare_operator',2,'p_compare_operator','main.py',1256),
  ('string_calculate -> string_calculate stringoperator STRING','string_calculate',3,'p_string_calculate','main.py',1264),
  ('string_calculate -> STRING','string_calculate',1,'p_string_calculate','main.py',1265),
  ('stringoperator -> PLUS','stringoperator',1,'p_stringOperator','main.py',1271),
  ('calculate -> calculate baseoperator INT','calculate',3,'p_calculate','main.py',1277),
  ('calculate -> calculate baseoperator FLOAT','calculate',3,'p_calculate','main.py',1278),
  ('calculate -> calculate baseoperator IDENTIFIER','calculate',3,'p_calculate_identifier','main.py',1284),
  ('calculate -> INT','calculate',1,'p_calculate_type_int','main.py',1289),
  ('calculate -> FLOAT','calculate',1,'p_calculate_type_float','main.py',1293),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate_type_identifier','main.py',1298),
  ('baseoperator -> PLUS','baseoperator',1,'p_baseOperator','main.py',1304),
  ('baseoperator -> MINUS','baseoperator',1,'p_baseOperator','main.py',1305),
  ('baseoperator -> MUL','baseoperator',1,'p_baseOperator','main.py',1306),
  ('baseoperator -> DIV','baseoperator',1,'p_baseOperator','main.py',1307),
  ('empty -> <empty>','empty',0,'p_empty','main.py',1314),
]
