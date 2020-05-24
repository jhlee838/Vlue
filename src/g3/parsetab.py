
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCATCH CLASS COLON COMMA DEBUG DIV ELSE EQUAL FLOAT FOR FUNCTION GLOBAL IDENTIFIER IF IN INT LB LIST LMB LSB MINUS MUL PLUS PYTHON RB REPEAT RMB RSB SEMI STRING TRY USE VAR WHILE\n    root : expression\n    \n    expression : expression variable_declaration SEMI\n        | expression variable_value_change SEMI\n    \n    expression : expression if_statement\n    \n    expression : expression function\n        | expression function_call SEMI\n    \n    expression : expression repeat\n    \n    expression : expression for\n    \n    expression : expression while\n    \n    expression : expression use SEMI\n    \n    expression : expression error_handling\n    \n    expression : expression variable_alone SEMI\n    \n    expression : expression global_variable SEMI\n    \n    expression : expression class_def\n    \n    expression : expression debug SEMI\n    \n    expression : variable_declaration SEMI\n        | variable_value_change SEMI\n    \n    expression : if_statement\n    \n    expression : function\n        | function_call\n    \n    expression : repeat\n    \n    expression : for\n    \n    expression : while\n    \n    expression : use SEMI\n    \n    expression : error_handling\n    \n    expression : variable_alone SEMI\n    \n    expression : global_variable SEMI\n    \n    expression : class_def\n    \n    expression : debug SEMI\n    \n    expression : empty\n    \n    error_handling : try catch\n    \n    try : TRY LMB expression RMB\n    \n    catch : CATCH LSB IDENTIFIER RSB LMB expression RMB\n    \n    for : for_head for_body\n    \n    for_head : FOR LSB IDENTIFIER IN IDENTIFIER RSB\n    \n    for_body : LMB expression RMB\n    \n    while : while_head while_body\n    \n    while_head : WHILE LSB condition RSB\n    \n    while_body : LMB expression RMB\n    \n    repeat : repeat_head repeat_body\n    \n    repeat_head : REPEAT LSB calculate RSB\n    \n    repeat_body : LMB expression RMB\n    \n    function_class : IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB\n    \n    class_def : CLASS IDENTIFIER LMB expression RMB\n    \n    function : function_head function_body\n    \n    function_head : FUNCTION IDENTIFIER LSB parameter RSB\n        | FUNCTION IDENTIFIER LSB empty RSB\n    \n    function_body : LMB expression RMB\n    \n    function_call : IDENTIFIER LSB parameter RSB\n        | IDENTIFIER LSB empty RSB\n    \n    parameter : parameter COMMA calculate\n    \n    parameter : calculate\n    \n    debug : USE DEBUG\n    \n    if_statement : if_statement_1 if_statement_2 if_statement_3\n        | if_statement_1 if_statement_2\n        | if_statement_1 if_statement_3\n        | if_statement_1\n    \n    if_statement_1 : IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_2 : if_statement_2 ELSE IF LSB condition RSB LMB expression RMB\n    \n    if_statement_3 : ELSE LMB expression RMB\n    \n    condition : condition LB calculate\n        | condition RB calculate\n    \n    condition : condition LB EQUAL calculate\n        | condition RB EQUAL calculate\n    \n    condition : condition EQUAL calculate\n    \n    condition : calculate\n    \n    library : identifier PYTHON\n    \n    library : library identifier PYTHON\n    \n    identifier : identifier IDENTIFIER\n    \n    identifier : IDENTIFIER\n    \n    use : USE use_params\n    \n    use_params : IDENTIFIER\n    \n    global_variable : GLOBAL IDENTIFIER\n    \n    variable_alone : IDENTIFIER\n    \n    variable_value_change : IDENTIFIER EQUAL LIST\n    \n    variable_value_change : IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER LIST EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER EQUAL calculate\n    \n    variable_declaration : VAR IDENTIFIER\n    calculate : calculate PLUS calculatecalculate : calculate MINUS calculatecalculate : MINUS calculate %prec UMINUS\n    calculate : calculate MUL calculate\n        | calculate DIV calculate\n    \n    calculate : INT\n        | FLOAT\n        | STRING\n    \n    calculate : IDENTIFIER\n    \n    calculate : IDENTIFIER LIST\n    \n    calculate : LIST\n    calculate : LSB calculate RSBempty : '
    
