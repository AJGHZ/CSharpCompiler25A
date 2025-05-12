class ASTNode:
    def __init__(self, line, column):
        self.line = line
        self.column = column

class ProgramNode(ASTNode):
    def __init__(self, statements, line=0, column=0):
        super().__init__(line, column)
        self.statements = statements

class VarDeclarationNode(ASTNode):
    def __init__(self, var_type, var_name, expression=None, line=0, column=0):
        super().__init__(line, column)
        self.var_type = var_type
        self.var_name = var_name
        self.expression = expression

class AssignmentNode(ASTNode):
    def __init__(self, var_name, expression, line=0, column=0):
        super().__init__(line, column)
        self.var_name = var_name
        self.expression = expression

class IfNode(ASTNode):
    def __init__(self, condition, then_block, else_block=None, line=0, column=0):
        super().__init__(line, column)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class WhileNode(ASTNode):
    def __init__(self, condition, body, line=0, column=0):
        super().__init__(line, column)
        self.condition = condition
        self.body = body

class DoWhileNode(ASTNode):
    def __init__(self, condition, body):
        super().__init__()
        self.condition = condition
        self.body = body

class ForNode(ASTNode):
    def __init__(self, init, condition, update, body, line=0, column=0):
        super().__init__(line, column)
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

class ForeachNode(ASTNode):
    def __init__(self, var_type, var_name, collection, body):
        super().__init__()
        self.var_type = var_type
        self.var_name = var_name
        self.collection = collection
        self.body = body

class SwitchNode(ASTNode):
    def __init__(self, expression, cases):
        super().__init__()
        self.expression = expression
        self.cases = cases

class SwitchCaseNode(ASTNode):
    def __init__(self, labels, statements):
        super().__init__()
        self.labels = labels
        self.statements = statements

class BinaryOpNode(ASTNode):
    def __init__(self, left, operator, right, line=0, column=0):
        super().__init__(line, column)
        self.left = left
        self.operator = operator
        self.right = right

class LiteralNode(ASTNode):
    def __init__(self, value, line=0, column=0):
        super().__init__(line, column)
        self.value = value
        self.type = self._infer_type(value)

    def _infer_type(self, value):
        if isinstance(value, int):
            return "int"
        elif isinstance(value, float):
            return "float"
        elif isinstance(value, str):
            return "string"
        elif isinstance(value, bool):
            return "bool"
        return "unknown"

class IdentifierNode(ASTNode):
    def __init__(self, name, line=0, column=0):
        super().__init__(line, column)
        self.name = name
        self.type = None
        self.value = None
        self.initialized = False

class ClassNode:
    def __init__(self, name, members, line, column):
        self.name = name
        self.members = members
        self.line = line
        self.column = column

class MethodNode:
    def __init__(self, name, return_type, parameters, body, line, column):
        self.name = name
        self.return_type = return_type
        self.parameters = parameters
        self.body = body
        self.line = line
        self.column = column

class ParameterNode:
    def __init__(self, name, param_type, line, column):
        self.name = name
        self.param_type = param_type
        self.line = line
        self.column = column

class BlockNode(ASTNode):
    def __init__(self, statements, line, column):
        super().__init__(line, column)
        self.statements = statements  # Lista de nodos (sentencias)

class TypeNode:
    def __init__(self, name):
        self.name = name

