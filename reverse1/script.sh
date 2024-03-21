#!/bin/bash

foo="$1"

cat << EOF > script.gdb
break *0x5555555552f4
run '${foo}'
set logging overwrite on
set logging file gdb.bt
info registers \$rax
EOF

gdb crackme --command script.gdb > out &
sleep 0.1
kill `pgrep gdb` 2>/dev/null

reg=`tail -n 6 out | head -n 1 | awk '{print $2}'`

echo $reg
