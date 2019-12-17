import re
def id_validator():
    a = True
    while a:
        id = input('id pls: ')
        if bool(re.match('^\d{6}$',id)):
            a = False
            return id
        else:
            print('Данные введены неверно')
def state_validator():
    a = True
    while a:
        state = input('state pls: ')
        if bool(re.match('^\d{5}$',state)):
            a = False
            return state
        else:
            print('Данные введены неверно')
def cencer_validator():
    a = True
    while a:
        cancer = input('cancer pls: ')
        if bool(re.match("^([0-9]{1,2})?$",cancer)):
            a = False
            return cancer
        else:
            print('Двнные введены не верно')
def chf_validator():
    a = True
    while a:
        chf = input('chf pls: ')
        if bool(re.match("^([1]?[0-9]{1,2})?$",chf)):
            a = False
            return chf
        else:
            print('Данные введены неверно')