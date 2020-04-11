  TTL comparenum
  AREA Program, CODE, READONLY
  ENTRY


Main
  LDR R1, Value1
  LDR R2, Value2
  CMP R1, R2  ; Compare them
  BHI Done    ; if R1 contains highest
  MOV R1, R2  ; otherwise overwrite R1
Done
  STR R1, Result
  SWI &11

Value1 DCD &FEDCA987
Value2 DCD &12345678
Result DCD 0
       END
