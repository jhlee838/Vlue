
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA EQUAL IDENTIFIER NEWLINE OTHER TABtest : NEWLINE IDENTIFIER NEWLINEempty : '
    
_lr_action_items = {'NEWLINE':([0,3,],[2,4,]),'$end':([1,4,],[0,-1,]),'IDENTIFIER':([2,],[3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'test':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> test","S'",1,None,None,None),
  ('test -> NEWLINE IDENTIFIER NEWLINE','test',3,'p_test','parser.py',7),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',12),
]
