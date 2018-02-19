from django.db import models


class Piece(models.Model):
    pass

class Article(Piece):
    article_piece = models.OneToOneField(
        Piece,
        on_delete=models.CASCADE,
        parent_link=True
    )
    pass

class Book(Piece):
    book_piece = models.OneToOneField(
        Piece,
        on_delete=models.CASCADE,
        parent_link=True
    )
    pass

class BookReview(Book, Article):
    pass