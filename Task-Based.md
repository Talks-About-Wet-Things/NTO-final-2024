## Task-based

### pwn 1
для получения флага нужно вызвать функцию `win`. мы можем вставлять в format string в `prinf` любую строку; используя эту уязвимость, перезаписываем адрес функции `exit`(которая вызывается в конце программы) на адрес функции `win` в GOT(Global Offset Table). таким образом, при вызове `exit` будет на самом деле вызываться `win`. используя возможности `pwntools`, эксплойт создаётся в одну строчку:
```python
payload = fmtstr_payload(6, {elf.got["exit"]: elf.symbols["win"]})
```

полный эксплойт: [expoit.py](pwn1/exploit.py)

флаг: `nto{easy_formt_string}`


### pwn 2
данная программа полностью совпадает с заданием на [очень популярном учебнике по pwnу](https://ir0nstone.gitbook.io/notes/types/stack/syscalls/sigreturn-oriented-programming-srop/using-srop). эксплойт полностью совпадает с предложенным автором учебника, только нужно заменить адрес строки `/bin/bash`(его можно найти используя `gdb`):
```python
BINSH = elf.address + 0x1430
```

для поиска `/bin/bash` в `gdb`:
```python
info proc mappings # берем адресс первого исполняемого блока
find <addr>, +0x1000, "/bin/bash"
```

полный эксплойт: [exploit.py](pwn2/exploit.py)

флаг: `nto{sropsropsroplazy}`


### web 1
простейшая lfi. в коде страницы видим ссылку вида `http://192.168.12.10:5001/download?file_type=file1.txt`. как раз в `file1.txt` написано, что флаг в `/etc/secret`. делаем запрос `http://192.168.12.10:5001/download?file_type=../../../../../../etc/secret`

флаг: `nto{P6t9_T77v6RsA1}`


### web 2
Декомпилим с помощью jadx файл с веб приложением, смотрим на код и видим что используются `Spring` и `Thymeleaf`, являющийся шаблонизатором. Ищем `SSTI`, находим, что можно использовать препроцессор в `__${}__`, а так же подставлять вывод, а-ля echo, используя в конце `::..`. Находим эндпоинт `/doc`, который как раз принимается шаблонизатором, пишем туда 
```java
__${new java.util.Scanner(T(java.langRuntime).getRuntime().exec('cat<password.txt').getInputStream()).next()}__::..
```
Отправляем запрос и в ответ значение команды из пейлоада подставляется в значение ошибки ненайденного шаблона, отсюда мы узнаем пароль, далее по этому паролю заходим и получаем флаг.


### web 3
Приложение использует `haproxy`, который не пускает на страницу с флагом, ищем, как обойти и подставляем для этого в путь еще один `/` (`//flag`). Далее можно использовать `SSTI` в `jinja`, чтобы через `RCE` прочитать флаг:
```python
//flag?name={{self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}
```

флаг: `nto{Ht1P_sM088Lin6_88Ti}`


### reverse 1
в программе есть массив с зашифрованным флагом. программа сравнивает зашифрованные пары символов флага с числами из массива. таким образом, можно зашифровать все возможные пары букв и вытащить флаг. мы это сделали написав скрипт на python, который использует скрипт на bash, который генерирует скрипт для gdb на каждую пару символов. в gdb просто ставится breakpoint на нужном месте и из регистра считаывается шифртекст. ~~да, интерпретатор, который использует интерпретатор, который использует интерпретатор, чтобы вытаскивать значения регистров.~~ далее, сохраняем все пары зашифрованные символы <-> сама биграмма и декодируем флаг.

генератор скрипта для gdb: [script.sh](reverse1/script.sh)
перебор и декодирование флага: [reverse1](reverse1/solve.py)

флаг: `nto{4n0TH3R_bRu73F0RC3_7ASk}`