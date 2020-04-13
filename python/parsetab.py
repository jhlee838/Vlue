
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA CONTENTS EQUAL IDENTIFIER LMB LSB RMB RSB\n    elements_expr : LSB elements RSB\n    \n    elements : elements COMMA elements\n    \n    elements : IDENTIFIER EQUAL IDENTIFIER\n    '
    
_lr_action_items = {'LSB':([0,],[2,]),'$end':([1,5,],[0,-1,]),'IDENTIFIER':([2,6,7,],[4,4,9,]),'RSB':([3,8,9,],[5,-2,-3,]),'COMMA':([3,8,9,],[6,6,-3,]),'EQUAL':([4,],[7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'elements_expr':([0,],[1,]),'elements':([2,6,],[3,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> elements_expr","S'",1,None,None,None),
  ('elements_expr -> LSB elements RSB','elements_expr',3,'p_elements_expr','parser.py',8),
  ('elements -> elements COMMA elements','elements',3,'p_elements_2','parser.py',15),
  ('elements -> IDENTIFIER EQUAL IDENTIFIER','elements',3,'p_elements','parser.py',22),
]
