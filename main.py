from pascal_interpreter import Parser, Interpreter

if __name__ == '__main__':
    parser = Parser()
    my_interpreter = Interpreter()
    syntax_tree = parser('(1) + (1 - 1)')
    print(my_interpreter(syntax_tree))
