
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCOLON COMMA DIV ELSE EQUAL FLOAT FOR FUNCTION IDENTIFIER IF IN INT LB LIST LMB LSB MINUS MUL PLUS RB REPEAT RMB RSB SEMI STRING USE VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n        | expression function_call SEMI\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : expression while\n    \n    expression : expression use\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n        | function_call\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : while\n    \n    expression : use\n    \n    expression : empty\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    while : while_head while_body\n    \n    while_head : WHILE LSB condition RSB\n    \n    while_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB empty RSB\n        | FUNCTION IDENTIFIER LSB parameter RSB\n    \n    function_body : LMB expression RMB\n    \n    function_call : IDENTIFIER LSB parameter RSB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n        | empty\n    \n    if_statement : if_statement_head if_statement_body\n    \n    if_statement_head : IF LSB condition RSB\n    \n    if_statement_body : LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    use : USE IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL LIST\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL LIST\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[13,13,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,13,-30,13,-27,13,-21,13,-24,13,-47,-2,-3,-6,13,13,13,13,13,-34,-40,-33,-29,-23,-26,]),'IDENTIFIER':([0,2,5,6,7,8,9,10,11,12,13,20,22,28,29,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,63,67,71,72,73,74,75,78,84,85,86,87,90,91,92,93,94,95,96,98,99,100,104,113,115,],[14,14,-13,-14,-15,-16,-17,-18,-19,-20,37,50,52,-4,-5,-7,-8,-9,-10,-11,-12,60,60,-38,14,-30,14,-27,14,-21,14,-24,14,-47,60,60,80,60,-2,-3,-6,60,60,60,14,14,14,14,14,60,60,60,60,60,-34,60,-40,-33,-29,-23,-26,60,60,60,119,60,60,]),'USE':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[20,20,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,20,-30,20,-27,20,-21,20,-24,20,-47,-2,-3,-6,20,20,20,20,20,-34,-40,-33,-29,-23,-26,]),'IF':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[21,21,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,21,-30,21,-27,21,-21,21,-24,21,-47,-2,-3,-6,21,21,21,21,21,-34,-40,-33,-29,-23,-26,]),'FUNCTION':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[22,22,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,22,-30,22,-27,22,-21,22,-24,22,-47,-2,-3,-6,22,22,22,22,22,-34,-40,-33,-29,-23,-26,]),'REPEAT':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[23,23,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,23,-30,23,-27,23,-21,23,-24,23,-47,-2,-3,-6,23,23,23,23,23,-34,-40,-33,-29,-23,-26,]),'FOR':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[24,24,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,24,-30,24,-27,24,-21,24,-24,24,-47,-2,-3,-6,24,24,24,24,24,-34,-40,-33,-29,-23,-26,]),'WHILE':([0,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[25,25,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,25,-30,25,-27,25,-21,25,-24,25,-47,-2,-3,-6,25,25,25,25,25,-34,-40,-33,-29,-23,-26,]),'$end':([0,1,2,5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,42,44,46,48,50,56,57,58,90,92,93,94,95,96,],[-63,0,-1,-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,-30,-27,-21,-24,-47,-2,-3,-6,-34,-40,-33,-29,-23,-26,]),'SEMI':([3,4,26,27,30,37,60,61,62,64,65,66,82,83,88,90,106,107,108,109,110,],[35,36,56,57,58,-52,-61,-48,-49,-58,-59,-60,-50,-51,-55,-34,-53,-54,-56,-57,-62,]),'RMB':([5,6,7,8,9,10,11,12,28,29,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49,50,56,57,58,71,72,73,74,75,90,92,93,94,95,96,],[-13,-14,-15,-16,-17,-18,-19,-20,-4,-5,-7,-8,-9,-10,-11,-12,-38,-63,-30,-63,-27,-63,-21,-63,-24,-63,-47,-2,-3,-6,92,93,94,95,96,-34,-40,-33,-29,-23,-26,]),'EQUAL':([14,37,60,64,65,66,76,77,81,88,98,99,106,107,108,109,110,112,114,116,120,121,],[38,59,-61,-58,-59,-60,100,-46,100,-55,113,115,-53,-54,-56,-57,-62,-41,-42,-45,-43,-44,]),'LSB':([14,21,23,24,25,38,39,51,52,53,55,59,63,67,78,84,85,86,87,91,98,99,100,113,115,],[39,51,53,54,55,67,67,67,78,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'LMB':([15,16,17,18,19,97,103,105,117,118,122,],[41,43,45,47,49,-39,-28,-25,-31,-32,-22,]),'LIST':([38,59,],[61,82,]),'MINUS':([38,39,51,53,55,59,60,62,63,64,65,66,67,69,77,78,79,83,84,85,86,87,88,89,91,98,99,100,106,107,108,109,110,111,112,113,114,115,116,120,121,],[63,63,63,63,63,63,-61,85,63,-58,-59,-60,63,85,85,63,85,85,63,63,63,63,-55,85,63,63,63,63,-53,-54,-56,-57,-62,85,85,63,85,63,85,85,85,]),'INT':([38,39,51,53,55,59,63,67,78,84,85,86,87,91,98,99,100,113,115,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'FLOAT':([38,39,51,53,55,59,63,67,78,84,85,86,87,91,98,99,100,113,115,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'STRING':([38,39,51,53,55,59,63,67,78,84,85,86,87,91,98,99,100,113,115,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'RSB':([39,60,64,65,66,68,69,70,76,77,78,79,81,88,89,101,102,106,107,108,109,110,111,112,114,116,119,120,121,],[-63,-61,-58,-59,-60,90,-36,-37,97,-46,-63,103,105,-55,110,117,118,-53,-54,-56,-57,-62,-35,-41,-42,-45,122,-43,-44,]),'COMMA':([39,60,64,65,66,68,69,70,78,88,101,102,106,107,108,109,110,111,],[-63,-61,-58,-59,-60,91,-36,-37,-63,-55,-37,91,-53,-54,-56,-57,-62,-35,]),'PLUS':([60,62,64,65,66,69,77,79,83,88,89,106,107,108,109,110,111,112,114,116,120,121,],[-61,84,-58,-59,-60,84,84,84,84,-55,84,-53,-54,-56,-57,-62,84,84,84,84,84,84,]),'MUL':([60,62,64,65,66,69,77,79,83,88,89,106,107,108,109,110,111,112,114,116,120,121,],[-61,86,-58,-59,-60,86,86,86,86,-55,86,86,86,-56,-57,-62,86,86,86,86,86,86,]),'DIV':([60,62,64,65,66,69,77,79,83,88,89,106,107,108,109,110,111,112,114,116,120,121,],[-61,87,-58,-59,-60,87,87,87,87,-55,87,87,87,-56,-57,-62,87,87,87,87,87,87,]),'LB':([60,64,65,66,76,77,81,88,106,107,108,109,110,112,114,116,120,121,],[-61,-58,-59,-60,98,-46,98,-55,-53,-54,-56,-57,-62,-41,-42,-45,-43,-44,]),'RB':([60,64,65,66,76,77,81,88,106,107,108,109,110,112,114,116,120,121,],[-61,-58,-59,-60,99,-46,99,-55,-53,-54,-56,-57,-62,-41,-42,-45,-43,-44,]),'IN':([80,],[104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,41,43,45,47,49,],[2,71,72,73,74,75,]),'variable_declaration':([0,2,41,43,45,47,49,71,72,73,74,75,],[3,26,3,3,3,3,3,26,26,26,26,26,]),'variable_value_change':([0,2,41,43,45,47,49,71,72,73,74,75,],[4,27,4,4,4,4,4,27,27,27,27,27,]),'if_statement':([0,2,41,43,45,47,49,71,72,73,74,75,],[5,28,5,5,5,5,5,28,28,28,28,28,]),'function':([0,2,41,43,45,47,49,71,72,73,74,75,],[6,29,6,6,6,6,6,29,29,29,29,29,]),'function_call':([0,2,41,43,45,47,49,71,72,73,74,75,],[7,30,7,7,7,7,7,30,30,30,30,30,]),'repeat':([0,2,41,43,45,47,49,71,72,73,74,75,],[8,31,8,8,8,8,8,31,31,31,31,31,]),'for':([0,2,41,43,45,47,49,71,72,73,74,75,],[9,32,9,9,9,9,9,32,32,32,32,32,]),'while':([0,2,41,43,45,47,49,71,72,73,74,75,],[10,33,10,10,10,10,10,33,33,33,33,33,]),'use':([0,2,41,43,45,47,49,71,72,73,74,75,],[11,34,11,11,11,11,11,34,34,34,34,34,]),'empty':([0,39,41,43,45,47,49,78,],[12,70,12,12,12,12,12,101,]),'if_statement_head':([0,2,41,43,45,47,49,71,72,73,74,75,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'function_head':([0,2,41,43,45,47,49,71,72,73,74,75,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'repeat_head':([0,2,41,43,45,47,49,71,72,73,74,75,],[17,17,17,17,17,17,17,17,17,17,17,17,]),'for_head':([0,2,41,43,45,47,49,71,72,73,74,75,],[18,18,18,18,18,18,18,18,18,18,18,18,]),'while_head':([0,2,41,43,45,47,49,71,72,73,74,75,],[19,19,19,19,19,19,19,19,19,19,19,19,]),'if_statement_body':([15,],[40,]),'function_body':([16,],[42,]),'repeat_body':([17,],[44,]),'for_body':([18,],[46,]),'while_body':([19,],[48,]),'calculate':([38,39,51,53,55,59,63,67,78,84,85,86,87,91,98,99,100,113,115,],[62,69,77,79,77,83,88,89,69,106,107,108,109,111,112,114,116,120,121,]),'parameter':([39,78,],[68,102,]),'condition':([51,55,],[76,81,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',146),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',160),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',161),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',178),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',189),
  ('expression -> expression function_call SEMI','expression',3,'p_expression_function','main.py',190),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',196),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',202),
  ('expression -> expression while','expression',2,'p_expression_while','main.py',208),
  ('expression -> expression use','expression',2,'p_expression_use','main.py',214),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',222),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',223),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',234),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',242),
  ('expression -> function_call','expression',1,'p_expression_function_2','main.py',243),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',249),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',255),
  ('expression -> while','expression',1,'p_expression_while_2','main.py',261),
  ('expression -> use','expression',1,'p_expression_use_2','main.py',267),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',275),
  ('for -> for_head for_body','for',2,'p_for','main.py',284),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',292),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',298),
  ('while -> while_head while_body','while',2,'p_while','main.py',309),
  ('while_head -> WHILE LSB condition RSB','while_head',4,'p_while_head','main.py',317),
  ('while_body -> LMB expression RMB','while_body',3,'p_while_body','main.py',323),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',335),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',343),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',349),
  ('function -> function_head function_body','function',2,'p_function','main.py',362),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',370),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',371),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',380),
  ('function_call -> IDENTIFIER LSB parameter RSB','function_call',4,'p_function_call','main.py',391),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',399),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',405),
  ('parameter -> empty','parameter',1,'p_parameter_2','main.py',406),
  ('if_statement -> if_statement_head if_statement_body','if_statement',2,'p_if_statement','main.py',417),
  ('if_statement_head -> IF LSB condition RSB','if_statement_head',4,'p_if_statement_head','main.py',425),
  ('if_statement_body -> LMB expression RMB','if_statement_body',3,'p_if_statement_body','main.py',431),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',442),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',443),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',449),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',450),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',456),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',462),
  ('use -> USE IDENTIFIER','use',2,'p_use','main.py',472),
  ('variable_value_change -> IDENTIFIER EQUAL LIST','variable_value_change',3,'p_variable_value_change_list','main.py',488),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',494),
  ('variable_declaration -> VAR IDENTIFIER EQUAL LIST','variable_declaration',4,'p_variable_declaration_list','main.py',520),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',526),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',542),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',571),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',607),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',611),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',616),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',617),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',628),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',629),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',630),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',636),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',644),
  ('empty -> <empty>','empty',0,'p_empty','main.py',650),
]
