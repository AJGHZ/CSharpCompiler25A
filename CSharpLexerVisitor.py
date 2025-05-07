# Generated from CSharpLexer.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSharpLexerParser import CSharpLexerParser
else:
    from CSharpLexerParser import CSharpLexerParser

# This class defines a complete generic visitor for a parse tree produced by CSharpLexerParser.

class CSharpLexerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSharpLexerParser#variable_declaration.
    def visitVariable_declaration(self, ctx:CSharpLexerParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:CSharpLexerParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#constant_declaration.
    def visitConstant_declaration(self, ctx:CSharpLexerParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#type_identifier.
    def visitType_identifier(self, ctx:CSharpLexerParser.Type_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#expression.
    def visitExpression(self, ctx:CSharpLexerParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#primary_expression.
    def visitPrimary_expression(self, ctx:CSharpLexerParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#unary_expression.
    def visitUnary_expression(self, ctx:CSharpLexerParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:CSharpLexerParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#additive_expression.
    def visitAdditive_expression(self, ctx:CSharpLexerParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#shift_expression.
    def visitShift_expression(self, ctx:CSharpLexerParser.Shift_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#relational_expression.
    def visitRelational_expression(self, ctx:CSharpLexerParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#equality_expression.
    def visitEquality_expression(self, ctx:CSharpLexerParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#logical_and_expression.
    def visitLogical_and_expression(self, ctx:CSharpLexerParser.Logical_and_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#logical_or_expression.
    def visitLogical_or_expression(self, ctx:CSharpLexerParser.Logical_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#conditional_expression.
    def visitConditional_expression(self, ctx:CSharpLexerParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#assignment_expression.
    def visitAssignment_expression(self, ctx:CSharpLexerParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#assignment_operator.
    def visitAssignment_operator(self, ctx:CSharpLexerParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#literal.
    def visitLiteral(self, ctx:CSharpLexerParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#error.
    def visitError(self, ctx:CSharpLexerParser.ErrorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#float_declaration.
    def visitFloat_declaration(self, ctx:CSharpLexerParser.Float_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#prog.
    def visitProg(self, ctx:CSharpLexerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#controlStructure.
    def visitControlStructure(self, ctx:CSharpLexerParser.ControlStructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#ifStatement.
    def visitIfStatement(self, ctx:CSharpLexerParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#switchStatement.
    def visitSwitchStatement(self, ctx:CSharpLexerParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#switchSection.
    def visitSwitchSection(self, ctx:CSharpLexerParser.SwitchSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#caseLabel.
    def visitCaseLabel(self, ctx:CSharpLexerParser.CaseLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#whileStatement.
    def visitWhileStatement(self, ctx:CSharpLexerParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:CSharpLexerParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#forStatement.
    def visitForStatement(self, ctx:CSharpLexerParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#forInitializer.
    def visitForInitializer(self, ctx:CSharpLexerParser.ForInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#forIterator.
    def visitForIterator(self, ctx:CSharpLexerParser.ForIteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#foreachStatement.
    def visitForeachStatement(self, ctx:CSharpLexerParser.ForeachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#block.
    def visitBlock(self, ctx:CSharpLexerParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#statement.
    def visitStatement(self, ctx:CSharpLexerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CSharpLexerParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#expressionList.
    def visitExpressionList(self, ctx:CSharpLexerParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#compilationUnit.
    def visitCompilationUnit(self, ctx:CSharpLexerParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#classDeclaration.
    def visitClassDeclaration(self, ctx:CSharpLexerParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#classBase.
    def visitClassBase(self, ctx:CSharpLexerParser.ClassBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#classBody.
    def visitClassBody(self, ctx:CSharpLexerParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#classMemberDeclaration.
    def visitClassMemberDeclaration(self, ctx:CSharpLexerParser.ClassMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:CSharpLexerParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#returnType.
    def visitReturnType(self, ctx:CSharpLexerParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#formalParameterList.
    def visitFormalParameterList(self, ctx:CSharpLexerParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#fixedParameters.
    def visitFixedParameters(self, ctx:CSharpLexerParser.FixedParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#fixedParameter.
    def visitFixedParameter(self, ctx:CSharpLexerParser.FixedParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#parameterModifier.
    def visitParameterModifier(self, ctx:CSharpLexerParser.ParameterModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#parameterArray.
    def visitParameterArray(self, ctx:CSharpLexerParser.ParameterArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#methodBody.
    def visitMethodBody(self, ctx:CSharpLexerParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#type.
    def visitType(self, ctx:CSharpLexerParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#attributes.
    def visitAttributes(self, ctx:CSharpLexerParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#attributeSection.
    def visitAttributeSection(self, ctx:CSharpLexerParser.AttributeSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#attributeList.
    def visitAttributeList(self, ctx:CSharpLexerParser.AttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#attribute.
    def visitAttribute(self, ctx:CSharpLexerParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#modifiers.
    def visitModifiers(self, ctx:CSharpLexerParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#modifier.
    def visitModifier(self, ctx:CSharpLexerParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#typeParameters.
    def visitTypeParameters(self, ctx:CSharpLexerParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#null_literal.
    def visitNull_literal(self, ctx:CSharpLexerParser.Null_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpLexerParser#boolean_literal.
    def visitBoolean_literal(self, ctx:CSharpLexerParser.Boolean_literalContext):
        return self.visitChildren(ctx)



del CSharpLexerParser