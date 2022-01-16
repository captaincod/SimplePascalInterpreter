from pascal_interpreter import Parser, Interpreter

if __name__ == '__main__':
    parser = Parser()
    my_interpreter = Interpreter()
    expression = parser('5 * 10')  # >>> 50.0
    print(my_interpreter(expression))
    parser = Parser()
    print(my_interpreter(parser.parse("2 + 2")))  # >>> 4.0
    print(my_interpreter(parser.parse("(11224-4)/(10)")))  # >>> 1122.0
    # print(my_interpreter(parser.parse("?")))  # >>> LexerException: Bad token
