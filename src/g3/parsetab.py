
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCOLON COMMA DIV ELSE EQUAL FLOAT FOR FUNCTION IDENTIFIER IF IN INT LB LIST LMB LSB MINUS MUL PLUS RB REPEAT RMB RSB SEMI STRING USE VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n        | expression function_call SEMI\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : expression while\n    \n    expression : expression use\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n        | function_call\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : while\n    \n    expression : use\n    \n    expression : empty\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    while : while_head while_body\n    \n    while_head : WHILE LSB condition RSB\n    \n    while_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB empty RSB\n        | FUNCTION IDENTIFIER LSB parameter RSB\n    \n    function_body : LMB expression RMB\n    \n    function_call : IDENTIFIER LSB parameter RSB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n        | empty\n    \n    if_statement : if_statement_1 if_statement_2 if_statement_3\n    \n    if_statement_1 : IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : ELSE IF LSB condition RSB LMB expression RMB\n        | empty\n    \n    if_statement_3 : ELSE LMB expression RMB\n        | empty\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    use : USE IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL LIST\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL LIST\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[13,13,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,13,-27,13,-21,13,-24,13,-50,-2,-3,-6,-38,-43,13,13,13,13,-34,13,-33,-29,-23,-26,13,13,-42,13,13,-39,13,-40,]),'IDENTIFIER':([0,2,5,6,7,8,9,10,11,12,13,15,20,22,28,29,31,32,33,34,35,36,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,64,68,72,74,76,77,78,79,82,88,89,90,91,94,95,96,97,98,99,100,101,103,104,105,109,117,119,121,123,128,130,134,135,136,137,],[14,14,-13,-14,-15,-16,-17,-18,-19,-20,37,-66,51,53,-4,-5,-7,-8,-9,-10,-11,-12,61,61,-66,-41,-30,14,-27,14,-21,14,-24,14,-50,61,61,84,61,-2,-3,-6,61,61,61,-38,-43,14,14,14,14,61,61,61,61,61,-34,61,14,61,-33,-29,-23,-26,61,61,61,127,14,14,61,61,-42,14,14,-39,14,-40,]),'USE':([0,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[20,20,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,20,-27,20,-21,20,-24,20,-50,-2,-3,-6,-38,-43,20,20,20,20,-34,20,-33,-29,-23,-26,20,20,-42,20,20,-39,20,-40,]),'IF':([0,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[21,21,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,75,-41,-30,21,-27,21,-21,21,-24,21,-50,-2,-3,-6,-38,-43,21,21,21,21,-34,21,-33,-29,-23,-26,21,21,-42,21,21,-39,21,-40,]),'FUNCTION':([0,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[22,22,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,22,-27,22,-21,22,-24,22,-50,-2,-3,-6,-38,-43,22,22,22,22,-34,22,-33,-29,-23,-26,22,22,-42,22,22,-39,22,-40,]),'REPEAT':([0,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[23,23,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,23,-27,23,-21,23,-24,23,-50,-2,-3,-6,-38,-43,23,23,23,23,-34,23,-33,-29,-23,-26,23,23,-42,23,23,-39,23,-40,]),'FOR':([0,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[24,24,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,24,-27,24,-21,24,-24,24,-50,-2,-3,-6,-38,-43,24,24,24,24,-34,24,-33,-29,-23,-26,24,24,-42,24,24,-39,24,-40,]),'WHILE':([0,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[25,25,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,25,-27,25,-21,25,-24,25,-50,-2,-3,-6,-38,-43,25,25,25,25,-34,25,-33,-29,-23,-26,25,25,-42,25,25,-39,25,-40,]),'$end':([0,1,2,5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,45,47,49,51,57,58,59,72,74,94,98,99,100,101,128,135,137,],[-66,0,-1,-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,-27,-21,-24,-50,-2,-3,-6,-38,-43,-34,-33,-29,-23,-26,-42,-39,-40,]),'SEMI':([3,4,26,27,30,37,61,62,63,65,66,67,86,87,92,94,111,112,113,114,115,],[35,36,57,58,59,-55,-64,-51,-52,-61,-62,-63,-53,-54,-58,-34,-56,-57,-59,-60,-65,]),'RMB':([5,6,7,8,9,10,11,12,15,28,29,31,32,33,34,35,36,40,42,43,44,45,46,47,48,49,50,51,57,58,59,72,74,76,77,78,79,94,96,98,99,100,101,117,119,128,130,134,135,136,137,],[-13,-14,-15,-16,-17,-18,-19,-20,-66,-4,-5,-7,-8,-9,-10,-11,-12,-66,-41,-30,-66,-27,-66,-21,-66,-24,-66,-50,-2,-3,-6,-38,-43,98,99,100,101,-34,-66,-33,-29,-23,-26,128,-66,-42,135,-66,-39,137,-40,]),'EQUAL':([14,37,61,65,66,67,80,81,85,92,103,104,111,112,113,114,115,118,120,122,124,131,132,],[38,60,-64,-61,-62,-63,105,-49,105,-58,121,123,-56,-57,-59,-60,-65,105,-44,-45,-48,-46,-47,]),'LSB':([14,21,23,24,25,38,39,52,53,54,56,60,64,68,75,82,88,89,90,91,95,97,103,104,105,121,123,],[39,52,54,55,56,68,68,68,82,68,68,68,68,68,97,68,68,68,68,68,68,68,68,68,68,68,68,]),'ELSE':([15,40,42,135,137,],[41,73,-41,-39,-40,]),'LMB':([16,17,18,19,73,102,108,110,125,126,129,133,],[44,46,48,50,96,119,-28,-25,-31,-32,134,-22,]),'LIST':([38,60,],[62,86,]),'MINUS':([38,39,52,54,56,60,61,63,64,65,66,67,68,70,81,82,83,87,88,89,90,91,92,93,95,97,103,104,105,111,112,113,114,115,116,120,121,122,123,124,131,132,],[64,64,64,64,64,64,-64,89,64,-61,-62,-63,64,89,89,64,89,89,64,64,64,64,-58,89,64,64,64,64,64,-56,-57,-59,-60,-65,89,89,64,89,64,89,89,89,]),'INT':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,103,104,105,121,123,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'FLOAT':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,103,104,105,121,123,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'STRING':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,103,104,105,121,123,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'RSB':([39,61,65,66,67,69,70,71,80,81,82,83,85,92,93,106,107,111,112,113,114,115,116,118,120,122,124,127,131,132,],[-66,-64,-61,-62,-63,94,-36,-37,102,-49,-66,108,110,-58,115,125,126,-56,-57,-59,-60,-65,-35,129,-44,-45,-48,133,-46,-47,]),'COMMA':([39,61,65,66,67,69,70,71,82,92,106,107,111,112,113,114,115,116,],[-66,-64,-61,-62,-63,95,-36,-37,-66,-58,-37,95,-56,-57,-59,-60,-65,-35,]),'PLUS':([61,63,65,66,67,70,81,83,87,92,93,111,112,113,114,115,116,120,122,124,131,132,],[-64,88,-61,-62,-63,88,88,88,88,-58,88,-56,-57,-59,-60,-65,88,88,88,88,88,88,]),'MUL':([61,63,65,66,67,70,81,83,87,92,93,111,112,113,114,115,116,120,122,124,131,132,],[-64,90,-61,-62,-63,90,90,90,90,-58,90,90,90,-59,-60,-65,90,90,90,90,90,90,]),'DIV':([61,63,65,66,67,70,81,83,87,92,93,111,112,113,114,115,116,120,122,124,131,132,],[-64,91,-61,-62,-63,91,91,91,91,-58,91,91,91,-59,-60,-65,91,91,91,91,91,91,]),'LB':([61,65,66,67,80,81,85,92,111,112,113,114,115,118,120,122,124,131,132,],[-64,-61,-62,-63,103,-49,103,-58,-56,-57,-59,-60,-65,103,-44,-45,-48,-46,-47,]),'RB':([61,65,66,67,80,81,85,92,111,112,113,114,115,118,120,122,124,131,132,],[-64,-61,-62,-63,104,-49,104,-58,-56,-57,-59,-60,-65,104,-44,-45,-48,-46,-47,]),'IN':([84,],[109,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,44,46,48,50,96,119,134,],[2,76,77,78,79,117,130,136,]),'variable_declaration':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[3,26,3,3,3,3,26,26,26,26,3,26,3,26,3,26,]),'variable_value_change':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[4,27,4,4,4,4,27,27,27,27,4,27,4,27,4,27,]),'if_statement':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[5,28,5,5,5,5,28,28,28,28,5,28,5,28,5,28,]),'function':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[6,29,6,6,6,6,29,29,29,29,6,29,6,29,6,29,]),'function_call':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[7,30,7,7,7,7,30,30,30,30,7,30,7,30,7,30,]),'repeat':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[8,31,8,8,8,8,31,31,31,31,8,31,8,31,8,31,]),'for':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[9,32,9,9,9,9,32,32,32,32,9,32,9,32,9,32,]),'while':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[10,33,10,10,10,10,33,33,33,33,10,33,10,33,10,33,]),'use':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[11,34,11,11,11,11,34,34,34,34,11,34,11,34,11,34,]),'empty':([0,15,39,40,44,46,48,50,82,96,119,134,],[12,42,71,74,12,12,12,12,106,12,12,12,]),'if_statement_1':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'function_head':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'repeat_head':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'for_head':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'while_head':([0,2,44,46,48,50,76,77,78,79,96,117,119,130,134,136,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'if_statement_2':([15,],[40,]),'function_body':([16,],[43,]),'repeat_body':([17,],[45,]),'for_body':([18,],[47,]),'while_body':([19,],[49,]),'calculate':([38,39,52,54,56,60,64,68,82,88,89,90,91,95,97,103,104,105,121,123,],[63,70,81,83,81,87,92,93,70,111,112,113,114,116,81,120,122,124,131,132,]),'parameter':([39,82,],[69,107,]),'if_statement_3':([40,],[72,]),'condition':([52,56,97,],[80,85,118,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',147),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',161),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',162),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',179),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',190),
  ('expression -> expression function_call SEMI','expression',3,'p_expression_function','main.py',191),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',197),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',203),
  ('expression -> expression while','expression',2,'p_expression_while','main.py',209),
  ('expression -> expression use','expression',2,'p_expression_use','main.py',215),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',223),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',224),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',235),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',243),
  ('expression -> function_call','expression',1,'p_expression_function_2','main.py',244),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',250),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',256),
  ('expression -> while','expression',1,'p_expression_while_2','main.py',262),
  ('expression -> use','expression',1,'p_expression_use_2','main.py',268),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',276),
  ('for -> for_head for_body','for',2,'p_for','main.py',285),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',293),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',299),
  ('while -> while_head while_body','while',2,'p_while','main.py',310),
  ('while_head -> WHILE LSB condition RSB','while_head',4,'p_while_head','main.py',318),
  ('while_body -> LMB expression RMB','while_body',3,'p_while_body','main.py',324),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',336),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',344),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',350),
  ('function -> function_head function_body','function',2,'p_function','main.py',363),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',371),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',372),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',381),
  ('function_call -> IDENTIFIER LSB parameter RSB','function_call',4,'p_function_call','main.py',392),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',400),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',406),
  ('parameter -> empty','parameter',1,'p_parameter_2','main.py',407),
  ('if_statement -> if_statement_1 if_statement_2 if_statement_3','if_statement',3,'p_if_statement','main.py',418),
  ('if_statement_1 -> IF LSB condition RSB LMB expression RMB','if_statement_1',7,'p_if_statement_1','main.py',425),
  ('if_statement_2 -> ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',8,'p_if_statement_2','main.py',432),
  ('if_statement_2 -> empty','if_statement_2',1,'p_if_statement_2','main.py',433),
  ('if_statement_3 -> ELSE LMB expression RMB','if_statement_3',4,'p_if_statement_3','main.py',440),
  ('if_statement_3 -> empty','if_statement_3',1,'p_if_statement_3','main.py',441),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',450),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',451),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',457),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',458),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',464),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',470),
  ('use -> USE IDENTIFIER','use',2,'p_use','main.py',480),
  ('variable_value_change -> IDENTIFIER EQUAL LIST','variable_value_change',3,'p_variable_value_change_list','main.py',497),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',503),
  ('variable_declaration -> VAR IDENTIFIER EQUAL LIST','variable_declaration',4,'p_variable_declaration_list','main.py',529),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',535),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',551),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',580),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',616),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',620),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',625),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',626),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',637),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',638),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',639),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',645),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',653),
  ('empty -> <empty>','empty',0,'p_empty','main.py',659),
]
