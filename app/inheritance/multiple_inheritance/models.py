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


# (1) Use an explicit AutoField in the base models

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ...


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ...


class BookReview(Book, Article):
    pass


# (2) Use a common ancestor to hold the AutoField

class Piece(models.Model):
    pass


class Article2(Piece):
    article_piece = models.OneToOneField(
        Piece,
        on_delete=models.CASCADE,
        parent_link=True
    )
    pass


class Book2(Piece):
    book_piece = models.OneToOneField(
        Piece,
        on_delete=models.CASCADE,
        parent_link=True
    )
    pass


# class BookReview(Article):
class BookReview2(Book2, Article2):
    pass
