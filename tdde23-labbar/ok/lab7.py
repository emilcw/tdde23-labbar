"""
Emil Wiman, emiwi425
August Nordin, augno992
Laboration 7A och 7B
"""

#from tree import *
#import books

# -- LAB 7A
def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern.
    """
    if not pattern:
        return not seq
    elif isinstance(pattern[0],list) and isinstance(seq[0],list):
         return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    #elif isinstance(seq[0],list):
    #    if_in_that = match(seq[0],pattern) + match(seq[1:], pattern)
    #    return if_in_that
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False


def search(pattern,database):
    """Takes a given pattern and searches through a database
    and returns matches"""
    if not database:
        return []
    elif match(database[0],pattern):
        return database[0] + search(pattern, database[1:])
    else:
        return search(pattern, database[1:])


# -- Help functions to 7B
def empty_tree_fn():
    return 0

def leaf_fn(key):
    return key**2

def inner_node_fn(key,left_value,right_value):
    return key + left_value


# -- LAB 7B
def traverse(tree, func1, func2, func3):
    """ Searches through a binary tree and handles different scenarios with
    the help from the given functions.
    """
    if is_empty_tree(tree):
        return func3()
    elif is_leaf(tree):
        return func2(tree)
    elif len(tree) == 3:
        return func1(get_key(tree), traverse(left_subtree(tree), func1, func2, func3), traverse(right_subtree(tree), func1, func2, func3))


def contains_key(key, tree):
    """ Searches through a binary tree with traverse to find a matching key.
    """
    def empty_tree_fn1():
        return False

    def leaf_fn1(leaf):
        if leaf == key:
            return True
        else:
            return False

    def inner_node_fn1(node,left_value,right_value):
        if node == key or left_value == True or right_value == True:
            return True
        else:
            return False

    return traverse(tree, inner_node_fn1, leaf_fn1, empty_tree_fn1)


def tree_size(tree):
    """ Goes through a binary tree with traverse and returns the size of the tree.
    """
    def empty_tree_fn2():
        return 0

    def leaf_fn2(leaf):
        return 1

    def inner_node_fn2(node, left_value, right_value):
        return 1 + left_value + right_value

    return traverse(tree, inner_node_fn2, leaf_fn2, empty_tree_fn2)


def tree_depth(tree):
    """ Goes through a binary tree with traverse and returns the length of the deepest path.
    """
    def empty_tree_fn3():
        return 0

    def leaf_fn3(leaf):
        return 1

    def inner_node_fn3(node, left_value, right_value):
        return 1 + max(left_value, right_value)

    return traverse(tree, inner_node_fn3, leaf_fn3, empty_tree_fn3)
