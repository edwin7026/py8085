# Name: Edwin Joy
# email: edwin7026@gmail.com
# This file has the instrObject class

# For github
# Remove labels

class instrObject:
    '''
    Holds all parameters consituting an instuction
    '''
    def __init__(self,
                instr_addr = None,
                func = None, 
                rst = None, 
                psw = None, 
                addr16 = None, 
                opr_reg = None, 
                rd = None, 
                rs = None, 
                reg_imm = None,
                imm = None):
        '''
        Initializer

        Arguments:
        instr_addr: (int, hex) Address of the instruction in the memory
        func:       (string) The functional part of the opcode
        rst:        (int 0-7) RST type
        psw:        (string) Pop/Push from/to PSW
        addr16:     (string) 16-bit address for the immediate addressing instructions
        opr_reg:    (string) Operand register for arithmetic instructions
        rd:         (string) Destination register
        rs:         (string) Source register
        imm:        (string) Immediate value in the instruction
        '''
        self.instr_addr = instr_addr
        self.func = func
        self.rst = int(rst) if rst != None else None
        self.psw = psw
        self.addr16 = int(addr16, 16) if addr16 != None else None
        self.opr_reg = opr_reg
        self.rd = rd
        self.rs = rs
        self.reg_imm = int(reg_imm, 16) if reg_imm != None else None
        self.imm = int(imm, 16) if imm != None else None
     
    def __str__(self):
        '''
        Overloading print function
        '''      
        code = '(' + str(hex(self.instr_addr)) + ') '
        if self.func:
            code = code + self.func + ' '
            if self.rst:
                code += str(self.rst)
            elif self.psw:
                code += self.psw
            elif self.addr16:
                code += str(hex(self.addr16))
            elif self.opr_reg:
                code += self.opr_reg
            elif self.rd:
                code += self.rd + ', '
                if self.rs:
                    code += self.rs
                elif self.reg_imm:
                    code += str(hex(self.reg_imm))
            elif self.imm:
                    code += str(hex(self.imm))
        else:
            return 'N/A'

        

    


