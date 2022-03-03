# Name: Edwin Joy
# email: edwin7026@gmail.com

from py8085.Assembler import assembler
from py8085.MnemonicParser import mnemoParser
import unittest
import sys

class assembler_test(unittest.TestCase):
    
    known_values_dict = {}
        
    def test_assembler(self):
        '''
        Generate test bench dictionary
        '''
        test_line = ''
        with open('test_bench.testfile', encoding='utf-8') as fp:
            for line in fp:        
                if line.strip(' \t') == '\n':                       # Empty line
                    continue
                split_line = line.split('#')                        # Check for comments
                if len(split_line) == 2:
                    if split_line[0].strip(' \t') == '':            # Full line comment
                        continue
                    else:
                        test_line = split_line[0]
                else:
                    test_line = split_line[0]

                temp = test_line.split(':')
                mnem = temp[0].strip(' \t')
                hex_code = temp[1].strip(' \t\n')
                
                assembler_test.known_values_dict[mnem] = hex_code

        mnemoParser('main: 0x0000')                                 # Initialize the address
        for op_code in assembler_test.known_values_dict:
            temp_instr_obj = mnemoParser(op_code).get_instr_object()
            assembler_hex_code = assembler(temp_instr_obj).get_hex_code()

            ref_hex_code = hex(int(assembler_test.known_values_dict[op_code], 16))

            print('Checking instruction: {0}\t\t:{1}'.format(op_code, assembler_hex_code), end='')
            try:
                self.assertEqual(assembler_hex_code, ref_hex_code)
            except:
                print('\nTest failed: Instruction: {}'.format(op_code))
                sys.exit()
            print('\tPassed!')

if __name__ == '__main__':
    unittest.main()