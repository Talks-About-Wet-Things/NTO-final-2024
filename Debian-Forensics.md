## Debian forensics

### Вопрос 1
на сервере установлен GitLab Community Edition версии 15.2.2. можно узнать из `/opt/gitlab/LICENSE`

### Вопрос 2
злоумышленник использовал RCE уязвимость в GitLab. это критическая [CVE-2022-2884](https://nvd.nist.gov/vuln/detail/CVE-2022-2884)

### Вопрос 3
1. у пользователя `git`(из под которого запущен GitLab) есть право запускать `git` через `sudo` от `root` без пароля
2. на программе `/usr/bin/git` стоит SETUID бит. то есть, при запуске любым пользователем, `git` будет исполняться под `root`
3. разрешен вход по паролю под пользователем `root` по ssh. в `/etc/ssh/sshd_config`: `PermitRootLogin yes`

### Вопрос 4
злоумышленник использовал первую мисконфигурацию из вопроса 3

### Вопрос 5
злоумышленник добавил в доверенные для пользователя `root` ssh-ключи свой ключ:
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIKXFjUp2LlKAsLvM1PZE7CYEfztiZrOf8PHx9ja1mu2 amongus@debian
```

### Вопрос 6
злоумышленник использовал linpeas. В папке `/tmp` был файл `linpeas.txt`. из `/root/.bash_history` мы узнаем что этот файл был удален

### Вопрос 7
злоумышленник использовал руткит [Jynx2](https://github.com/chokepoint/Jynx2)