# Name: Edwin Joy
# email: edwin7026@gmail.com

from py8085.InstructionObject import instrObject
from py8085.MnemonicParser import mnemoParser

class assembler:

    REG = {
        'A'     : '111',
        'B'     : '000',
        'C'     : '001',
        'D'     : '010',
        'E'     : '011',
        'H'     : '100',
        'L'     : '101',
        'M'     : '110'
    }

    REG_PAIR = {
        'B'     : '00',
        'D'     : '01',
        'H'     : '10',
        'SP'    : '11',
    }
    
    CONDITION = {
        'NZ'    : '000',
        'Z'     : '001',
        'NC'    : '010',
        'C'     : '011',
        'PO'    : '100',
        'PE'    : '101',
        'P'     : '110',
        'M'     : '111'
    }

    OP_CODES = {
        # Data Transfer group
        'MOV'   : '01',
        'MVI'   : '00',
        'LXI'   : '00',
        
        'LDA'   : '00111010',
        'STA'   : '00110010',
        'LHLD'  : '00101010',
        'SHLD'  : '00100010',
        
        'LDAX'  : '00',
        'STAX'  : '00',
        
        'XCHG'  : '11101011',

        # Arithmetric Group
        'ADD'   : '10000',
        'ADI'   : '11000',
        'ADC'   : '10001',
        'ACI'   : '11001',
        'SUB'   : '10010',
        'SUB'   : '10010',
        'SUI'   : '11010',
        'SBB'   : '10011',
        'SBI'   : '11011',
        
        'INR'   : '00',              # Special instr with '100' as prefix
        'DCR'   : '00',              # Special instr with '101' as prefix
        'INX'   : '00',
        'DCX'   : '00',
        'DAD'   : '00',
        'DAA'   : '00100111',

        # Logical Group
        'ANA'   : '10100',
        'ANI'   : '11100',
        'XRA'   : '10101',
        'XRI'   : '11101',
        'ORA'   : '10110',
        'ORI'   : '11110',
        'CMP'   : '10111',
        'CPI'   : '11111',
        'RLC'   : '00000111',
        'RRC'   : '00001111',
        'RAL'   : '00010111',
        'RAR'   : '00011111',
        'CMA'   : '00101111',
        'CMC'   : '00111111',
        'STC'   : '00110111',

        # Branch Group
        # J Condition
        'JMP'   : '11000011',
        'JC'    : '11011010',   
        'JM'    : '11111010',
        'JNC'   : '11010010',
        'JNZ'   : '11000010',
        'JP'    : '11110010',
        'JPE'   : '11101010',
        'JPO'   : '11100010',
        'JZ'    : '11001010',
        
        # C Condition
        'CALL'  : '11001101',
        'CC'    : '11011100',
        'CM'    : '11111100',
        'CNC'   : '11010100',
        'CNZ'   : '11000100',
        'CP'    : '11110100',
        'CPE'   : '11101100',
        'CPO'   : '11100100',
        'CZ'    : '11001100',
        
        # R condition
        'RET'   : '11001001',
        'RC'    : '11011000',
        'RM'    : '11111000',
        'RNC'   : '11010000',
        'RNZ'   : '11000000',
        'RP'    : '11110000',
        'RPE'   : '11101000',
        'RPO'   : '11100000',
        'RZ'    : '11001000',
        
        'RST'   : '11',
        'PCHL'  : '11101001',

        # Stack, I/O and Machine Control Group
        'PUSH'  : '11',
        'POP'   : '11',
        'XTHL'  : '11100011',
        'SPHL'  : '11111001',
        'IN'    : '11011011',
        'OUT'   : '11010011',

        'EI'    : '11111011',
        'DI'    : '11110011',
        'HLT'   : '01110110',
        'NOP'   : '00000000',
        

        # Interrupt stuffs
        'RIM' : '00100000',
        'SIM' : '00110000'

    }

    # Suffixes if any
    OP_CODES_SUFFIX = {
        'LXI' : '0001',
        'DAD' : '1001',
        'DCR' : '101',
        'DCX' : '1011',
        'INR' : '100',
        'INX' : '0011',
        'LDAX': '1010',
        'STAX': '0010',
        'POP' : '0001',
        'PUSH': '0101',
        'RST' : '111'
    }

    hex_code_list = []

    def __init__(self, instr_obj: instrObject):

        hex_code = ''
        if instr_obj.func:
            hex_code += assembler.OP_CODES[instr_obj.func]
            if len(hex_code) != 8:
                if instr_obj.addr16:
                    hex_code += '010'
                elif instr_obj.rd:
                    hex_code += assembler.REG[instr_obj.rd]
                    if instr_obj.rs:
                        hex_code += assembler.REG[instr_obj.rs]
                    elif instr_obj.reg_imm:
                        hex_code += '110'
                elif instr_obj.imm:
                    hex_code += '110'
                elif instr_obj.opr_reg:
                    if len(hex_code) == 2:
                        suffix = assembler.OP_CODES_SUFFIX[instr_obj.func]
                        if len(suffix) == 4:
                            hex_code += assembler.REG_PAIR[instr_obj.opr_reg]
                            hex_code += suffix
                        else:
                            hex_code += assembler.REG[instr_obj.opr_reg]
                            hex_code += suffix
                    else:    
                        hex_code += assembler.REG[instr_obj.opr_reg]
                elif instr_obj.psw:
                    suffix = assembler.OP_CODES_SUFFIX[instr_obj.func]
                    hex_code += '11'
                    hex_code += suffix
                elif instr_obj.rst is not None:
                    suffix = assembler.OP_CODES_SUFFIX[instr_obj.func]
                    hex_code += format(instr_obj.rst, '#05b')[2:]
                    hex_code += suffix
        
        self.hex_code = hex_code

    def get_hex_code(self):
        return hex(int(self.hex_code, 2))