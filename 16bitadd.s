 # Add two 16 bit numbers 
    TTL 16bitadd
    AREA program, CODE, READONLY
    ENTRY

Main
    LDR R1, Value1
    LDR R2, Value2
    ADD R1, R1, R2
    STR R1, Result
    SWI &11

Value1   DCW &C123
         ALIGN
Value2   DCW &02AA
         ALIGN
Result   DCW 0
         END
