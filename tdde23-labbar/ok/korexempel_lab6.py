from lab6 import *
factorial = ['calc',
                ['read', 'n'],
                ['set', 'res', 1],
                ['while', ['n', '>', 0],
                    ['set', 'res', ['res', '*', 'n']],
                    ['set', 'n', ['n', '-', 1]]],
                ['print', 'res']]
print("Print the factorial", eval_program(factorial))




fibonacci = ['calc',
                ['read', 'n'],
                ['set', 'm', 0],
                ['set', 'a', 0],
                ['set', 'b', 1],
                ['set', 'c', 0],
                ['while',['n', '>', 'm'],
                    ["set", 'm', ['m','+',1]],
                    ['set', 'c', ['a', '+', 'b']],
                    ['set', 'a', 'b'],
                    ['set', 'b', 'c']],
                ['print', 'c']]
new_table = fibonacci

print("Print the Fibonacci nr at that index", eval_program(new_table))



lower = ['calc',
            ['read', 'n'],
            ['read', 'm'],
            ['if', ['n','>', 'm'],
                ['print','m'], ['print', 'n']
            ]]
print("Print the loweer nr", eval_program(lower))
