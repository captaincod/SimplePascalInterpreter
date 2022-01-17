from pascal_interpreter import Token, TokenType


class LexerException(Exception):
    pass


class Lexer:
    def __init__(self):
        self._pos: int = -1
        self._text: str = ''
        self._current_char: str = ''

    def next(self) -> Token:
        while self._current_char is not None:
            if self._current_char == ' ':
                self._skip()
                continue
            if self._current_char == '\n':
                self._forward()
                self._skip()
                continue
            if self._current_char.isdigit():
                return Token(TokenType.FLOAT, self._number())
            if self._current_char.isalpha():
                string = ''
                while self._current_char.isalpha():
                    string += self._current_char
                    self._forward()
                if string == 'BEGIN':
                    return Token(TokenType.BEGIN, string)
                elif string == 'END':
                    return Token(TokenType.END, string)
                else:
                    return Token(TokenType.VARIABLE, string)
            if self._current_char == '+':
                char = self._current_char
                self._forward()
                return Token(TokenType.PLUS, char)
            if self._current_char == '-':
                char = self._current_char
                self._forward()
                return Token(TokenType.MINUS, char)
            if self._current_char == '*':
                char = self._current_char
                self._forward()
                return Token(TokenType.MUL, char)
            if self._current_char == '/':
                char = self._current_char
                self._forward()
                return Token(TokenType.DIV, char)
            if self._current_char == '(':
                char = self._current_char
                self._forward()
                return Token(TokenType.LPAREN, char)
            if self._current_char == ')':
                char = self._current_char
                self._forward()
                return Token(TokenType.RPAREN, char)
            if self._current_char == '.':
                char = self._current_char
                self._forward()
                return Token(TokenType.DOT, char)
            if self._current_char == ';':
                char = self._current_char
                self._forward()
                return Token(TokenType.SEMI, char)
            if self._current_char == ':':
                char = ''
                char += self._current_char
                self._forward()
                if self._current_char == '=':
                    char += self._current_char
                    self._forward()
                    return Token(TokenType.ASSIGN, char)
                else:
                    raise LexerException(f"Bad token '{self._current_char}'")

            raise LexerException(f"Bad token '{self._current_char}'")
        return Token(TokenType.EOS, None)

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def _skip(self):
        while self._current_char == ' ':
            self._forward()

    def _number(self) -> str:
        result = []
        dots_amount = 0
        while self._current_char and (self._current_char.isdigit() or self._current_char == '.'):
            if self._current_char == '.':
                dots_amount += 1
            if dots_amount > 1:
                raise LexerException("Invalid number")
            result.append(str(self._current_char))
            self._forward()
        if result[len(result) - 1] == '.':
            raise LexerException("Invalid number")
        return "".join(result)

    def init(self, text: str):
        self._text = text
        self._pos = -1
        self._forward()
