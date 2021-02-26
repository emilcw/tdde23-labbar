from calc import *
from copy import deepcopy


def eval_program(p,opt={}):

    if isprogram(p):
        return eval_statements(program_statements(p),opt)
    else:
        print("This is not a legit program")


def eval_statements(p,opt):
    variabeltable = opt
    if empty_statements(p):
        return variabeltable
    elif isstatements(p):
            if isassignment(first_statement(p)):
                variabeltable = eval_assignement(first_statement(p), variabeltable)
                return eval_statements(rest_statements(p), variabeltable)
            elif isselection(first_statement(p)):
                variabeltable = eval_selection(first_statement(p), variabeltable)
                return eval_statements(rest_statements(p), variabeltable)
            elif isinput(first_statement(p)):
                variabeltable = eval_input(first_statement(p), variabeltable)
                return eval_statements(rest_statements(p), variabeltable)
            elif isrepetition(first_statement(p)):
                variabeltable = eval_repetition(first_statement(p), variabeltable)
                return eval_statements(rest_statements(p), variabeltable)
            elif isoutput(first_statement(p)):
                variabeltable = output(first_statement(p), variabeltable)
                return eval_statements(rest_statements(p), variabeltable)
    elif isinstance(p, list):
        return eval_statements([p], variabeltable)


def eval_assignement(p,opt):
    variabeltable = opt
    if isinstance(assignment_expression(p), list):
        new_table = deepcopy(variabeltable)
        a = assignment_variable(p)
        b = eval_expression(assignment_expression(p),variabeltable)
        new_table[a] = b
        return new_table
    else:
        new_table = deepcopy(variabeltable)
        a = assignment_variable(p)
        b = assignment_expression(p)
        new_table[a] = b
        return new_table

def eval_selection(p,opt):
    variabeltable = opt
    if eval_condition(selection_condition(p), variabeltable):
        return eval_statements(selection_true(p), variabeltable)
    elif hasfalse(p):
        return eval_statements(selection_false(p), variabeltable)
    else:
        return variabeltable


def eval_repetition(p, opt):
    variabeltable = opt
    while eval_condition(repetition_condition(p), variabeltable):
        return eval_statements(repetition_statements(p), variabeltable)

def eval_condition(p, opt):
    variabeltable = opt
    print(p)
    operator = condition_operator(p)
    a = eval_expression(condition_left(p),variabeltable)
    b = eval_expression(condition_right(p),variabeltable)
    if operator == "<":
        return a < b
    elif operator == ">":
        return a > b
    elif operator == "=":
        return a == b
    else:
        raise ValueError

def eval_expression(p, opt):
    print(p)
    variabeltable = opt
    if isvariable(p):
        return variabeltable[p]
    elif isconstant(p):
        return p
    elif isbinaryoper(p[1]):
        return eval_binaryexpr(p,variabeltable)

def eval_binaryexpr(p, opt):
    variabeltable = opt
    binary_op = binary_operator(p)
    a = eval_expression(binary_left(p),variabeltable)
    b = eval_expression(binary_right(p), variabeltable)
    if binary_op == "+":
        return a + b
    elif binary_op == "-":
        return a - b
    elif binary_op == "*":
        return a * b
    elif binary_op == "/":
        return a / b


def eval_input(p, opt):
    variabeltable = opt
    new_table = deepcopy(variabeltable)
    a = input_variable(p)
    new_table[a] = int(input("Enter value for "+a+": "))
    return new_table

def output(p, opt):
    variabeltable = opt
    a = output_variable(p)
    print (a, "=", variabeltable[a])
    return variabeltable
