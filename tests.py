from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_one_books - добавление одной книги

    def test_add_new_book_add_one_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книги
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилось именно одна
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_rating()) == 1, "Книга не добавилась"

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_two_same_books_add_one_book(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1 , "Книга задублировалась"

    def test_add_rating_book_whith_isnot_book_rating_rating_not_add(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Рандомная книга',7)
        assert 'Рандомная книга' not in collector.get_books_rating()


    def test_set_book_rating_less_1_rating_less_1_not_add(self,):

        collector = BooksCollector()

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить',-1)
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == 1


    def test_set_book_rating_more_10_rating_more_10_not_add(self,):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби',12)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_rating_which_not_in_book_rating_book_not_rating(self):

        collector = BooksCollector()

        collector.set_book_rating('Рандомная книга',7)
        assert collector.get_book_rating('Рандомная книга') == None

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_which_not_book_rating_book_not_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_in_favorites_zero(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0