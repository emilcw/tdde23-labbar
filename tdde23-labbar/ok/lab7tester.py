"""
Emil Wiman, emiwi425
August Nordin, augno992
Laboration 7A och 7B, Tester med hjälp av assert
"""

from tree import *

db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
       ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']],
       ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993]]]

def test_lab7():

    # -- LAB 7A
    def match(seq, pattern):
        """
        Returns whether given sequence matches the given pattern.
        """
        if not pattern:
            return not seq
        elif isinstance(pattern[0],list):
            if_in_this = match(seq, pattern[0])
            return if_in_this
        elif pattern[0] == '--':
            if match(seq, pattern[1:]):
                return True
            elif not seq:
                return False
            else:
                return match(seq[1:], pattern)
        elif not seq:
            return False
        elif isinstance(seq[0],list):
            if_in_that = match(seq[0],pattern)
            return if_in_that
        elif pattern[0] == '&':
            return match(seq[1:], pattern[1:])
        elif seq[0] == pattern[0]:
            return match(seq[1:], pattern[1:])
        else:
            return False

    assert match(['anka', 'häst', 'ko'], [ 'anka','&', 'ko']) == True               #Test with '&' to see if it matches strictly on element
    assert match(['anka', 'häst','koala', 'ko'], [ 'anka','--', 'ko']) == True      #Test with '--' to see if it matches zero, one or more element
    assert match(['anka', 'häst','koala', 'ko'], [ 'anka','&', 'ko']) == False      #Test with '&' to see if it returns False with several elements
    assert match(['anka', 'häst','koala', 'gås'], [ 'anka','--', 'ko']) == False    #Test with '--' to see if it stays True to the pattern given


    def search(pattern,database):
        """Takes a given pattern and searches through a database
        and returns matches"""
        if not database:
            return []
        elif match(database[0],pattern):
            return database[0] + search(pattern, database[1:])
        else:
            return search(pattern, database[1:])


    #We use the database given in the exercise
    assert search([['författare', ['anders', '&']] , ['titel', ['--']], ['år', '&']], db) == \
    [['författare', ['anders', 'haraldsson']], ['titel', ['programmering', 'i', 'lisp']], ['år', 1993]] #Testing the '&' token and the '--' so they work properly.

    assert search(['--', ['år', 2001], '--'], db) == [] #Testing so it checks the year.

    assert search(['--', ['titel', ['&','&','&','&']], '--'], db) == \
    [['författare', ['j', 'glenn', 'brookshear']], ['titel', ['computer', 'science', 'an', 'overview']], ['år', 2011]] #Testing a more dynamic search.

    assert search(['smörgås'], []) == [] # Testing if it does not recieves a database


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

    assert contains_key(4,[]) == False                                  #Test if it does not recive a tree
    assert contains_key(3,3) == True                                    #Test when it recieves a single node
    assert contains_key(2, [6, 7, [[2, 3, 4, 5], 0, []]]) == False      #Test should return false since the tree is not binary
    assert contains_key(2, [[4,3,7],3,[ 2,8,9]]) == True                #Test to see a regular search in two branches
    assert contains_key(57, [ [4,3,7], 3, [ 2,8,9] ]) == False          #Test to see that it cannot find key

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

    assert tree_size([]) == 0                                   #Test with an empty tree
    assert tree_size(3) == 1                                    #Test with a single node
    assert tree_size([2,10,[45, 25, [36, 346, 13]]]) == 7       #Test with a more complex tree


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

    assert tree_depth([4,6,7,8]) == None                                                #Test should return nothing since its not a binary tree
    assert tree_depth([]) == 0                                                          #Test with an empty tree
    assert tree_depth(5) == 1                                                           #Test with a single node
    assert tree_depth([[3,6,[13, 46, [34, 57, []]]],10,[45, 25, [36, 346, 13]]]) == 5   #Test with a more complex tree



    print("The code passed all tests")
