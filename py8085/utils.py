# Name: Edwin Joy
# email: edwin7026@gmail.com

# Utilities for file handling
# 1. Handle the assembly files written and upload into the Memory
# 2. Store metadata to return formatted Hex file
# 3. Dump Intel Hex file

from MnemonicParser import mnemoParser
from log import logger
import logging

mnemonic_list = []

def extract_line(line):
    '''
    Extract relevant information from a line

    Input argument
    line:   (string) A line in the file

    Output argument:
    (None)      Maybe a comment or empty line
    (string)    A string of mnemonic
    '''
    if line.strip(' \t') == '\n':                   # Empty line
        return None
    split_line = line.split('#')                    # Check for comments
    if len(split_line) == 2:
        if split_line[0] == '':                     # Full line comment
            return None
        else:
            return split_line[0]
    else:
       return split_line[0]


def process_file(file_name):
    '''
    File processing method. Handles mnemonic files for initial processing

    Input Argument:
    file_name:  (string) Path to the assembly file
    '''
    
    with open(file_name, encoding='utf-8') as fp:
        for line in fp:
            mnem_str = extract_line(line)
            mnemo_temp = mnemoParser(mnem_str)
            mnemonic_list.append(mnemo_temp)

def get_all_instr_obj(list = mnemonic_list):
    '''
    Extract instrObj objects from all mnemonic objects

    Input arguments:
    mnemonic_list:  (list) A list of all the mnemonic objects from the file
    
    Return
    list:           A list of instrObj for corresponding instructions

    '''
    
    instr_obj_list = []
    for mnem in mnemonic_list:
        instr_obj = mnem.get_instr_obj()
        if instr_obj:
            instr_obj_list.append(instr_obj)
    
    return instr_obj_list
        
def print_all_mnemonics(list = mnemonic_list):
    for mnem in list:
        print(mnem)


def dump_hex(instr_obj_list):
    '''
    Dump CPU instruction file in Intel Hex format

    Input arguments:
    

    '''
    # TODO