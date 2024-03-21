break *0x5555555552f4
run 'mX'
set logging overwrite on
set logging file gdb.bt
info registers rax
