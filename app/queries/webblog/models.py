from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100, blank=False)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)

    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(blank=True, null=True)
    n_pingbacks = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.headline
