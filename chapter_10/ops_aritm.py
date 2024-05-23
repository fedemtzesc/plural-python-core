class Operaciones:
    
    def __init__(self):
        self._op1 = 0
        self._op2 = 0 
        self._op3 = 0 
        
    def __init__(self, op1, op2):
        self._op1 = op1
        self._op2 = op2 
        self._op3 = 0 
        
    def init_instance(self, op1, op2, op3):
        self._op1 = op1
        self._op2 = op2 
        self._op3 = op3
        
    def add_op(self, op3):
        self._op3 = op3
        
    def suma(self, all=False):
        if all:
            return self._op1 + self._op2 + self._op3
        else:
            return self._op1 + self._op2
        
    def resta(elf, all=False):
        if all:
            return self._op1 - self._op2 - self._op3
        else:
            return self._op1 - self._op2
        
    def multiplicacion(self, all=False):
        if all:
            return self._op1 * self._op2 * self._op3
        else:
            return self._op1 * self._op2
        
    
    if __name__ == 'main':
        o = Operaciones(1,2)
        print(o.suma())
        