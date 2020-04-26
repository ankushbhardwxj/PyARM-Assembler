 ; Add two 16 bit numbers 
    TTL 16bitadd
    AREA program, CODE, READONLY
    ENTRY

Main
    LDR R1, Value1 ; Store value1 in register
    LDR R2, Value2 ; Store value2 in register
    ADD R1, R1, R2 ; Add values in registers 
    STR R1, Result ; Store value in new reg
    SWI &11  ; Interrupt

Value1 DCW &C123 ; assigned value
       ALIGN
Value2 DCW &02AA ; assigned value
         ALIGN
Result DCW 0  ; initialised result to 0
       END
