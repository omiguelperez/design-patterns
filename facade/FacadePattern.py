class Scanner:
    def __init__(self):
        self.name = 'Scanner'

class Parser:
    def __init__(self):
        self.name = 'Parser'

class Compiler:
    def __init__(self):
        self.name = 'Compiler'
        self.scanner = Scanner()
        self.parser = Scanner()

    def compile(self):
        print('Compiling...')
        print("Scanning %s" % self.scanner.name)
        print("Parser %s" % self.parser.name)

compiler = Compiler()
compiler.compile()
