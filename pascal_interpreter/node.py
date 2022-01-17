from pascal_interpreter import Token


class Node:
    pass


class Number(Node):

    def __init__(self, token: Token) -> None:
        self.token = token
        super().__init__()

    def __str__(self) -> str:
        return f"Number({self.token})"


class BinaryOp(Node):

    def __init__(self, left: Node, operation: Token, right: Node) -> None:
        self.left = left
        self.operation = operation
        self.right = right

    def __str__(self) -> str:
        return f"Binary Operation: {self.operation.value} (left: {self.left}, right: {self.right})"


class UnaryOp(Node):

    def __init__(self, operation: Token, left: Node) -> None:
        self.operation = operation
        self.left = left

    def __str__(self) -> str:
        return f"Unary Operation: {self.operation.value} node: {self.left}"


class Statements(Node):
    def __init__(self, values=None):
        if values is None:
            values = []
        self.values = values

    def __str__(self) -> str:
        return f"Statement List: {self.values}"


class AssignOp(Node):
    def __init__(self, left: Node, operation: Token, right: Node) -> None:
        self.left = left
        self.operation = operation
        self.right = right

    def __str__(self) -> str:
        return f"AssignOp: {self.operation.value} (left: {self.left}, right: {self.right})"


class Variable(Node):
    def __init__(self, variable: Token):
        self.variable = variable
        self.value = variable.value

    def __str__(self) -> str:
        return f"Variable: {self.variable} = {self.value}"


class Empty(Node):
    pass
