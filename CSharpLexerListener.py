# Generated from CSharpLexer.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSharpLexerParser import CSharpLexerParser
else:
    from CSharpLexerParser import CSharpLexerParser

# This class defines a complete listener for a parse tree produced by CSharpLexerParser.
class CSharpLexerListener(ParseTreeListener):

    # Enter a parse tree produced by CSharpLexerParser#variable_declaration.
    def enterVariable_declaration(self, ctx:CSharpLexerParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#variable_declaration.
    def exitVariable_declaration(self, ctx:CSharpLexerParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:CSharpLexerParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:CSharpLexerParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#constant_declaration.
    def enterConstant_declaration(self, ctx:CSharpLexerParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#constant_declaration.
    def exitConstant_declaration(self, ctx:CSharpLexerParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#type_identifier.
    def enterType_identifier(self, ctx:CSharpLexerParser.Type_identifierContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#type_identifier.
    def exitType_identifier(self, ctx:CSharpLexerParser.Type_identifierContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#expression.
    def enterExpression(self, ctx:CSharpLexerParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#expression.
    def exitExpression(self, ctx:CSharpLexerParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#primary_expression.
    def enterPrimary_expression(self, ctx:CSharpLexerParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#primary_expression.
    def exitPrimary_expression(self, ctx:CSharpLexerParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#unary_expression.
    def enterUnary_expression(self, ctx:CSharpLexerParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#unary_expression.
    def exitUnary_expression(self, ctx:CSharpLexerParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:CSharpLexerParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:CSharpLexerParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#additive_expression.
    def enterAdditive_expression(self, ctx:CSharpLexerParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#additive_expression.
    def exitAdditive_expression(self, ctx:CSharpLexerParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#shift_expression.
    def enterShift_expression(self, ctx:CSharpLexerParser.Shift_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#shift_expression.
    def exitShift_expression(self, ctx:CSharpLexerParser.Shift_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#relational_expression.
    def enterRelational_expression(self, ctx:CSharpLexerParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#relational_expression.
    def exitRelational_expression(self, ctx:CSharpLexerParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#equality_expression.
    def enterEquality_expression(self, ctx:CSharpLexerParser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#equality_expression.
    def exitEquality_expression(self, ctx:CSharpLexerParser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#logical_and_expression.
    def enterLogical_and_expression(self, ctx:CSharpLexerParser.Logical_and_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#logical_and_expression.
    def exitLogical_and_expression(self, ctx:CSharpLexerParser.Logical_and_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#logical_or_expression.
    def enterLogical_or_expression(self, ctx:CSharpLexerParser.Logical_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#logical_or_expression.
    def exitLogical_or_expression(self, ctx:CSharpLexerParser.Logical_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#conditional_expression.
    def enterConditional_expression(self, ctx:CSharpLexerParser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#conditional_expression.
    def exitConditional_expression(self, ctx:CSharpLexerParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#assignment_expression.
    def enterAssignment_expression(self, ctx:CSharpLexerParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#assignment_expression.
    def exitAssignment_expression(self, ctx:CSharpLexerParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#assignment_operator.
    def enterAssignment_operator(self, ctx:CSharpLexerParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#assignment_operator.
    def exitAssignment_operator(self, ctx:CSharpLexerParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#literal.
    def enterLiteral(self, ctx:CSharpLexerParser.LiteralContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#literal.
    def exitLiteral(self, ctx:CSharpLexerParser.LiteralContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#error.
    def enterError(self, ctx:CSharpLexerParser.ErrorContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#error.
    def exitError(self, ctx:CSharpLexerParser.ErrorContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#float_declaration.
    def enterFloat_declaration(self, ctx:CSharpLexerParser.Float_declarationContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#float_declaration.
    def exitFloat_declaration(self, ctx:CSharpLexerParser.Float_declarationContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#prog.
    def enterProg(self, ctx:CSharpLexerParser.ProgContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#prog.
    def exitProg(self, ctx:CSharpLexerParser.ProgContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#controlStructure.
    def enterControlStructure(self, ctx:CSharpLexerParser.ControlStructureContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#controlStructure.
    def exitControlStructure(self, ctx:CSharpLexerParser.ControlStructureContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#ifStatement.
    def enterIfStatement(self, ctx:CSharpLexerParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#ifStatement.
    def exitIfStatement(self, ctx:CSharpLexerParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#switchStatement.
    def enterSwitchStatement(self, ctx:CSharpLexerParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#switchStatement.
    def exitSwitchStatement(self, ctx:CSharpLexerParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#switchSection.
    def enterSwitchSection(self, ctx:CSharpLexerParser.SwitchSectionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#switchSection.
    def exitSwitchSection(self, ctx:CSharpLexerParser.SwitchSectionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#caseLabel.
    def enterCaseLabel(self, ctx:CSharpLexerParser.CaseLabelContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#caseLabel.
    def exitCaseLabel(self, ctx:CSharpLexerParser.CaseLabelContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#whileStatement.
    def enterWhileStatement(self, ctx:CSharpLexerParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#whileStatement.
    def exitWhileStatement(self, ctx:CSharpLexerParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:CSharpLexerParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:CSharpLexerParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#forStatement.
    def enterForStatement(self, ctx:CSharpLexerParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#forStatement.
    def exitForStatement(self, ctx:CSharpLexerParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#forInitializer.
    def enterForInitializer(self, ctx:CSharpLexerParser.ForInitializerContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#forInitializer.
    def exitForInitializer(self, ctx:CSharpLexerParser.ForInitializerContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#forIterator.
    def enterForIterator(self, ctx:CSharpLexerParser.ForIteratorContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#forIterator.
    def exitForIterator(self, ctx:CSharpLexerParser.ForIteratorContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#foreachStatement.
    def enterForeachStatement(self, ctx:CSharpLexerParser.ForeachStatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#foreachStatement.
    def exitForeachStatement(self, ctx:CSharpLexerParser.ForeachStatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#block.
    def enterBlock(self, ctx:CSharpLexerParser.BlockContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#block.
    def exitBlock(self, ctx:CSharpLexerParser.BlockContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#statement.
    def enterStatement(self, ctx:CSharpLexerParser.StatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#statement.
    def exitStatement(self, ctx:CSharpLexerParser.StatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CSharpLexerParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CSharpLexerParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#expressionList.
    def enterExpressionList(self, ctx:CSharpLexerParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#expressionList.
    def exitExpressionList(self, ctx:CSharpLexerParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CSharpLexerParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CSharpLexerParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#classDeclaration.
    def enterClassDeclaration(self, ctx:CSharpLexerParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#classDeclaration.
    def exitClassDeclaration(self, ctx:CSharpLexerParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#classBase.
    def enterClassBase(self, ctx:CSharpLexerParser.ClassBaseContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#classBase.
    def exitClassBase(self, ctx:CSharpLexerParser.ClassBaseContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#classBody.
    def enterClassBody(self, ctx:CSharpLexerParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#classBody.
    def exitClassBody(self, ctx:CSharpLexerParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#classMemberDeclaration.
    def enterClassMemberDeclaration(self, ctx:CSharpLexerParser.ClassMemberDeclarationContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#classMemberDeclaration.
    def exitClassMemberDeclaration(self, ctx:CSharpLexerParser.ClassMemberDeclarationContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:CSharpLexerParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:CSharpLexerParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#returnType.
    def enterReturnType(self, ctx:CSharpLexerParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#returnType.
    def exitReturnType(self, ctx:CSharpLexerParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#formalParameterList.
    def enterFormalParameterList(self, ctx:CSharpLexerParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#formalParameterList.
    def exitFormalParameterList(self, ctx:CSharpLexerParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#fixedParameters.
    def enterFixedParameters(self, ctx:CSharpLexerParser.FixedParametersContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#fixedParameters.
    def exitFixedParameters(self, ctx:CSharpLexerParser.FixedParametersContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#fixedParameter.
    def enterFixedParameter(self, ctx:CSharpLexerParser.FixedParameterContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#fixedParameter.
    def exitFixedParameter(self, ctx:CSharpLexerParser.FixedParameterContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#parameterModifier.
    def enterParameterModifier(self, ctx:CSharpLexerParser.ParameterModifierContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#parameterModifier.
    def exitParameterModifier(self, ctx:CSharpLexerParser.ParameterModifierContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#parameterArray.
    def enterParameterArray(self, ctx:CSharpLexerParser.ParameterArrayContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#parameterArray.
    def exitParameterArray(self, ctx:CSharpLexerParser.ParameterArrayContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#methodBody.
    def enterMethodBody(self, ctx:CSharpLexerParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#methodBody.
    def exitMethodBody(self, ctx:CSharpLexerParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#type.
    def enterType(self, ctx:CSharpLexerParser.TypeContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#type.
    def exitType(self, ctx:CSharpLexerParser.TypeContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#attributes.
    def enterAttributes(self, ctx:CSharpLexerParser.AttributesContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#attributes.
    def exitAttributes(self, ctx:CSharpLexerParser.AttributesContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#attributeSection.
    def enterAttributeSection(self, ctx:CSharpLexerParser.AttributeSectionContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#attributeSection.
    def exitAttributeSection(self, ctx:CSharpLexerParser.AttributeSectionContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#attributeList.
    def enterAttributeList(self, ctx:CSharpLexerParser.AttributeListContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#attributeList.
    def exitAttributeList(self, ctx:CSharpLexerParser.AttributeListContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#attribute.
    def enterAttribute(self, ctx:CSharpLexerParser.AttributeContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#attribute.
    def exitAttribute(self, ctx:CSharpLexerParser.AttributeContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#modifiers.
    def enterModifiers(self, ctx:CSharpLexerParser.ModifiersContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#modifiers.
    def exitModifiers(self, ctx:CSharpLexerParser.ModifiersContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#modifier.
    def enterModifier(self, ctx:CSharpLexerParser.ModifierContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#modifier.
    def exitModifier(self, ctx:CSharpLexerParser.ModifierContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#typeParameters.
    def enterTypeParameters(self, ctx:CSharpLexerParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#typeParameters.
    def exitTypeParameters(self, ctx:CSharpLexerParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#null_literal.
    def enterNull_literal(self, ctx:CSharpLexerParser.Null_literalContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#null_literal.
    def exitNull_literal(self, ctx:CSharpLexerParser.Null_literalContext):
        pass


    # Enter a parse tree produced by CSharpLexerParser#boolean_literal.
    def enterBoolean_literal(self, ctx:CSharpLexerParser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by CSharpLexerParser#boolean_literal.
    def exitBoolean_literal(self, ctx:CSharpLexerParser.Boolean_literalContext):
        pass



del CSharpLexerParser