# Generador de Código Intermedio (TAC) para un AST simple
# Este generador de código intermedio produce un código similar a TAC (Three Address Code)
# para un AST simple. El código generado es una representación intermedia que puede ser utilizada
# para optimización y generación de código final.

# El código generado es una lista de instrucciones, donde cada instrucción tiene la forma:
#   <temp> = <operador> <op1> <op2>
#   <temp> = <unario_op> <op>
#   <temp> = <valor>
#   <temp> = <variable>
#   <variable> = <temp>
#   if <cond> goto <label>
#   goto <label>
#   <label>:    
#   <temp> = <true_expr>
#   <temp> = <false_expr>
#   <temp> = <method_call>
#   <temp> = <class_instance>
#   <temp> = <method_return>    
#   <temp> = <class_member_access>
#   <temp> = <array_access>
#   <temp> = <array_length> 
#   <temp> = <array_assignment>
#   <temp> = <array_declaration>    
#   <temp> = <array_initialization>
#   <temp> = <array_method_call>
#   <temp> = <array_member_access>
#   <temp> = <array_length>

from  ast_builder import ASTBuilder
from antlr4 import *
from ast_nodes import *
from semantic_analyzer import SemanticAnalyzer
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
        if isinstance(node, AssignmentNode):
            rhs = self.generate(node.value)
            self.code.append(f"{node.target} = {rhs}")
        elif isinstance(node, BinaryOpNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {node.op} {right}")
            return temp
        elif isinstance(node, UnaryOpNode):
            operand = self.generate(node.operand)
            temp = self.new_temp()
            self.code.append(f"{temp} = {node.op}{operand}")
            return temp
        elif isinstance(node, VarDeclarationNode):
            return node.name
        elif isinstance(node, ConstantNode):
            return str(node.value)
        else:
            raise Exception("Nodo del AST desconocido: " + str(node))

    def get_code(self):
        return self.code

    def unsupported_node(self, node):
        raise Exception(f"La generación del TAC no es soportada por el tipo de nodo: {type(node).__name__}")

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

    # Ciclos de generación de código

    def gen_IfNode(self, node):
        cond = self.generate(node.condition)
        label_end = self.new_label("endif")
        self.emit(f"ifFalse {cond} goto {label_end}")
        for stmt in node.body:
            self.generate(stmt)
        self.emit(f"{label_end}:")
    
    def gen_IfElseNode(self, node):
        cond = self.generate(node.condition)
        label_else = self.new_label("else")
        label_end = self.new_label("endif")
        self.emit(f"ifFalse {cond} goto {label_else}")
        for stmt in node.then_body:
            self.generate(stmt)
        self.emit(f"goto {label_end}")
        self.emit(f"{label_else}:")
        for stmt in node.else_body:
            self.generate(stmt)
            self.emit(f"{label_end}:")

    def gen_WhileNode(self, node):
        label_start = self.new_label("while_start")
        label_end = self.new_label("while_end")
        self.emit(f"{label_start}:")
        cond = self.generate(node.condition)
        self.emit(f"ifFalse {cond} goto {label_end}")
        for stmt in node.body:
            self.generate(stmt)
        self.emit(f"goto {label_start}")
        self.emit(f"{label_end}:")

    def gen_DoWhileNode(self, node):
        label_start = self.new_label("do_start")
        self.emit(f"{label_start}:")
        for stmt in node.body:
            self.generate(stmt)
        cond = self.generate(node.condition)
        self.emit(f"if {cond} goto {label_start}")

    def gen_ForNode(self, node):
        if node.init:
            self.generate(node.init)
            label_start = self.new_label("for_start")
            label_end = self.new_label("for_end")
        self.emit(f"{label_start}:")
        if node.condition:
            cond = self.generate(node.condition)
            self.emit(f"ifFalse {cond} goto {label_end}")
        for stmt in node.body:
            self.generate(stmt)
        if node.increment:
            self.generate(node.increment)
        self.emit(f"goto {label_start}")
        self.emit(f"{label_end}:")

    def gen_ForeachNode(self, node):
        # node.collection -> expresión con una lista u objeto iterable
        # node.var -> nombre de la variable iteradora
        collection_temp = self.generate(node.collection)
        index_temp = self.new_temp()
        length_temp = self.new_temp()
    
        self.emit(f"{index_temp} = 0")
        self.emit(f"{length_temp} = len {collection_temp}")

        label_start = self.new_label("foreach_start")
        label_end = self.new_label("foreach_end")

        self.emit(f"{label_start}:")
        self.emit(f"if {index_temp} >= {length_temp} goto {label_end}")
        iter_value = self.new_temp()
        self.emit(f"{iter_value} = {collection_temp}[{index_temp}]")
        self.emit(f"{node.var} = {iter_value}")
        for stmt in node.body:
            self.generate(stmt)
        self.emit(f"{index_temp} = {index_temp} + 1")
        self.emit(f"goto {label_start}")
        self.emit(f"{label_end}:")

    def gen_SwitchNode(self, node):
        expr = self.generate(node.expression)
        end_label = self.new_label("switch_end")
        case_labels = {}
    
        # Crear etiquetas para cada case
        for case in node.cases:
            label = self.new_label("case")
            case_labels[case.value] = label

        default_label = self.new_label("default") if node.default else end_label

        # Comparaciones
        for case_value, label in case_labels.items():
            self.emit(f"if {expr} == {case_value} goto {label}")
        self.emit(f"goto {default_label}")

        # Generar código de cada case
        for case in node.cases:
            self.emit(f"{case_labels[case.value]}:")
            for stmt in case.body:
                self.generate(stmt)
        self.emit(f"goto {end_label}")

        if node.default:
            self.emit(f"{default_label}:")
            for stmt in node.default:
                self.generate(stmt)

        self.emit(f"{end_label}:")