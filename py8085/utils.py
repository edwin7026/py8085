# Name: Edwin Joy
# email: edwin7026@gmail.com

# Utilities for file handling
# 1. Handle the assembly files written and upload into the Memory
# 2. Store metadata to return formatted Hex file
# 3. Dump Intel Hex file

from MnemonicParser import mnemoParser

def process_file(file_name):
    '''
    File processing method. Handles mnemonic files for initial processing

    Input Argument:
    file_name:  (string) Path to the assembly file
    '''
    
    mnemonic_list = []
    with open(file_name, encoding='utf-8') as fp:
        for line in fp:
            mnem_str = extract_line(line)
            mnemo_temp = mnemoParser(mnem_str)
            mnemonic_list.append(mnemo_temp)

        for obj in mnemonic_list:                   # For debug
            print(obj)
        
        print(mnemoParser.label_dict)

    print('File closed successfully')               # For debug

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


def dump_hex():
    '''
    Dump CPU instruction file in Intel Hex format
    '''
    # TODO


# For tests
if __name__ == '__main__':
    
    process_file('../tests/test1.S')