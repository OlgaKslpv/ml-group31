## Приложение определяет тональность текста на корейском языке.
Задание по дисциплине "Программная инженерия" магистратуры "Инженерия машинного обучения".

#### Оглавление:
- [Цель проекта](#цель-проекта)
- [Описание проекта](#описание-проекта)
- [Запуск и результаты работы проекта](#запуск-и-результаты-работы-проекта)
- [Запуск и результаты тестов](#запуск-и-результаты-тестов)
- [Источники](#источники)
- [Авторы](#авторы)


### Цель проекта:

Разработать Web или API-приложение машинного обучения и развернуть его в облаке. 

### Описание проекта:

Нами были подготовлено API-приложение по определению тональности текстов на корейском языке - (https://github.com/OlgaKslpv/ml-group31/blob/main/main.py). Приложение использует модель KR-FinBert-SC (https://huggingface.co/snunlp/KR-FinBert-SC), обученную на новостных статьях, текстах из корейской Википедии, юридических текстах и базе данных корейскоязычных интернет-комментариев.

### Запуск и результаты работы проекта:


API-приложение, развернутое на Яндекс-облаке. Для передачи запроса был применен метод post и приложение postman.
Все методы:

GET /
Возвращает приветственное сообщение.

POST /predict/
Принимает текст на корейском языке и возвращает эмоциональную окраску текста (positive, neutral или negative).

GET /emotions/
Возвращает список всех эмоций, поддерживаемых моделью.

GET /get-user/
Принимает ID зарегистрированного пользователя и возвращает его адрес электронной почты.



<img src="https://user-images.githubusercontent.com/118006933/215146049-599d74ca-a6b4-432a-b6ae-19b802c737ae.png" width="960" height="540">


### Запуск и результаты тестов:

Для API-приложения были написаны [тесты](https://github.com/OlgaKslpv/ml-group31/blob/main/project/test_main.py). Запуск осуществляется введением команды pytest в каталоге с приложением, также на GitHub была настроена система  Continuous Integration таким образом, что при выполнении push в репозиторий GitHub выполняется автоматический запуск тестов.

<img src="https://user-images.githubusercontent.com/118006933/215255939-fb817cf0-75b4-4e5c-b1f8-36685e6d475a.png" width="640" height="480"> 
<img src="https://user-images.githubusercontent.com/118006933/215255852-d04970bc-cc31-491d-9054-b8249564f2be.png" width="960" height="540">
<img src="https://user-images.githubusercontent.com/118006933/215255898-589adf39-0319-4dbe-bd95-64c77a0058ba.png" width="960" height="540">

### Источники:

1. [Документация pipeline на huggingface.co](https://huggingface.co/docs/transformers/main_classes/pipelines)
2. [Wiki: Transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), ([на русском](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80_(%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)))
3. [Документация io на python.org](https://docs.python.org/3/library/io.html)
4. [FastAPI](https://fastapi.tiangolo.com/)

### Авторы:
- [Косолапова Ольга](https://github.com/OlgaKslpv)
- [Филимонова Татьяна](https://github.com/Tatiana-Filimonova)
- [Гмырин Виктор](https://github.com/Victor-Gmyrin)
- [Крупский Андрей](https://github.com/KrupskiiAndrei)
