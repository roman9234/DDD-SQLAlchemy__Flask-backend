

Добавление книг:
curl -L "http://127.0.0.1:5000/books/" -XPOST --json "{\"title\":\"title of book 1\",\"description\":\"book 1 description\",\"publish_year\":\"2003\",\"pages_count\":\"250\",\"created_at\":\"2021-01-01\"}"

curl -L "http://127.0.0.1:5000/books/" -XPOST --json "{\"title\":\"title of book 2\",\"description\":\"book 2 description\",\"publish_year\":\"2009\",\"pages_count\":\"170\",\"created_at\":\"2021-01-01\"}"

curl -L "http://127.0.0.1:5000/books/" -XPOST --json "{\"title\":\"title of book 3\",\"description\":\"book 3 description\",\"publish_year\":\"2013\",\"pages_count\":\"400\",\"created_at\":\"2022-01-01\"}"

Получение книг:
curl -L "http://127.0.0.1:5000/books/" -XGET

Удаление книг:
curl -L "http://127.0.0.1:5000/books/1" -XDELETE

Обновление книг:

curl -L "http://127.0.0.1:5000/books/2" -XUPDATE --json "{\"title\":\"title of UPDATED book 2\",\"description\":\"book 2 description\",\"publish_year\":\"2007\",\"pages_count\":\"300\",\"created_at\":\"2021-01-01\"}"


За что отвечают разделы (подробнее в файлах)

Domain:  Фокусируется на логике предметной области, оставаясь независимым от внешних зависимостей.
Infra:  Обеспечивает связь с внешним миром, не вмешиваясь в бизнес-логику.
Application:  Содержит бизнес-логику, отделяет интерфейс пользователя от ORM
Views:  Предоставляет интерфейс для пользователей, не заботясь о деталях реализации.

