## PyARM-Assembler 

Assembler for [ARM assembly language](http://www.toves.org/books/arm/).      

An assembler is just a simple program that is supposed to convert assembly code to 
machine code(binary).     
A linker may be further implemented for execution. 
Given an assembly code to our assembler, we want it to spit binary.    
eg: 
```
MOV R3, R9   # assembly
1110 0001 1010 0000 0011 0000 0000 1001  # binary

``` 
An assembler has two passes, coz it skips certain lines in first pass.   
Read input line, parse the opcode, check for operands, addressing modes etc,   
get all 8 bits and write them to a object text file.  



#### Some material : 
- [ARM Assembly](http://www.toves.org/books/arm/): ARM assembly doc.
- [Assembler Steps](https://cseweb.ucsd.edu/classes/wi05/cse141L/assembler.html)
- see page [32] (http://www.me:.sc.edu/courses/emch367/Download/programming.pdf)
- [Working](https://www.geeksforgeeks.org/introduction-of-assembler/)
- A [C](https://github.com/jlowe64/Assembly-Language-Parser/blob/master/asm.c) based assembly parser
- Standard Assembly [book](http://arantxa.ii.uam.es/~gdrivera/sed/docs/ARMBook.pdf)

#### Open questions: 
- Will this support 8051 microcontroller?
- 8051 is 8 bit Von Neumann arch, and ARM is 32 bit Modified Harvard arch. What    
  difference would that make ? 
