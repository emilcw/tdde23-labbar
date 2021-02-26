from calc import *
from copy import deepcopy
import pdb


def eval_program(p,opt={}):
    """Interpretator that reads our Calc languague, takes a list of commands
    and evaluets the code"""
    if isprogram(p):
        return eval_statements(program_statements(p),opt)
    else:
        print("This is not a legitimate program")


def eval_statements(p,opt):
    """This function interpret the different types of statements in our code."""
    #pdb.set_trace()
    variabeltable = opt
    if empty_statements(p):
        return variabeltable
    else:
        if isassignment(first_statement(p)):
            variabeltable = eval_assignement(first_statement(p), variabeltable)
        elif isselection(first_statement(p)):
            variabeltable = eval_selection(first_statement(p), variabeltable)
        elif isinput(first_statement(p)):
            variabeltable = eval_input(first_statement(p), variabeltable)
        elif isrepetition(first_statement(p)):
            variabeltable = eval_repetition(first_statement(p), variabeltable)
        elif isoutput(first_statement(p)):
            variabeltable = output(first_statement(p), variabeltable)
        return eval_statements(rest_statements(p), variabeltable)




def eval_assignement(p,opt):
    """This function interpret the different types of assignment in our Calc
    languague"""
    variabeltable = deepcopy(opt)
    a = assignment_variable(p)
    b = eval_expression(assignment_expression(p), variabeltable)
    variabeltable[a] = b
    return variabeltable

def eval_selection(p,opt):
    """This function interpret the differnt types of selection in our Calc
    languague"""
    variabeltable = opt
    if eval_condition(selection_condition(p), variabeltable):
        return eval_statements([selection_true(p)], variabeltable)
    elif hasfalse(p):
        return eval_statements([selection_false(p)], variabeltable)
    else:
        return variabeltable


def eval_repetition(p, opt):
    """This function interpret and executes repetition in our Calc languague"""
    variabeltable = opt
    while eval_condition(repetition_condition(p), variabeltable):
        variabeltable = eval_statements(repetition_statements(p), variabeltable)
    return variabeltable


def eval_condition(p, opt):
    """This function intrepret different conditions in our Calc languague """
    variabeltable = opt
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
    """This function intrepret the different expressions in our Calc languague """
    variabeltable = opt
    if isvariable(p):
        return variabeltable[p]
    elif isconstant(p):
        return p
    elif isbinary(p):
        return eval_binaryexpr(p,variabeltable)

def eval_binaryexpr(p, opt):
    """This function intrepret and executes differnt binary operations
    in our Calc languague """
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
    """This function takes in input to our Calc languague and saves it"""
    variabeltable = deepcopy(opt)
    a = input_variable(p)
    variabeltable[a] = int(input("Enter value for "+a+": "))
    return variabeltable

def output(p, opt):
    """This function prints the output"""
    variabeltable = opt
    a = output_variable(p)
    print(a, "=", variabeltable[a])
    return variabeltable
