from pascal_interpreter import TokenType, \
    Number, Node, UnaryOp, BinaryOp, Statements, AssignOp, Variable, Empty


class InterpreterException(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.data = {}

    def __call__(self, tree: Node) -> float:
        return self._visit(tree)

    def _visit(self, node: Node):
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, UnaryOp):
            return self._visit_unaryop(node)
        elif isinstance(node, BinaryOp):
            return self._visit_binaryop(node)
        elif isinstance(node, Statements):
            return self._visit_statements(node)
        elif isinstance(node, AssignOp):
            return self._visit_assignop(node)
        elif isinstance(node, Variable):
            return self._visit_variable(node)
        elif isinstance(node, Empty):
            return self._visit_empty(node)
        else:
            raise InterpreterException("Invalid node")

    def _visit_number(self, node: Number) -> float:
        return float(node.token.value)

    def _visit_binaryop(self, node: BinaryOp) -> float:
        op = node.operation
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left) + self._visit(node.right)
        if op.type_ == TokenType.MINUS:
            return self._visit(node.left) - self._visit(node.right)
        if op.type_ == TokenType.MUL:
            return self._visit(node.left) * self._visit(node.right)
        if op.type_ == TokenType.DIV:
            return self._visit(node.left) / self._visit(node.right)
        raise InterpreterException("Invalid operator")

    def _visit_unaryop(self, node: UnaryOp) -> float:
        op = node.operation
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left)
        if op.type_ == TokenType.MINUS:
            return 0 - self._visit(node.left)
        raise InterpreterException("Invalid operator")

    def _visit_statements(self, node: Statements):
        for statement in node.values:
            self._visit(statement)

    def _visit_assignop(self, node: AssignOp):
        self.data[node.left] = self._visit(node.right)

    def _visit_variable(self, node: Variable):
        value = node.value
        return self.data[value]

    def _visit_empty(self, node: Empty):
        pass


