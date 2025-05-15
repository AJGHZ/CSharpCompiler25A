import antlr4
from antlr4 import *
from CSharpLexer import CSharpLexer
from CSharpLexerParser import CSharpLexerParser
from antlr4.Token import CommonToken
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import BailErrorStrategy
from CSharpLexerVisitor import CSharpLexerVisitor

from ast_builder import ASTBuilder
from semantic_analyzer import SemanticAnalyzer
from ast_nodes import *
from TACGen import TACGenerator


print('#####################################################')
print('CENTRO UNIVERSITARIO DE TONALÁ')
print('UNIVERSIDAD DE GUADALAJARA')
print('Ingenieria en ciencias computacionales')
print('TRADUCTORES DE LENGUAJES I')
print('MAESTRO: RIGOBERTO CARDENAS LARIOS')
print('Creadores de este proyecto:')
print('Fuentes Tinajero, Eduardo.')
print('Garcia Hernandez, Aldo Josue.')
print('Velazquez Mateos, Edgar Ivan.')
print('#####################################################')
print()
print('Compilador de C#')
print()
print()
print('Este programa analiza un archivo de texto con código C# y genera una lista de tokens.')
print('Además, verifica la sintaxis del código y muestra errores si los encuentra.')
print()
class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f'Error sintáctico: {msg}, en línea: {line}, columna: {column}')

def imprimir_tokens(token_stream):
    print("\nTokens generados:")
    token_stream.fill()
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            print(f"Token: {token.text}, Tipo: {token.type}")

def imprimir_errores_sintacticos(error_listener):
    if error_listener.errors:
        for error in error_listener.errors:
            print(error)
        return True
    return False

def imprimir_errores_semanticos(semantic_errors):
    if semantic_errors:
        print("\nErrores semánticos detectados:")
        for err in semantic_errors:
            print(err)
    else:
        print("Análisis semántico exitoso. No se encontraron errores.")

def imprimir_tabla_simbolos(symbol_table):
    print("\nTabla de símbolos:")
    for name, info in symbol_table.items():
        print(f"  {name} -> tipo: {info['type']}, línea: {info['line']}, columna: {info['column']}")

def imprimir_nodos_ast(ast, nivel=0):
    indent = "  " * nivel
    if hasattr(ast, 'type'):
        print(f"{indent}{ast.__class__.__name__} (tipo: {ast.type})")
    else:
        print(f"{indent}{ast.__class__.__name__}")
    for attr in vars(ast).values():
        if isinstance(attr, list):
            for item in attr:
                if hasattr(item, '__class__') and not isinstance(item, str):
                    imprimir_nodos_ast(item, nivel + 1)
        elif hasattr(attr, '__class__') and not isinstance(attr, str):
            imprimir_nodos_ast(attr, nivel + 1)

def main():
    # Leer el archivo de prueba
    input_stream = FileStream("test.cs", encoding="utf-8")
    # Crear lexer y stream de tokens
    lexer = CSharpLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Imprimir los tokens generados antes del análisis sintáctico
    tokens = []
    while True:
        token = lexer.nextToken()
        if token.type == Token.EOF:
            break
        tokens.append(f'Token: {token.text}, Tipo: {token.type}')

    print("\nTokens generados:")
    print("\n".join(tokens))

    # Crear parser y configurar estrategias de error
    parser = CSharpLexerParser(stream)
    parser.removeErrorListeners()
    error_listener = SyntaxErrorListener()
    parser.addErrorListener(error_listener)

    # Activar BailErrorStrategy para depuración rápida
    parser._errHandler = BailErrorStrategy()

    # Iniciar análisis sintáctico con la regla de inicio
    print("\nIniciando análisis sintáctico...")
    try:
        tree = parser.prog()  # Cambia 'prog' por la regla de inicio de tu gramática
        if error_listener.errors:
            for error in error_listener.errors:
                print(error)
        else:
            print("El análisis sintáctico fue exitoso. Todas las declaraciones son válidas.")
    except Exception as e:
        print(f"Se produjo un error: {str(e)}")

    tree = parser.prog()  # Cambia 'prog' por la regla de inicio de tu gramática

    builder = ASTBuilder()
    ast = builder.visit(tree)
    print("\nÁrbol de sintaxis abstracta (AST):")
    print(ast)  # Imprime el AST generado

    # Crear un analizador semántico y analizar el AST
    analyzer = SemanticAnalyzer()
    errors = analyzer.analyze(ast)

    if errors:
        print("\nErrores semánticos encontrados:")
        for e in errors:
            print(' -', e)
    else:
        print("\nNo se encontraron errores semánticos.")

     # Generación de código de tres direcciones (TAC)
    TACGen = TACGenerator()
    TACGen.generate(ast)

    # Imprimir el TAC generado
    print("Código de Tres Direcciones (TAC):")
    print(TACGen.get_code())


if __name__ == '__main__':
    main()