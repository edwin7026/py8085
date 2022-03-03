# Name: Edwin Joy
# email: edwin7026@gmail.com

from py8085.Assembler import assembler
from py8085 import utils
#from Assembler import assembler

# For tests
if __name__ == '__main__':
    
    utils.process_file('../tests/test1.S')
    #utils.print_all_mnemonics()
    
    instr_list = utils.get_all_instr_obj()
    for obj in instr_list:
        #print(obj)
        assm = assembler(obj)
        print(assm.get_hex_code())