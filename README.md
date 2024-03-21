## Task-based

#### pwn 1
для получения флага нужно вызвать функцию `win`. мы можем вставлять в format string в `prinf` любую строку; используя эту уязвимость, перезаписываем адрес функции `exit`(которая вызывается в конце программы) на адрес функции `win` в GOT(Global Offset Table). таким образом, при вызове `exit` будет на самом деле вызываться `win`. используя возможности `pwntools`, эксплойт создаётся в одну строчку:
```python
payload = fmtstr_payload(6, {elf.got["exit"]: elf.symbols["win"]})
```

Полный эксплойт: [expoit.py](pwn1/exploit.py)


#### pwn 2
данная программа полностью совпадает с заданием на [очень популярном учебнике по pwnу](https://ir0nstone.gitbook.io/notes/types/stack/syscalls/sigreturn-oriented-programming-srop/using-srop). эксплойт полностью совпадает с предложенным автором учебника, только нужно заменить адрес строки `/bin/bash`(его можно найти используя `gdb`):
```python
BINSH = elf.address + 0x1430
```

для поиска `/bin/bash` в `gdb`:
```python
info proc mappings # берем адресс первого исполняемого блока
find <addr>, +0x1000, "/bin/bash"
```

Полный эксплойт: [exploit.py](pwn2/exploit.py)