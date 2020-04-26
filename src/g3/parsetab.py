
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSDIV ELSE EQUAL IDENTIFIER IF INT LMB LSB MINUS MUL NEWLINE PLUS RMB RSB TAB VAR\n    expression : expression variable_declaration NEWLINE\n        | expression variable_value_change NEWLINE\n        | variable_declaration NEWLINE\n        | variable_value_change\n        | NEWLINE\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n    \n    calculate : IDENTIFIER\n    calculate : LSB calculate RSB'
    
_lr_action_items = {'NEWLINE':([0,2,7,8,10,15,16,18,20,25,27,28,29,30,31,],[3,9,12,13,-8,-15,-6,-14,-7,-11,-9,-10,-12,-13,-16,]),'VAR':([0,1,3,4,9,12,13,15,16,18,25,27,28,29,30,31,],[5,5,-5,-4,-3,-1,-2,-15,-6,-14,-11,-9,-10,-12,-13,-16,]),'IDENTIFIER':([0,1,3,4,5,9,11,12,13,14,15,16,17,18,19,21,22,23,24,25,27,28,29,30,31,],[6,6,-5,-4,10,-3,15,-1,-2,15,-15,-6,15,-14,15,15,15,15,15,-11,-9,-10,-12,-13,-16,]),'$end':([1,3,4,9,12,13,15,16,18,25,27,28,29,30,31,],[0,-5,-4,-3,-1,-2,-15,-6,-14,-11,-9,-10,-12,-13,-16,]),'EQUAL':([6,10,],[11,14,]),'MINUS':([11,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[17,17,-15,22,17,-14,17,22,17,17,17,17,-11,22,-9,-10,-12,-13,-16,]),'INT':([11,14,17,19,21,22,23,24,],[18,18,18,18,18,18,18,18,]),'LSB':([11,14,17,19,21,22,23,24,],[19,19,19,19,19,19,19,19,]),'PLUS':([15,16,18,20,25,26,27,28,29,30,31,],[-15,21,-14,21,-11,21,-9,-10,-12,-13,-16,]),'MUL':([15,16,18,20,25,26,27,28,29,30,31,],[-15,23,-14,23,-11,23,23,23,-12,-13,-16,]),'DIV':([15,16,18,20,25,26,27,28,29,30,31,],[-15,24,-14,24,-11,24,24,24,-12,-13,-16,]),'RSB':([15,18,25,26,27,28,29,30,31,],[-15,-14,-11,31,-9,-10,-12,-13,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'variable_declaration':([0,1,],[2,7,]),'variable_value_change':([0,1,],[4,8,]),'calculate':([11,14,17,19,21,22,23,24,],[16,20,25,26,27,28,29,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression variable_declaration NEWLINE','expression',3,'p_expression','main.py',97),
  ('expression -> expression variable_value_change NEWLINE','expression',3,'p_expression','main.py',98),
  ('expression -> variable_declaration NEWLINE','expression',2,'p_expression','main.py',99),
  ('expression -> variable_value_change','expression',1,'p_expression','main.py',100),
  ('expression -> NEWLINE','expression',1,'p_expression','main.py',101),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',108),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',117),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',124),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',131),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',135),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',139),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',144),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',145),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',156),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',162),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',170),
]
