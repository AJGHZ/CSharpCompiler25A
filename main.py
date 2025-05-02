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

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f'Error sintactico: {msg}, en linea: {line}, Columna: {column}')

def main():
    InputStream = antlr4.FileStream("test.txt")
    lexer = CSharpLexer(InputStream)
    stream = CommonTokenStream(lexer)
    parser = CSharpLexerParser(stream)
    parser.removeErrorListeners()
    errorListener = SyntaxErrorListener()
    parser.addErrorListener(errorListener)
    #parser.error = BailErrorStrategy()

    tree = parser.prog()

    print(open("test.txt").read())
    print()

    print("Iniciando análisis sintáctico...")

    if errorListener.errors:
        for error in errorListener.errors:
            print(error)
    else:
        print("El análisis sintáctico fue exitoso. Todas las declaraciones son válidas.")

if __name__ == '__main__':
    main()