_lr_action_items = {'VAR':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[18,18,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,18,-40,18,-34,18,-37,18,-31,18,-2,-3,-6,-10,-12,-13,-15,-54,18,18,18,18,18,18,18,-49,-50,18,-48,-42,-36,-39,18,-61,-44,18,18,18,18,18,-58,18,18,-33,18,-59,-60,]),'IDENTIFIER':([0,2,5,6,7,8,9,10,12,15,17,18,20,25,27,28,30,37,38,40,41,42,44,47,49,50,51,52,53,54,56,57,58,59,61,62,63,64,65,66,67,68,72,76,78,79,80,81,82,83,84,85,86,87,88,90,94,98,103,106,107,108,109,110,111,112,115,119,120,123,124,125,126,129,130,131,133,134,135,136,137,138,140,142,143,144,148,158,160,162,163,165,167,174,175,180,181,182,183,184,185,186,187,188,],[19,19,-18,-19,-20,-21,-22,-23,-25,-28,-30,55,-57,71,74,75,77,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,91,91,-55,-56,-45,19,-40,19,-34,19,-37,19,-31,91,91,117,91,19,-2,-3,-6,-10,-12,-13,-15,91,91,91,-54,19,19,19,19,19,139,19,91,19,91,91,91,91,91,-49,91,-50,91,19,-48,-42,-36,-39,19,91,91,91,171,91,-61,-44,19,91,91,19,19,19,19,-58,19,19,-33,19,-59,-60,]),'USE':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[25,25,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,25,-40,25,-34,25,-37,25,-31,25,-2,-3,-6,-10,-12,-13,-15,-54,25,25,25,25,25,25,25,-49,-50,25,-48,-42,-36,-39,25,-61,-44,25,25,25,25,25,-58,25,25,-33,25,-59,-60,]),'GLOBAL':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[27,27,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,27,-40,27,-34,27,-37,27,-31,27,-2,-3,-6,-10,-12,-13,-15,-54,27,27,27,27,27,27,27,-49,-50,27,-48,-42,-36,-39,27,-61,-44,27,27,27,27,27,-58,27,27,-33,27,-59,-60,]),'CLASS':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[28,28,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,28,-40,28,-34,28,-37,28,-31,28,-2,-3,-6,-10,-12,-13,-15,-54,28,28,28,28,28,28,28,-49,-50,28,-48,-42,-36,-39,28,-61,-44,28,28,28,28,28,-58,28,28,-33,28,-59,-60,]),'IF':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,60,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,104,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[29,29,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,105,-45,29,-40,29,-34,29,-37,29,-31,29,-2,-3,-6,-10,-12,-13,-15,-54,132,29,29,29,29,29,29,29,-49,-50,29,-48,-42,-36,-39,29,-61,-44,29,29,29,29,29,-58,29,29,-33,29,-59,-60,]),'FUNCTION':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[30,30,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,30,-40,30,-34,30,-37,30,-31,30,-2,-3,-6,-10,-12,-13,-15,-54,30,30,30,30,30,30,30,-49,-50,30,-48,-42,-36,-39,30,-61,-44,30,30,30,30,30,-58,30,30,-33,30,-59,-60,]),'REPEAT':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[31,31,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,31,-40,31,-34,31,-37,31,-31,31,-2,-3,-6,-10,-12,-13,-15,-54,31,31,31,31,31,31,31,-49,-50,31,-48,-42,-36,-39,31,-61,-44,31,31,31,31,31,-58,31,31,-33,31,-59,-60,]),'FOR':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[32,32,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,32,-40,32,-34,32,-37,32,-31,32,-2,-3,-6,-10,-12,-13,-15,-54,32,32,32,32,32,32,32,-49,-50,32,-48,-42,-36,-39,32,-61,-44,32,32,32,32,32,-58,32,32,-33,32,-59,-60,]),'WHILE':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[33,33,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,33,-40,33,-34,33,-37,33,-31,33,-2,-3,-6,-10,-12,-13,-15,-54,33,33,33,33,33,33,33,-49,-50,33,-48,-42,-36,-39,33,-61,-44,33,33,33,33,33,-58,33,33,-33,33,-59,-60,]),'TRY':([0,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[34,34,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,34,-40,34,-34,34,-37,34,-31,34,-2,-3,-6,-10,-12,-13,-15,-54,34,34,34,34,34,34,34,-49,-50,34,-48,-42,-36,-39,34,-61,-44,34,34,34,34,34,-58,34,34,-33,34,-59,-60,]),'$end':([0,1,2,5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,63,65,67,72,82,83,84,85,86,87,88,103,129,131,135,136,137,138,160,162,182,185,187,188,],[-93,0,-1,-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,-40,-34,-37,-31,-2,-3,-6,-10,-12,-13,-15,-54,-49,-50,-48,-42,-36,-39,-61,-44,-58,-33,-59,-60,]),'SEMI':([3,4,11,13,14,16,19,35,36,39,43,45,46,48,55,69,70,71,74,91,92,93,95,96,97,102,121,122,127,129,131,151,152,153,154,155,156,],[49,50,51,52,53,54,-75,82,83,84,85,86,87,88,-80,-72,-53,-73,-74,-89,-76,-77,-86,-87,-88,-91,-79,-90,-83,-49,-50,-78,-81,-82,-84,-85,-92,]),'RMB':([5,6,7,8,9,10,12,15,17,20,37,38,40,41,42,44,47,49,50,51,52,53,54,58,59,61,62,63,64,65,66,67,68,72,81,82,83,84,85,86,87,88,103,106,107,108,109,110,112,119,129,131,134,135,136,137,138,140,160,162,163,174,175,180,181,182,183,184,185,186,187,188,],[-18,-19,-20,-21,-22,-23,-25,-28,-30,-57,-4,-5,-7,-8,-9,-11,-14,-16,-17,-24,-26,-27,-29,-55,-56,-45,-93,-40,-93,-34,-93,-37,-93,-31,-93,-2,-3,-6,-10,-12,-13,-15,-54,-93,135,136,137,138,-93,150,-49,-50,160,-48,-42,-36,-39,162,-61,-44,-93,-93,182,-93,185,-58,-93,187,-33,188,-59,-60,]),'EQUAL':([19,55,89,91,95,96,97,102,113,114,118,122,127,142,143,152,153,154,155,156,159,164,166,168,172,176,177,],[56,90,120,-89,-86,-87,-88,-91,144,-67,144,-90,-83,165,167,-81,-82,-84,-85,-92,144,-62,-63,-66,144,-64,-65,]),'LSB':([19,29,31,32,33,56,57,73,76,77,78,80,90,94,98,105,115,120,123,124,125,126,130,132,133,142,143,144,158,165,167,],[57,76,78,79,80,98,98,111,98,115,98,98,98,98,98,133,98,98,98,98,98,98,98,158,98,98,98,98,98,98,98,]),'ELSE':([20,58,182,187,188,],[60,104,-58,-59,-60,]),'LMB':([21,22,23,24,34,60,75,104,141,147,149,161,169,170,173,178,179,],[62,64,66,68,81,106,112,106,163,-41,-38,174,-46,-47,180,-35,183,]),'DEBUG':([25,],[70,]),'CATCH':([26,150,],[73,-32,]),'LIST':([55,56,57,76,78,80,90,91,94,98,115,120,123,124,125,126,130,133,142,143,144,158,165,167,],[89,92,102,102,102,102,102,122,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'MINUS':([56,57,76,78,80,90,91,92,93,94,95,96,97,98,101,102,114,115,116,120,121,122,123,124,125,126,127,128,130,133,142,143,144,151,152,153,154,155,156,157,158,164,165,166,167,168,176,177,],[94,94,94,94,94,94,-89,-91,124,94,-86,-87,-88,94,124,-91,124,94,124,94,124,-90,94,94,94,94,-83,124,94,94,94,94,94,124,-81,-82,-84,-85,-92,124,94,124,94,124,94,124,124,124,]),'INT':([56,57,76,78,80,90,94,98,115,120,123,124,125,126,130,133,142,143,144,158,165,167,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'FLOAT':([56,57,76,78,80,90,94,98,115,120,123,124,125,126,130,133,142,143,144,158,165,167,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'STRING':([56,57,76,78,80,90,94,98,115,120,123,124,125,126,130,133,142,143,144,158,165,167,],[97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,]),'RSB':([57,91,95,96,97,99,100,101,102,113,114,115,116,118,122,127,128,139,145,146,152,153,154,155,156,157,159,164,166,168,171,172,176,177,],[-93,-89,-86,-87,-88,129,131,-52,-91,141,-67,-93,147,149,-90,-83,156,161,169,170,-81,-82,-84,-85,-92,-51,173,-62,-63,-66,178,179,-64,-65,]),'PLUS':([91,92,93,95,96,97,101,102,114,116,121,122,127,128,151,152,153,154,155,156,157,164,166,168,176,177,],[-89,-91,123,-86,-87,-88,123,-91,123,123,123,-90,-83,123,123,-81,-82,-84,-85,-92,123,123,123,123,123,123,]),'MUL':([91,92,93,95,96,97,101,102,114,116,121,122,127,128,151,152,153,154,155,156,157,164,166,168,176,177,],[-89,-91,125,-86,-87,-88,125,-91,125,125,125,-90,-83,125,125,125,125,-84,-85,-92,125,125,125,125,125,125,]),'DIV':([91,92,93,95,96,97,101,102,114,116,121,122,127,128,151,152,153,154,155,156,157,164,166,168,176,177,],[-89,-91,126,-86,-87,-88,126,-91,126,126,126,-90,-83,126,126,126,126,-84,-85,-92,126,126,126,126,126,126,]),'COMMA':([91,95,96,97,99,101,102,122,127,145,152,153,154,155,156,157,],[-89,-86,-87,-88,130,-52,-91,-90,-83,130,-81,-82,-84,-85,-92,-51,]),'LB':([91,95,96,97,102,113,114,118,122,127,152,153,154,155,156,159,164,166,168,172,176,177,],[-89,-86,-87,-88,-91,142,-67,142,-90,-83,-81,-82,-84,-85,-92,142,-62,-63,-66,142,-64,-65,]),'RB':([91,95,96,97,102,113,114,118,122,127,152,153,154,155,156,159,164,166,168,172,176,177,],[-89,-86,-87,-88,-91,143,-67,143,-90,-83,-81,-82,-84,-85,-92,143,-62,-63,-66,143,-64,-65,]),'IN':([117,],[148,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'expression':([0,62,64,66,68,81,106,112,163,174,180,183,],[2,107,108,109,110,119,134,140,175,181,184,186,]),'variable_declaration':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[3,35,3,3,3,3,3,3,35,35,35,35,3,35,35,35,3,3,35,3,35,3,35,35,]),'variable_value_change':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[4,36,4,4,4,4,4,4,36,36,36,36,4,36,36,36,4,4,36,4,36,4,36,36,]),'if_statement':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[5,37,5,5,5,5,5,5,37,37,37,37,5,37,37,37,5,5,37,5,37,5,37,37,]),'function':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[6,38,6,6,6,6,6,6,38,38,38,38,6,38,38,38,6,6,38,6,38,6,38,38,]),'function_call':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[7,39,7,7,7,7,7,7,39,39,39,39,7,39,39,39,7,7,39,7,39,7,39,39,]),'repeat':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[8,40,8,8,8,8,8,8,40,40,40,40,8,40,40,40,8,8,40,8,40,8,40,40,]),'for':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[9,41,9,9,9,9,9,9,41,41,41,41,9,41,41,41,9,9,41,9,41,9,41,41,]),'while':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[10,42,10,10,10,10,10,10,42,42,42,42,10,42,42,42,10,10,42,10,42,10,42,42,]),'use':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[11,43,11,11,11,11,11,11,43,43,43,43,11,43,43,43,11,11,43,11,43,11,43,43,]),'error_handling':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[12,44,12,12,12,12,12,12,44,44,44,44,12,44,44,44,12,12,44,12,44,12,44,44,]),'variable_alone':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[13,45,13,13,13,13,13,13,45,45,45,45,13,45,45,45,13,13,45,13,45,13,45,45,]),'global_variable':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[14,46,14,14,14,14,14,14,46,46,46,46,14,46,46,46,14,14,46,14,46,14,46,46,]),'class_def':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[15,47,15,15,15,15,15,15,47,47,47,47,15,47,47,47,15,15,47,15,47,15,47,47,]),'debug':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[16,48,16,16,16,16,16,16,48,48,48,48,16,48,48,48,16,16,48,16,48,16,48,48,]),'empty':([0,57,62,64,66,68,81,106,112,115,163,174,180,183,],[17,100,17,17,17,17,17,17,17,146,17,17,17,17,]),'if_statement_1':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'function_head':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'repeat_head':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'for_head':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'while_head':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'try':([0,2,62,64,66,68,81,106,107,108,109,110,112,119,134,140,163,174,175,180,181,183,184,186,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'if_statement_2':([20,],[58,]),'if_statement_3':([20,58,],[59,103,]),'function_body':([21,],[61,]),'repeat_body':([22,],[63,]),'for_body':([23,],[65,]),'while_body':([24,],[67,]),'use_params':([25,],[69,]),'catch':([26,],[72,]),'calculate':([56,57,76,78,80,90,94,98,115,120,123,124,125,126,130,133,142,143,144,158,165,167,],[93,101,114,116,114,121,127,128,101,151,152,153,154,155,157,114,164,166,168,114,176,177,]),'parameter':([57,115,],[99,145,]),'condition':([76,80,133,158,],[113,118,159,172,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','main.py',152),
  ('expression -> expression variable_declaration SEMI','expression',3,'p_expression_variable','main.py',166),
  ('expression -> expression variable_value_change SEMI','expression',3,'p_expression_variable','main.py',167),
  ('expression -> expression if_statement','expression',2,'p_expression_if_statement','main.py',184),
  ('expression -> expression function','expression',2,'p_expression_function','main.py',195),
  ('expression -> expression function_call SEMI','expression',3,'p_expression_function','main.py',196),
  ('expression -> expression repeat','expression',2,'p_expression_repeat','main.py',202),
  ('expression -> expression for','expression',2,'p_expression_for','main.py',208),
  ('expression -> expression while','expression',2,'p_expression_while','main.py',214),
  ('expression -> expression use SEMI','expression',3,'p_expression_use','main.py',220),
  ('expression -> expression error_handling','expression',2,'p_expression_error_handling','main.py',226),
  ('expression -> expression variable_alone SEMI','expression',3,'p_expression_variable_alone','main.py',232),
  ('expression -> expression global_variable SEMI','expression',3,'p_expression_global_variable','main.py',238),
  ('expression -> expression class_def','expression',2,'p_expression_class_def','main.py',244),
  ('expression -> expression debug SEMI','expression',3,'p_expression_debug','main.py',250),
  ('expression -> variable_declaration SEMI','expression',2,'p_expression_variable_2','main.py',258),
  ('expression -> variable_value_change SEMI','expression',2,'p_expression_variable_2','main.py',259),
  ('expression -> if_statement','expression',1,'p_expression_if_statement_2','main.py',270),
  ('expression -> function','expression',1,'p_expression_function_2','main.py',278),
  ('expression -> function_call','expression',1,'p_expression_function_2','main.py',279),
  ('expression -> repeat','expression',1,'p_expression_repeat_2','main.py',285),
  ('expression -> for','expression',1,'p_expression_for_2','main.py',291),
  ('expression -> while','expression',1,'p_expression_while_2','main.py',297),
  ('expression -> use SEMI','expression',2,'p_expression_use_2','main.py',303),
  ('expression -> error_handling','expression',1,'p_expression_error_handling_2','main.py',309),
  ('expression -> variable_alone SEMI','expression',2,'p_expression_variable_alone_2','main.py',315),
  ('expression -> global_variable SEMI','expression',2,'p_expression_global_variable_2','main.py',321),
  ('expression -> class_def','expression',1,'p_expression_class_def_2','main.py',327),
  ('expression -> debug SEMI','expression',2,'p_expression_debug_2','main.py',333),
  ('expression -> empty','expression',1,'p_expression_empty','main.py',341),
  ('error_handling -> try catch','error_handling',2,'p_error_handling','main.py',350),
  ('try -> TRY LMB expression RMB','try',4,'p_try','main.py',356),
  ('catch -> CATCH LSB IDENTIFIER RSB LMB expression RMB','catch',7,'p_catch','main.py',367),
  ('for -> for_head for_body','for',2,'p_for','main.py',380),
  ('for_head -> FOR LSB IDENTIFIER IN IDENTIFIER RSB','for_head',6,'p_for_head','main.py',388),
  ('for_body -> LMB expression RMB','for_body',3,'p_for_body','main.py',394),
  ('while -> while_head while_body','while',2,'p_while','main.py',405),
  ('while_head -> WHILE LSB condition RSB','while_head',4,'p_while_head','main.py',413),
  ('while_body -> LMB expression RMB','while_body',3,'p_while_body','main.py',419),
  ('repeat -> repeat_head repeat_body','repeat',2,'p_repeat','main.py',431),
  ('repeat_head -> REPEAT LSB calculate RSB','repeat_head',4,'p_repeat_head','main.py',439),
  ('repeat_body -> LMB expression RMB','repeat_body',3,'p_repeat_body','main.py',445),
  ('function_class -> IDENTIFIER EQUAL IDENTIFIER LSB parameter RSB','function_class',6,'p_function_class','main.py',456),
  ('class_def -> CLASS IDENTIFIER LMB expression RMB','class_def',5,'p_class_def','main.py',464),
  ('function -> function_head function_body','function',2,'p_function','main.py',479),
  ('function_head -> FUNCTION IDENTIFIER LSB parameter RSB','function_head',5,'p_function_head','main.py',487),
  ('function_head -> FUNCTION IDENTIFIER LSB empty RSB','function_head',5,'p_function_head','main.py',488),
  ('function_body -> LMB expression RMB','function_body',3,'p_function_body','main.py',497),
  ('function_call -> IDENTIFIER LSB parameter RSB','function_call',4,'p_function_call','main.py',508),
  ('function_call -> IDENTIFIER LSB empty RSB','function_call',4,'p_function_call','main.py',509),
  ('parameter -> parameter COMMA calculate','parameter',3,'p_parameter','main.py',520),
  ('parameter -> calculate','parameter',1,'p_parameter_2','main.py',526),
  ('debug -> USE DEBUG','debug',2,'p_debug','main.py',538),
  ('if_statement -> if_statement_1 if_statement_2 if_statement_3','if_statement',3,'p_if_statement','main.py',548),
  ('if_statement -> if_statement_1 if_statement_2','if_statement',2,'p_if_statement','main.py',549),
  ('if_statement -> if_statement_1 if_statement_3','if_statement',2,'p_if_statement','main.py',550),
  ('if_statement -> if_statement_1','if_statement',1,'p_if_statement','main.py',551),
  ('if_statement_1 -> IF LSB condition RSB LMB expression RMB','if_statement_1',7,'p_if_statement_1','main.py',563),
  ('if_statement_2 -> ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',8,'p_if_statement_2','main.py',572),
  ('if_statement_2 -> if_statement_2 ELSE IF LSB condition RSB LMB expression RMB','if_statement_2',9,'p_if_statement_2_2','main.py',583),
  ('if_statement_3 -> ELSE LMB expression RMB','if_statement_3',4,'p_if_statement_3','main.py',594),
  ('condition -> condition LB calculate','condition',3,'p_condition','main.py',607),
  ('condition -> condition RB calculate','condition',3,'p_condition','main.py',608),
  ('condition -> condition LB EQUAL calculate','condition',4,'p_condition_2','main.py',614),
  ('condition -> condition RB EQUAL calculate','condition',4,'p_condition_2','main.py',615),
  ('condition -> condition EQUAL calculate','condition',3,'p_condition_3','main.py',621),
  ('condition -> calculate','condition',1,'p_condition_4','main.py',627),
  ('library -> identifier PYTHON','library',2,'p_library','main.py',635),
  ('library -> library identifier PYTHON','library',3,'p_library_2','main.py',640),
  ('identifier -> identifier IDENTIFIER','identifier',2,'p_identifier','main.py',647),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier_2','main.py',653),
  ('use -> USE use_params','use',2,'p_use','main.py',661),
  ('use_params -> IDENTIFIER','use_params',1,'p_use_params','main.py',682),
  ('global_variable -> GLOBAL IDENTIFIER','global_variable',2,'p_global_variable','main.py',689),
  ('variable_alone -> IDENTIFIER','variable_alone',1,'p_variable_alone','main.py',697),
  ('variable_value_change -> IDENTIFIER EQUAL LIST','variable_value_change',3,'p_variable_value_change_list','main.py',705),
  ('variable_value_change -> IDENTIFIER EQUAL calculate','variable_value_change',3,'p_variable_value_change','main.py',711),
  ('variable_declaration -> VAR IDENTIFIER LIST EQUAL calculate','variable_declaration',5,'p_variable_declaration_list','main.py',739),
  ('variable_declaration -> VAR IDENTIFIER EQUAL calculate','variable_declaration',4,'p_variable_declaration_2','main.py',745),
  ('variable_declaration -> VAR IDENTIFIER','variable_declaration',2,'p_variable_declaration_1','main.py',761),
  ('calculate -> calculate PLUS calculate','calculate',3,'p_add','main.py',790),
  ('calculate -> calculate MINUS calculate','calculate',3,'p_sub','main.py',826),
  ('calculate -> MINUS calculate','calculate',2,'p_calculate2uminus','main.py',830),
  ('calculate -> calculate MUL calculate','calculate',3,'p_mul_div','main.py',835),
  ('calculate -> calculate DIV calculate','calculate',3,'p_mul_div','main.py',836),
  ('calculate -> INT','calculate',1,'p_calculate2num','main.py',847),
  ('calculate -> FLOAT','calculate',1,'p_calculate2num','main.py',848),
  ('calculate -> STRING','calculate',1,'p_calculate2num','main.py',849),
  ('calculate -> IDENTIFIER','calculate',1,'p_calculate2str','main.py',855),
  ('calculate -> IDENTIFIER LIST','calculate',2,'p_calculate2list','main.py',864),
  ('calculate -> LIST','calculate',1,'p_calculate2list_2','main.py',870),
  ('calculate -> LSB calculate RSB','calculate',3,'p_parens','main.py',875),
  ('empty -> <empty>','empty',0,'p_empty','main.py',881),
]
