[Вернуться][main]

# О чём?

На семинаре создадим приложение для сокращения `URL` с помощью `Python` и `FastAPI`.
URL-адреса могут быть очень длинными и неудобными для использования.
Именно здесь может пригодиться такое приложение.
Приложение будет сокращать количество символов в URL,
делая его более удобным для чтения, запоминания и обмена.

На семинаре узнаем, как:

- Создавать `REST API` с помощью [FastAPI][fastapi]
- Запускать веб-сервер с помощью `Uvicorn`
- Моделировать базу данных `SQLite`
- Изучать автоматически генерируемую документацию по `API`
- Взаимодействовать с базой данных с помощью `CRUD`
- Оптимизировать приложение путём рефакторинга кода

# Обзор

Проект будет предоставлять `API endpoints`, способные принимать различные типы HTTP-запросов.
Каждый `endpoint` будет выполнять определенное действие, которое укажем.

Краткое описание `API endpoints`:

| endpoint            | тип запроса | тело запроса   | Action                                                                            |
|---------------------|-------------|----------------|-----------------------------------------------------------------------------------|
| /                   | GET         |                | Возвращает строку `Hello, World!`                                                 |
| /url                | POST        | целевой URL    | Показывает созданный `url_key` с дополнительной информацией, включая `secret_key` |
| /{url_key}          | GET         |                | Переходит на целевой URL                                                          |
| /admin/{secret_key} | GET         |                | Показывает административную информацию о сокращённом URL                          |
| /admin/{secret_key} | DELETE      | секретный ключ | Удаляет сокращённый URL                                                           |

Код, который будем писать на семинаре, в первую очередь направлен на то, чтобы приложение работало.
Однако наличие работающего приложения не всегда означает, что код, лежащий в его основе, идеален.
Поэтому на семинаре будет этап, на котором будем рефакторить некоторые части приложения.

[Вернуться][main]

---

[main]: ../../README.md "содержание"

[fastapi]: https://fastapi.tiangolo.com/ "fastapi"
