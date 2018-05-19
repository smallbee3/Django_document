from django.db import models

"""
Specifying the parent link field¶
As mentioned, Django will automatically create a OneToOneField
linking your child class back to any non-abstract parent models.
If you want to control the name of the attribute linking back to
the parent, you can create your own OneToOneField and set 
parent_link=True to indicate that your field is the link back to
the parent class.
https://docs.djangoproject.com/en/2.0/topics/db/models/#specifying-the-parent-link-field
"""


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