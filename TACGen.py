class TACGenerator:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def generate(self, node):
        method_name = f'gen_{type(node).__name__}'
        method = getattr(self, method_name, self.unsupported_node)
        return method(node)

    def unsupported_node(self, node):
        raise Exception(f"TAC generation not supported for node type: {type(node).__name__}")

    def gen_ConstantNode(self, node):
        return str(node.value)

    def gen_VariableNode(self, node):
        return node.name

    def gen_BinaryOpNode(self, node):
        left = self.generate(node.left)
        right = self.generate(node.right)
        temp = self.new_temp()
        self.code.append(f"{temp} = {left} {node.op} {right}")
        return temp

    def gen_UnaryOpNode(self, node):
        operand = self.generate(node.operand)
        temp = self.new_temp()
        self.code.append(f"{temp} = {node.op}{operand}")
        return temp

    def gen_AssignmentNode(self, node):
        target = self.generate(node.target)
        value = self.generate(node.value)
        if node.op == '=':
            self.code.append(f"{target} = {value}")
        else:
            # Por ejemplo: x += y → t1 = x + y ; x = t1
            op = node.op[:-1]  # '+=' → '+'
            temp = self.new_temp()
            self.code.append(f"{temp} = {target} {op} {value}")
            self.code.append(f"{target} = {temp}")
        return target

    def gen_ConditionalExpressionNode(self, node):
        result = self.new_temp()
        label_true = self.new_label()
        label_false = self.new_label()
        label_end = self.new_label()

        cond = self.generate(node.condition)
        self.code.append(f"if {cond} goto {label_true}")
        self.code.append(f"goto {label_false}")
        self.code.append(f"{label_true}:")
        true_val = self.generate(node.true_expr)
        self.code.append(f"{result} = {true_val}")
        self.code.append(f"goto {label_end}")
        self.code.append(f"{label_false}:")
        false_val = self.generate(node.false_expr)
        self.code.append(f"{result} = {false_val}")
        self.code.append(f"{label_end}:")
        return result

    def gen_VarDeclNode(self, node):
        # Solo declaramos, sin inicialización (TAC no necesita acción)
        return None

    def gen_MethodDeclNode(self, node):
        self.code.append(f"\n# Begin method {node.name}")
        for param in node.parameters:
            self.code.append(f"# param {param[0]} : {param[1]}")
        for stmt in node.body:
            self.generate(stmt)
        self.code.append(f"# End method {node.name}\n")

    def gen_ClassNode(self, node):
        self.code.append(f"# Class {node.name}")
        for member in node.members:
            self.generate(member)

    def get_code(self):
        return '\n'.join(self.code)
    def clear(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []