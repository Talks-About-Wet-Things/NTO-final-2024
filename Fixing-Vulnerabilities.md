## Fixing vulnerabilities

### Заложенные уязвимости

#### XSS в заметках
Если пользователь вставит в заметки пэйлоады для xss с сайта [https://github.com/payloadbox/xss-payload-list](https://github.com/payloadbox/xss-payload-list), несколько десятков из них сработают. Чинится с DOMPurify


#### SQL injection in password reset
В коде эндпоинта по смене пароля можно вставить SQL иньекцию, так как строки конкатинируются

```python
sql_query = "UPDATE user SET pw = '" + str(new_password) + "' WHERE login = '" + str(username) + "';"
```
фикс: использование валидации или механизма конструкции запроса


#### Неправильные права доступа
Не имея прав админа можно менять значения светофоров через API


#### Смена пароля другому пользователю
При смене пароля в функции `changePassword`, не проверяется, что пользователь меняет пароль самому себе. Пользователь может сменить пароль другому пользователю, если знает его текущий пароль. Чтобы это исправить, нужно менять пароль по юзернейму из jwt токена, а не из параметра


### Не заложенные уязвимости

#### CORS
`Access-Control-Allow-Origin: *` слишком свободная политика, рекомендуется явно разрешать необходимые ориджины


#### Пароли в открытом виде
В базе данных пароли хранятся в открытом виде. Необходимо хэшировать пароли и хранить хэш-суммы


#### Раскрытие уязвимых данных
В `auth_api.py` в эндпоинте `register` при ошибке в БД эта ошибка возвращается в ответе, что может привести к раскрытию данных о структуре БД

```python
        except sqlite3.IntegrityError as e:
            error = "Ошибка БД: " + str(e)
            code = HTTPStatus.INTERNAL_SERVER_ERROR
```