from pascal_interpreter import Node, Number, UnaryOp, BinaryOp, TokenType


class InterpreterException(Exception):
    pass


class Interpreter:
    def __call__(self, tree: Node) -> float:
        return self._visit(tree)

    def _visit(self, node: Node) -> float:
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, UnaryOp):
            return self._visit_unaryop(node)
        elif isinstance(node, BinaryOp):
            return self._visit_binaryop(node)
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


