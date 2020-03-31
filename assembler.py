import os
import argparse
import sys
"""
We can try to create the two phase assembler, 
but we will try something else first, since no 
theory of 2 phase has been found for ARM7. 
We will parse all opcodes, operands, addressmodes 
and store them in arrays and then think about 
converting each of them to machine code serially. 
"""
"""
**************** SOME FORMATS *************
_dpi_format = _InstructionFormat("Cond 0 0 I Opcode S Rn Rd Operand2")
_branch_format = _InstructionFormat("Cond 1 0 1 L Offset")
_bx_format = _InstructionFormat("Cond 0 0 0 1 0 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 L 1 Rm")
_load_store_format = _InstructionFormat("Cond 0 1 I P U B W L Rn Rd Operand2")
_load_store_multi_format = _InstructionFormat("Cond 1 0 0 P U S W L Rn RegisterList")
_mul_format = _InstructionFormat("Cond 0 0 0 0 0 0 0 S Rd 0 0 0 0 Rs 1 0 0 1 Rm")
_mla_format = _InstructionFormat("Cond 0 0 0 0 0 0 1 S Rd Rn Rs 1 0 0 1 Rm")
_clz_format = _InstructionFormat("Cond 0 0 0 1 0 1 1 0 1 1 1 1 Rd 1 1 1 1 0 0 0 1 Rm")
_mrs_format = _InstructionFormat("Cond 0 0 0 1 0 R 0 0 1 1 1 1 Rd 0 0 0 0 0 0 0 0 0 0 0 0")
_msr_format_reg = _InstructionFormat("Cond 0 0 0 1 0 R 1 0 f s x c 1 1 1 1 0 0 0 0 0 0 0 0 Rm")
_msr_format_imm = _InstructionFormat("Cond 0 0 1 1 0 R 1 0 f s x c 1 1 1 1 Operand2")
_swi_format = _InstructionFormat("Cond 1 1 1 1 Imm24")

"""

opcode = []
labels = []
operands = []
instructions = []

conditions = [
 "EQ", "NE", "CS", "CC",
 "MI", "PL", "VS", "VC",
 "HI", "LS", "GE", "LT",
 "GT", "LE", "AL"]
 
data_proc = {
"AND":0000,
"EOR":0001,
"SUB":0010,
"RSB":0011, 
"ADD":0100,
"ADC":0101,
"SBC":0110,
"RSC":0111,
"TST":1000,
"TEQ":1001,
"CMP":1010,
"CMN":1011, 
"ORR":1100,
"MOV":1101, 
"BIC":1110, 
"MVN":1111
}

instruction_format = {
  "0" : 1,
  "1" : 1,
  "A" : 1,
  "B" : 1,
  "c" : 1,
  "x" : 1,
  "s" : 1,
  "f" : 1,
  "CPNum" : 4,
  "CRd" : 4,
  "CRm" : 4,
  "CRn" : 4,
  "Cond" : 4,
  "H" : 1,
  "I" : 1,
  "Imm24" : 24,
  "L" : 1,
  "N" : 1,
  "Offset" : 0,
  "Offset1" : 4,
  "Offset2" : 4,
  "Op1" : 0,
  "Op2" : 3,
  "Opcode" : 4,
  "Operand2" : 12,
  "P" : 1,
  "Rd" : 4,
  "RdHi" : 4,
  "RdLo" : 4,
  "RegisterList" : 16,
  "R" : 1,
  "Rm" : 4,
  "Rn" : 4,
  "Rs" : 4,
  "S" : 1,
  "Shift" : 3,
  "U" : 1,
  "W" : 1,
}


 

def parse_dpi(line, lineNumber): 
  print "Parsing for dpi" 

def parse_condition(line,lineNumber):
  print "Parsing for conditions"

def parseFile(f): 
  # read each file and get each line
  if os.access(f, os.R_OK):
    with open(f) as fp: 
      file = fp.read()
  lineNumber = 0
  file = file.split('\n') 
  for line in file: 
    lineNumber += 1
    line = line.split(';')
    line = line[0]
    # start parsing line by line from here 
    # match line with instructions here 
    # look for condition
    for ins in line: 
      print ins
    for instruction in line: 
      for cond in conditions:
        if instruction == cond:
          parse_condition(line,lineNumber)
    # look for data processing instructions
    for instruction in line: 
      for dpi in data_proc: 
        if instruction == dpi: 
          parse_dpi(line,lineNumber)     
    
def getfile(f):
  print "getting file",f 
  # check if file is present
  path = os.path
  if path.exists(f): 
    parseFile(f)  
    checkLoops()
  else :
    print "File Not Found!"

if __name__ == "__main__":
  # get file from current path
  # start parsing line by line
  # we want to generate 8 bits
  # write generated bits to newfile
  print "Assembler running..." 
  flag = sys.argv[1] 
  fileName = sys.argv[2]
  if flag == "-f": 
    getfile(fileName)

