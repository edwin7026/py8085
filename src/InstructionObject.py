# Name: Edwin Joy
# email: edwin7026@gmail.com
# This file has the instrObject class

class instrObject:
    '''
    Holds all parameters consituting an instuction
    '''
    def __init__(self,
                instr_addr = None,
                label = None,
                func = None, 
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
        instr_addr: (int, hex) Address of the instruction in the memory
        label:      (string) Mnemonic label if any
        func:       (string) The functional part of the opcode
        rst:        (int 0-7) RST type
        psw:        (boolean) Pop/Push from/to PSW
        addr16:     (string) 16-bit address for the immediate addressing instructions
        opr_reg:    (string) Operand register for arithmetic instructions
        rd:         (string) Destination register
        rs:         (string) Source register
        imm:        (string) Immediate value in the instruction
        '''
        self.instr_addr = instr_addr
        self.label = label
        self.func = func
        self.rst = int(rst)
        self.psw = psw
        self.addr16 = int(addr16, 16)
        self.opr_reg = opr_reg
        self.rd = rd
        self.rs = rs
        self.imm = int(imm, 16)

    


