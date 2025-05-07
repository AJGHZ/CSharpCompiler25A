# ast_builder.py
from CSharpLexerVisitor import CSharpLexerVisitor
from ast_nodes import *

class ASTBuilder(CSharpLexerVisitor):
    def visitProg(self, ctx):
        statements = [self.visit(child) for child in ctx.children if self.visit(child) is not None]
        return ProgramNode(statements, ctx.start.line, ctx.start.column)

    def visitVarDecl(self, ctx):
        var_type = ctx.TYPE().getText()
        name = ctx.ID().getText()
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDeclarationNode(var_type, name, expr, ctx.start.line, ctx.start.column)

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return AssignmentNode(name, value, ctx.start.line, ctx.start.column)
    

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expr())
        then_block = self.visit(ctx.thenBlock)
        else_block = self.visit(ctx.elseBlock) if ctx.elseBlock else None
        return IfNode(condition, then_block, else_block)

    def visitWhileStatement(self, ctx):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.statementBlock())
        return WhileNode(condition, body)

    def visitDoWhileStatement(self, ctx):
        body = self.visit(ctx.statementBlock())
        condition = self.visit(ctx.expr())
        return DoWhileNode(condition, body)

    def visitForStatement(self, ctx):
        init = self.visit(ctx.init) if ctx.init else None
        condition = self.visit(ctx.condition) if ctx.condition else None
        update = self.visit(ctx.update) if ctx.update else None
        body = self.visit(ctx.statementBlock())
        return ForNode(init, condition, update, body)

    def visitForeachStatement(self, ctx):
        type_name = ctx.TYPE().getText()
        var_name = ctx.ID().getText()
        collection = self.visit(ctx.expr())
        body = self.visit(ctx.statementBlock())
        return ForeachNode(type_name, var_name, collection, body)

    def visitSwitchStatement(self, ctx):
        expr = self.visit(ctx.expr())
        cases = [self.visit(case) for case in ctx.switchSection()]
        return SwitchNode(expr, cases)

    def visitSwitchSection(self, ctx):
        labels = [label.getText() for label in ctx.switchLabel()]
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return SwitchCaseNode(labels, statements)

    def visitExpr(self, ctx):
        if ctx.INT():
            return LiteralNode(int(ctx.INT().getText()), 'int', ctx.start.line, ctx.start.column)
        elif ctx.BOOL():
            return LiteralNode(ctx.BOOL().getText() == 'true', 'bool', ctx.start.line, ctx.start.column)
        elif ctx.ID():
            return VarDeclarationNode(ctx.ID().getText(), ctx.start.line, ctx.start.column)
        elif ctx.op and len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            return BinaryOpNode(left, op, right, ctx.start.line, ctx.start.column)
        else:
            return self.visit(ctx.expr(0))  # Paréntesis u otra forma

    def visitStatement(self, ctx):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        else:
            return None  # para extensiones futuras
