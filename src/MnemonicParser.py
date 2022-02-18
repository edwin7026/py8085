# Name: Edwin Joy
# email: edwin7026@gmail.com
# This file contains the menmoParser class

import re
from InstructionObject import instrObject

class mnemoParser:
    '''
    This class parse the mnemonic given as input
    '''

    def __init__(self):
        '''
        Initializes and compiles the regular expression for parsing the mnemonic
        code
        ''' 

        self.mnemonic_pattern = r'''
        ^                                                           # Beginning of string
        \s*
        ((?P<label>\D[A-Za-z0-9]+)\s*:)?                            # Handle labels
        (
            \s*
            (?P<func>[A-Z]{1,4})                                    # Mnemonic function
            \s*
            (
                \s+
                (
                    (?P<reset>[0-7])|                               # RST Operations
                    (?P<psw>(PSW))|                                 # Push or pop to/from PSW
                    0x(?P<addr16>[0-9abcdef]{1,4})|                 # 16-bit address
                    (?P<opr_reg>[ABCDEHLM])|                        # Operand register
                    (
                        (?P<rd>[ABCDEHLM])                          # Destination register
                        \s*?,\s*?                                   # Commas and Optional spaces
                        (
                            (?P<rs>[ABCDEHLM])|                     # Source register 
                            (?P<imm>[0-9abcdef]{2})                 # Immediate value
                        )
                    )
                )                                                   # Arguments to func is optional
            )?
        )?
        \s*
        $                                                           # End of string
        '''
        self.mnemonic_re = re.compile(self.mnemonic_pattern, re.VERBOSE)
        
    def process(self, line):
        '''
        Parses the line of code and builds an instance of instrObject class from the parsed 
        info

        Arguments:
            line:   (string) Line of code to be parsed
        
        Returns:
            (instrObject) containing the necessary properties of the line of mnemonic code
        '''
        
        instr_pattern = self.mnemonic_re
        re_search = instr_pattern.search(line)
        if re_search is not None:
            label = re_search.group('label')
            func = re_search.group('func')
            rst = re_search.group('reset')
            psw = True if re_search.group('psw') else False
            addr16 = re_search.group('addr16')
            opr_reg = re_search.group('opr_reg')
            rd = re_search.group('rd')
            rs = re_search.group('rs')
            imm = re_search.group('imm')
            instr_obj = instrObject(None, label, func, rst, psw, addr16, opr_reg, rd, rs, imm)
            return instr_obj

# Test code
if __name__ == '__main__':
    parsed = mnemoParser()
    print(parsed.process('ADD A, B'))