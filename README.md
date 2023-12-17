<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/VK_Compact_Logo.svg/2048px-VK_Compact_Logo.svg.png"  width="200" height="200">

# <p align="center">VK Group Activity Analytics
<p align="center">Анализ активности групп ВК методом парсинга данных постов.

## Возможности:

 - Извлечение данных из постов группы ВК:
    
    * ID поста
 
    * Количество постов
    
    * Количество лайков
    
    * Количество комментариев
    
    * Количество просмотров

    * Дата публикации поста

 - Сохрание извлеченных данных:
    
    * В виде Json, xlsx, csv

 - Импорт данных в ElasticSearch

## Установка библиотек
 
 `pip install -r requirements.txt`
  

## Документация библиотек:
 
 `requests` [Документация](https://pypi.org/project/requests/)
 
 `pandas` [Документация](https://pypi.org/project/pandas/)
 
 `json` [Документация](https://docs.python.org/3/library/json.html)
 
 `tqdm` [Документация](https://pypi.org/project/tqdm/2.2.3/)
 
 `datetime` [Документация](https://pypi.org/project/DateTime/)
 
 `elasticsearch` [Документация](https://pypi.org/project/elasticsearch/)
 
 `art` [Документация](https://pypi.org/project/art/)

## Конфигурация:

В 17 строке в файле VKparse.py замените на свой ключ

 - `parts = {'access_token' : 'СЮДА КЛЮЧ',
         'v' : '5.131',
         'count' : 100,
         'offset' : 0}`

 ## Запуск
 
`python VKparse.py`

## Над проектом работали команда Foresti Team

__Номер группы:__ *3743801/23001*

- __Нурмухаммед Бостан__

- __Михаил Сухов__

- __Волкова Диана__

- __Ляшенко Валерий__
