import re
def id_validator():
   return bool(re.match('^\d{6}$',id))
def state_validator(state):
    return bool(re.match('^\d{5}$', state))
def cancer_validator(cancer):
   return bool(re.match("^([0-9]{1,2})?$",cancer))
def chf_validator(chf):
    return bool(re.match("^([1]?[0-9]{1,2})?$", chf))
