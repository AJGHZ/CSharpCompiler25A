import antlr4
from antlr4 import *
from CSharpLexer import CSharpLexer
from CSharpLexerParser import CSharpLexerParser
from antlr4.Token import CommonToken
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import BailErrorStrategy


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
print('Analizador sintactico de C#')
print()

print('Este programa analiza un archivo de texto con código C# y genera una lista de tokens.')
print('Además, verifica la sintaxis del código y muestra errores si los encuentra.')
class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f'Error sintáctico: {msg}, en línea: {line}, columna: {column}')

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
    #parser._errHandler = BailErrorStrategy()

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

if __name__ == '__main__':
    main()