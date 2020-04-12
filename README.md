## PyARM-Assembler 

Assembler for [ARM assembly language](http://www.toves.org/books/arm/).      

An assembler is just a simple program that is supposed to convert assembly code to 
machine code(binary).     
A linker may be further implemented for execution. 
Given an ARM7 assembly code to our assembler, we want it to spit binary.    
eg: 
```
MOV R3, R9   # assembly
1110 0001 1010 0000 0011 0000 0000 1001  # binary

``` 
An assembler has two passes, coz it skips certain lines in first pass.   
Read input line, parse the opcode, check for operands, addressing modes etc,   
get all 8 bits and write them to a object text file.       
This assembler, however, is an one pass assembler.    

### How to run ? 
```
python assembler.py -f fileName.s 
```
For debugging, set the `debug` variable in source equal to 1. 


#### Some material : 
- [ARM Assembly](http://www.toves.org/books/arm/): ARM assembly doc.
- [Assembler Steps](https://cseweb.ucsd.edu/classes/wi05/cse141L/assembler.html)
- see page [32](http://www.me:.sc.edu/courses/emch367/Download/programming.pdf)
- [Working](https://www.geeksforgeeks.org/introduction-of-assembler/)
- A [C](https://github.com/jlowe64/Assembly-Language-Parser/blob/master/asm.c) based assembly parser
- Standard Assembly [book](http://arantxa.ii.uam.es/~gdrivera/sed/docs/ARMBook.pdf)
- ARM7 [Instruction Set](https://iitd-plos.github.io/col718/ref/arm-instructionset.pdf)
- A good [resource](https://github.com/stephanh42/armasm/blob/2a03810a2235997daa14ce6efebb0d4acac2d2c9/armasm.py#L42)

#### Future Work 
- Make a 8051 version of this, preferably using Chapel Language.
