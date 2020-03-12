from django.test import TestCase
from covers.api import GoodReadsClient, get_cover_urls


class GoodReadsTests(TestCase):

    def test_i_can_get_the_book_detail_from_the_isbn(self):
        isbn = '9780132350884'
        gc = GoodReadsClient()
        book_id = gc.book_id(isbn)
        self.assertTrue(book_id != None)

        detail = gc.book(book_id)

    def test_i_get_image_urls(self):
        isbns = ['9781491954621', '9781491912058', '9781942788003']
        res = get_cover_urls(isbns)
        debug = True
