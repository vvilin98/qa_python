# qa_python
Для покрытия тестами части приложения BooksCollector, был составлен чек лист:
- Проверка добавления книг.
- Нельзя добавить одну и ту же книгу дважды.
- Нельзя выставить рейтинг книге, которой нет в списке.
- Нельзя выставить рейтинг меньше 1.
- Нельзя выставить рейтинг больше 10.
- У не добавленной книги нет рейтинга.
- Добавление книги в избранное.
- Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
- Проверка удаления книги из избранного.