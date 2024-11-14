# О проекте:

Пэт-проект.
Этот проект представляет собой блог-соц.сеть на `Django`. 

## Функционал:
- Авторизация.
- Создание, редактирование постов.
- Комментарии к постам.
- Лайки к постам.
- Подписка/отписка.
- Просмотр списка и количества подписок/подписчиков.
- Просмотр постов определенного автора, всех авторов, только своих подписок.


# API DRF:

Здесь описаны основные запросы на сервер для получения данных:

#### Для просмотра всех постов, которые существуют отправляется запрос:

``` 
http://127.0.0.1:8000/api/post/
```

Ответ:

```json
{
    "count": 51,
    "next": "http://127.0.0.1:8000/api/post/?limit=3&offset=3",
    "previous": null,
    "results": [
        {
            "id": 5,
            "title_name": "Название",
            "description": "Описание",
            "date_create": "2024-01-09T14:02:23.205502Z",
            "author": "username"
        },
        {
            "id": 6,
            "title_name": "Название",
            "description": "Описание",
            "date_create": "2024-01-09T16:16:20.605098Z",
            "author": "username"
        },
        {
            "id": 7,
            "title_name": "Название",
            "description": "Описание",
            "date_create": "2024-01-09T16:17:43.546032Z",
            "author": "username"
        }
    ]
}
```

#### Для просмотра определенного поста, отправляется запрос:

``` 
http://127.0.0.1:8000/api/product/id_post
```

#### Для просмотра постов определенного автора, отправляется запрос:

``` 
http://127.0.0.1:8000/api/post/?author=username
```

### Для создания, удаления, редактирования поста - нужно авторизоваться и получить свой api-token:

```
http://127.0.0.1:8000/api-token-auth/
```

## Изображения:
![alt text](https://raw.githubusercontent.com/vetalissa/blogs_project/f8d3e4f37fb9df9e91b8c5abe2946fb8b17bd98b/1.png)
![alt text](https://raw.githubusercontent.com/vetalissa/blogs_project/f8d3e4f37fb9df9e91b8c5abe2946fb8b17bd98b/2.png)
![alt text](https://raw.githubusercontent.com/vetalissa/blogs_project/f8d3e4f37fb9df9e91b8c5abe2946fb8b17bd98b/3.png)
![alt text](https://raw.githubusercontent.com/vetalissa/blogs_project/f8d3e4f37fb9df9e91b8c5abe2946fb8b17bd98b/4.png)
![alt text](https://raw.githubusercontent.com/vetalissa/blogs_project/f8d3e4f37fb9df9e91b8c5abe2946fb8b17bd98b/5.png)
![alt text](https://raw.githubusercontent.com/vetalissa/blogs_project/f8d3e4f37fb9df9e91b8c5abe2946fb8b17bd98b/6.png)
![alt text](https://raw.githubusercontent.com/vetalissa/blogs_project/f8d3e4f37fb9df9e91b8c5abe2946fb8b17bd98b/7.png)
