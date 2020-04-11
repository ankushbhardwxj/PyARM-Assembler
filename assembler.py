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

labels = []
operands = []
registers = []

conditions = [
 "EQ", "NE", "CS", "CC",
 "MI", "PL", "VS", "VC",
 "HI", "LS", "GE", "LT",
 "GT", "LE"]
 
data_proc = {
"AND":"0000",
"EOR":"0001",
"SUB":"0010",
"RSB":"0011", 
"ADD":"0100",
"ADC":"0101",
"SBC":"0110",
"RSC":"0111",
"TST":"1000",
"TEQ":"1001",
"CMP":"1010",
"CMN":"1011", 
"ORR":"1100",
"MOV":"1101", 
"BIC":"1110", 
"MVN":"1111"
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
single_data_transfer = {
"LDR": 1, "STR":0
}
software_interrupt = {
 "SWI": 0, "SVC": 1,
}
"""
move_instructions = {
"MOV":13,
"MVN":15
}
"""
"""
def parse_move(line, lineNumber):
  print "Parsing move", line
"""
def parse_branch(line, ins, lineNumber): 
  

def parse_swp(line, ins, lineNumber):
  print "Parsing swap", line

def parse_swi(line,lineNumber): 
  # TODO add condition bits - default as 0000
  line = line.strip()
  line = line.split(" ")
  inte = line[0] 
  val = line[1]
  val = bin(int(val.replace("&","").lower(),16))
  binary = "0000"+"1111"+str(val)
  createBinaryFile(binary)

def checkIfLabel(reg):
  for keys in labels: 
    k = keys.get(reg)
    if k != None:
      return k 

def createBinaryFile(binary):
  f = open("binary.obj","a")
  f.write(binary)
  f.close()

def parse_sdt(line, lineNumber): 
  # specifically LDR and STR 
  line = line.strip();
  line = line.split(" ")
  sdt = line[0]
  if sdt == "LDR": 
    L = 1
  else: 
    L = 0
  if L == 1: 
    source_reg = line[1].strip(',')
    # check if source_reg can be converted to binary else use 00000000 
    base_reg = line[2] 
    bit = single_data_transfer[line[0]]
    # check if base_reg is label, if label then get value
    # print bin(int(x.get(base_reg).replace("&","").lower(),16)).zfill(8)
    new_base_reg = checkIfLabel(base_reg)
    if new_base_reg != None:
      for x in range(len(line)): 
        if line[x] == base_reg:
          line[x] = new_base_reg
    # write this instruction to file 
    # TODO: Add support for checking condition & offset, default 0000
    try: 
      new_base_reg_bin = str(bin(int(new_base_reg.replace("&","").lower(),16)))
      binary = "0000"+"01"+"0"+"0"+"0"+"1"+new_base_reg_bin+"00000000"
      createBinaryFile(binary)
      registers.append({source_reg : new_base_reg_bin}) 
    except: 
      print "Syntax Error. Unable to parse label" 
    # save reference of new_base_reg and source_reg which will be used later 
  else: 
    print "SDT is STR"
  
def parse_dpi(line, lineNumber): 
  # TODO Add support for checking condition & offset, default 0000
  line =  line.strip()
  line = line.split(" ")
  opcode = line[0]
  # convert opcode to its binary 
  for proc in data_proc: 
    if opcode == proc: 
      opcode = data_proc[proc]
  # get value of registers from array
  if len(line) > 3:
    source_reg = line[1]
    source_reg = source_reg.split(",")[0]
    dest_reg = line[2]
    dest_reg = dest_reg.split(",")[0] 
    operand_reg = line[3]
  else: 
    source_reg = line[1].split(",")[0]
    operand_reg = line[2].split(",")[0]
    dest_reg = '' 
  for reg in registers:
    for k,v in reg.items(): 
      if k == dest_reg: 
        dest_reg = v
      if k == operand_reg: 
        operand_reg = v

  binary = "0000"+"00"+"0"+opcode+"1"+operand_reg+dest_reg
  createBinaryFile(binary)

def parse_condition(line,lineNumber):
  """
  different types of conditions have different
  number of bits in them which is denoted by their idx
  """
def parse_label(line, lineNumber):
  try: 
    line = line.strip()
    line = line.split(" ")
    label_name = line[0] 
    command = line[1]
    value = line[2]
    labels.append({label_name : value})
   # print labels
  except: 
    print "Syntax Error! Cannot parse label due to spaces in line "+ lineNumber
    print "Tip: Replace spaces with tabs in source" 

def parseFile(f): 
  # read each file and get each line
  if os.access(f, os.R_OK):
    with open(f) as fp: 
      file = fp.read()
  lineNumber = 0
  lineOfLabels = 0
  file = file.split('\n') 
  for line in file: 
    lineOfLabels += 1
    line = line.split(';')
    line = line[0] 
    # parse label and push instruction to label array
    label = ["DCW","DCD"]
    for lbl in label:
      if lbl in line: 
       # print lbl, line
        parse_label(line,lineNumber)
  # second loop for !label
  lineNumber += lineOfLabels 
  for line in file: 
    lineNumber += 1
    line = line.split(';')
    line = line[0]
    # look for condition
    for cond in conditions:
      if cond in line:
        parse_condition(line,lineNumber)
    # look for data processing instructions
    for dpi in data_proc: 
      if dpi in line:
        parse_dpi(line, lineNumber)
    # look for single data transfer instructions
    for sdt in single_data_transfer: 
      if sdt in line:
        parse_sdt(line, lineNumber) 
    # look for interrupts
    for swi in software_interrupt: 
      if swi in line: 
        parse_swi(line, lineNumber)   
    # look for branches B, BL, BLX(branch-line-exchnge) 
    for _i in range(len(conditions)): 
      ins = "B" + conditions[_i]
      if ins in line: 
        parse_branch(line, ins, lineNumber)
      ins = "BL" + conditions[_i]
      if ins in line:   
        parse_branch(line, ins, lineNumber)
      ins = "BLX" + conditions[_i]
      if ins in line:
        parse_branch(line, ins, lineNumber)     
    # look for single data swap
    ins = "SWP" 
    if ins in line: 
       parse_swp(line, ins, lineNumber)  
"""   
 # look for move instruction
    for mv in move_instructions:
      if mv in line: 
        parse_move(line,lineNumber)      
"""

debug = 0;
def showDebug(): 
  print "*** LABEL ***"
  for label in labels: 
    print label
  print "*** REGISTERS ***"
  for reg in registers:
    print reg
  print "*** OPERANDS ***"
  for op in operands: 
    print op

def getfile(f):
  print "getting file",f 
  # check if file is present
  path = os.path
  if path.exists(f): 
    try: 
      parseFile(f) 
      if debug == 1: 
        showDebug() 
      print "Binary File 'binary.obj' has been created"
      # checkLoops()
    except:
      if debug == 1: 
        showDebug()
      print "Stopped Parsing! Unknown ARM syntax."
  else:
    print "File Not Found!"


if __name__ == "__main__":
  # get file from current path
  # start parsing line by line
  # we want to generate 8 bits
  # write generated bits to newfile
  print "Assembler running..." 
  try: 
    flag = sys.argv[1] 
    fileName = sys.argv[2]
    if flag == "-f": 
      getfile(fileName)
  except: 
    print "Type python assembler.py -f <fileName>.s"
