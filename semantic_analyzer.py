# semantic_analyzer.py
from ast_nodes import *
from ast_builder import *

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.errors = []

    def analyze(self, node):
        self.visit(node)
        return self.errors

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.unsupported)
        return method(node)

    def unsupported(self, node):
        raise Exception(f"No hay verificación semantica para el tipo de nodo: {type(node).__name__}")

    def generic_visit(self, node):
        self.errors.append(f"No se implementó visit para {type(node).__name__} en línea {node.line}, columna {node.column}")

    def visit_ProgramNode(self, node):
        for stmt in node.statements:
            self.visit(stmt)

    def visit_VarDeclarationNode(self, node):
        if node.name in self.symbol_table:
            self.errors.append(f"Variable '{node.name}' ya declarada en línea {node.line}, columna {node.column}")
        else:
            self.symbol_table[node.name] = {
                'type': node.type,
                'line': node.line,
                'column': node.column
            }
        if node.value:
            expr_type = self.visit(node.value)
            if expr_type and expr_type != node.type:
                self.errors.append(
                    f"Tipo incompatible en declaración de '{node.name}': esperado '{node.type}', obtenido '{expr_type}' en línea {node.line}, columna {node.column}"
                )

    def visit_AssignmentNode(self, node):
        if node.name not in self.symbol_table:
            self.errors.append(f"Variable '{node.name}' no declarada en línea {node.line}, columna {node.column}")
            return
        expected_type = self.symbol_table[node.name]['type']
        actual_type = self.visit(node.value)
        if actual_type and actual_type != expected_type:
            self.errors.append(
                f"Tipo incompatible en asignación a '{node.name}': esperado '{expected_type}', obtenido '{actual_type}' en línea {node.line}, columna {node.column}"
            )

    def visit_Literal(self, node):
        return node.type

    def visit_VariableNode(self, node):
        if node.name not in self.symbol_table:
            self.errors.append(f"Variable '{node.name}' no declarada en línea {node.line}, columna {node.column}")
            return None
        return self.symbol_table[node.name]['type']
    
    def visit_IfNode(self, node):
        self.visit(node.condition)
        self.visit(node.then_block)
        if node.else_block:
            self.visit(node.else_block)

    def visit_WhileNode(self, node):
        self.visit(node.condition)
        self.visit(node.body)

    def visit_DoWhileNode(self, node):
        self.visit(node.body)
        self.visit(node.condition)

    def visit_ForNode(self, node):
        if node.init:
            self.visit(node.init)
        if node.condition:
            self.visit(node.condition)
        if node.update:
            self.visit(node.update)
        self.visit(node.body)

    def visit_ForeachNode(self, node):
        if node.var_name in self.symbol_table:
            self.errors.append(f"Variable '{node.var_name}' ya declarada en foreach (línea {node.line}, columna {node.column})")
        else:
            self.symbol_table[node.var_name] = {'type': node.var_type, 'line': node.line, 'column': node.column}
        self.visit(node.collection)
        self.visit(node.body)

    def visit_SwitchNode(self, node):
        self.visit(node.expression)
        for case in node.cases:
            self.visit(case)

    def visit_SwitchCaseNode(self, node):
        for label in node.labels:
            self.visit(label)
        for stmt in node.statements:
            self.visit(stmt)

    def visit_BinaryOpNode(self, node):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        if left_type != right_type:
            self.errors.append(
                f"Tipos incompatibles en operación binaria: '{left_type}' y '{right_type}' en línea {node.line}, columna {node.column}"
            )
            return None
        return left_type

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def define(self, name, symbol):
        if name in self.symbols:
            raise Exception(f"Símbolo '{name}' ya está definido en este ámbito.")
        self.symbols[name] = symbol

    def resolve(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.resolve(name)
        else:
            return None

    def visit_ClassNode(self, node, scope):
        if scope.resolve(node.name):
            self.errors.append(f"Error: Clase '{node.name}' ya está definida (Línea {node.line}, Columna {node.column})")
        else:
            scope.define(node.name, node)

        class_scope = SymbolTable(scope)
        for method in node.methods:
            self.visit(method, class_scope)

    def visit_MethodNode(self, node, scope):
        if scope.resolve(node.name):
            self.errors.append(f"Error: Método '{node.name}' ya está definido (Línea {node.line}, Columna {node.column})")
        else:
            scope.define(node.name, node)

        method_scope = SymbolTable(scope)
        for param in node.parameters:
            self.visit(param, method_scope)
        self.visit(node.body, method_scope)

    def visit_ParameterNode(self, node, scope):
        if scope.resolve(node.name):
            self.errors.append(f"Error: Parámetro '{node.name}' duplicado (Línea {node.line}, Columna {node.column})")
        else:
            scope.define(node.name, node)

    def visit_BlockNode(self, node, scope):
        block_scope = SymbolTable(scope)
        for stmt in node.statements:
            if isinstance(stmt, VarDeclarationNode):
                if block_scope.resolve(stmt.name):
                    self.errors.append(f"Error: Variable '{stmt.name}' ya declarada en este ámbito (Línea {stmt.line}, Columna {stmt.column})")
                else:
                    block_scope.define(stmt.name, stmt)
            self.visit(stmt, block_scope)

    def visit_TypeNode(self, node, scope):
        tipos_validos = [
            "int", "float", "double", "bool", "char", "string",
            "byte", "sbyte", "short", "ushort", "uint", "ulong", "decimal"
        ]
        if node.name not in tipos_validos:
            self.errors.append(f"Error: Tipo desconocido '{node.name}' (Línea {node.line}, Columna {node.column})")
        return node.name