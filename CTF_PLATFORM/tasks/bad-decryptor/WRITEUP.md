# Bad Decryptor: Write-up

Итак, у нас есть страница, которая **якобы** выдает флаг. На самом деле, на ней происходит ошибка.

Что делает любой веб-разработчик, когда видит ошибку? Лезет в консоль разработчика.

Видим ошибку о нарушении политики [CORS](https://habr.com/company/pentestit/blog/337146/) (Cross-Origin Resource Sharing).

Разбираясь более подробно в этом вопросе, становится понятно, что ресурс `alliance.ugractf.ru` не разрешил использовать его ресурсы (а именно файл `flag.txt`) нашему сайту `decryptor.ugractf.ru`.

Дальше есть несколько способов решения:

### 1. Браузерный

Открываем магазин расширений нашего любимого браузера, ищем `Disable CORS`, скачиваем, заходим, получаем флаг.

### 2. JS-way

Сначала `lib.js`. Это библиотека [TripleSec](https://keybase.io/triplesec) от KeyBase. 

Мы зашифровали текст прямо кодом из примера. И если дешифровать его также кодом из примера, то получим флаг.

------

Решение выглядит просто, но для него нужно было разобраться в том, что же такое CORS, и многие не смогли этого сделать.

Флаг: **ugra_alliance_cors_secrets_revealed**