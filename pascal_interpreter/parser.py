from pascal_interpreter import Lexer, Token, TokenType, \
    Number, Node, UnaryOp, BinaryOp, Statements, AssignOp, Variable, Empty


class ParserException(Exception):
    pass


class Parser:

    def __init__(self) -> None:
        self._current_token: Token = None
        self._lexer = Lexer()

    def __call__(self, text: str) -> Node:
        return self.parse(text)

    def _program(self):
        complex_statement = self._complex_statement()
        self._check_token_type(TokenType.DOT)
        return complex_statement

    def _complex_statement(self) -> Node:
        self._check_token_type(TokenType.BEGIN)
        statement_list = self._statement_list()
        self._check_token_type(TokenType.END)
        return statement_list

    def _statement_list(self) -> Node:
        statements = [self._statement()]
        while self._current_token.type_ == TokenType.SEMI:
            self._check_token_type(TokenType.SEMI)
            statements.append(self._statement())
        statement_list = Statements(statements)
        return statement_list

    def _statement(self) -> Node:
        if self._current_token.type_ == TokenType.BEGIN:
            return self._complex_statement()
        elif self._current_token.type_ == TokenType.VARIABLE:
            return self._assigment()
        else:
            return self._empty()

    def _assigment(self) -> Node:
        variable = self._variable()
        token = self._current_token
        self._check_token_type(TokenType.ASSIGN)
        expr = self._expr()
        return AssignOp(variable, token, expr)

    def _variable(self) -> Node:
        self._check_token_type(TokenType.VARIABLE)
        return Variable(self._current_token)

    def _empty(self) -> Node:
        return Empty()

    def _expr(self) -> Node:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self._term()

        if self._current_token is None:
            return None
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self._check_token_type(TokenType.PLUS)
            else:
                self._check_token_type(TokenType.MINUS)
            result = BinaryOp(result, token, self._term())
        return result

    def _term(self) -> Node:
        ops = [TokenType.MUL, TokenType.DIV]
        result = self._factor()

        if self._current_token is None:
            return None
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self._check_token_type(TokenType.MUL)
            else:
                self._check_token_type(TokenType.DIV)
            result = BinaryOp(result, token, self._factor())
        return result

    def _factor(self) -> Node:
        token = self._current_token

        if token.type_ == TokenType.FLOAT:
            self._check_token_type(TokenType.FLOAT)
            return Number(token)
        elif token.type_ == TokenType.MINUS:
            self._check_token_type(TokenType.MINUS)
            return UnaryOp(token, self._factor())
        elif token.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
            return UnaryOp(token, self._factor())
        elif token.type_ == TokenType.LPAREN:
            self._check_token_type(TokenType.LPAREN)
            result = self._expr()
            self._check_token_type(TokenType.RPAREN)
            return result
        else:
            raise ParserException(f"Invalid factor {token.type_}")

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise ParserException(f"Invalid expression - expected token type: {type_}")

    def parse(self, text: str) -> Node:
        self._lexer.init(text)
        self._current_token = self._lexer.next()
        return self._program()
