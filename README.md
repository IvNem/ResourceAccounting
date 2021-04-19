# ResourceAccounting
Это тестовое задание для устройства на работу.

**Задание:**
Разработать веб-приложение для учёта складских запасов ресурсов. 

**Описание:**
Веб приложение должно содержать базу данных с перечнем запасов, приведённых в
Таблице 1, и должно предоставлять методы для взаимодействия с данными (REST API),
описаны в Таблице 2. Параметры должны приниматься как в JSON, так и в POST формате
параметров запроса.

*Таблица 1.*
| Id  | Наименование | Количество | Ед. Измерения | Цена за у.е. | Дата поступл. |
| --- | ------------ | ---------- | ------------- | ------------ | ------------- |
| int | String       | Real       | String        | Real         | Date          |


***Требования к решению:***
Кандидат должен самостоятельно развернуть приложение на хостинге и предоставить
URL для тестирования API. Исходный код должен должен быть выложен в открытом
доступе (Github) и содержать достаточный объем комментариев. Желательно реализовать
решение с применением стека: Flask/Django + MySQL/MongoDB/PostrgeSQL.


