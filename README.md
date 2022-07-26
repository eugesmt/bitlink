# Обрезка ссылок с помощью Битли

Программа предназнаена для сокращения длинных URL-адресов.

Перед сокращением  изначально проверяется, есть ли уже короткая ссылка URL-адреса, если ссылка уже имеется то выводится URL-адрес сокращенной ссылки.

Если ввести коротку ссылку URL-адреса , то будет показно суммарное количество переходов по данноый ссылке.


### Как установить

Для ипользования программы, изначально необходимо получить  
`GENERIC ACCESS TOKEN` — нужный тип токена. 

Сылка для получения: [Генератор токенов](https://bitly.com/a/oauth_apps)

Пример полученной ссылки: `17c09e20ad155405123ac1977542fecf00231da7`

Полученный токен необходимо разместить в файле `.env`, переменная  `BITLY_TOKEN`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Запуск скрипта для сокращения URL-адреса:

```python main.py [В параметр указывается URL-адрес]```

Пример выполнения скрипта для сокращения URL-адреса:

```python main.py https://yandex.ru/```

Результат выполнения скрипта для сокращения URL-адреса:

```Битлинк: https://bit.ly/3uBCX3J```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).