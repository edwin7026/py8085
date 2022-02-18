# Name: Edwin Joy
# email: edwin7026@gmail.com
# This file has the instrObject class

class instrObject:
    '''
    Holds all parameters consituting an instuction
    '''
    def __init__(self, 
                func, 
                rst = None, 
                psw = None, 
                addr16 = None, 
                opr_reg = None, 
                rd = None, 
                rs = None, 
                imm = None):
        '''
        Initializer

        Arguments:
        func:   (string) The functional part of the opcode
        rst:    (int 0-7) RST type
        psw:    (boolean) Pop/Push from/to PSW
        addr16: (string) 16-bit address for the immediate addressing instructions
        opr_reg: (string) Operand register for arithmetic instructions
        rd:     (string) Destination register
        rs:     (string) Source register
        imm:    (string) Immediate value in the instruction
        '''
        self.func = func
        self.rst = rst
        self.psw = psw
        self.addr16 = addr16
        self.opr_reg = opr_reg
        self.rd = rd
        self.rs = rs
        self.imm = imm
    

    


