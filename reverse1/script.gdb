break *0x5555555552f4
run 'hk'
set logging overwrite on
set logging file gdb.bt
info registers $rax
