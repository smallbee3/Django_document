from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100, blank=True)

    # 181008
    artist = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '뮤지션'

    def __str__(self):
        return f'{self.last_name}{self.first_name}'


class Album(models.Model):
    # artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    num_stars = models.IntegerField()

    class Meta:
        verbose_name = '앨범'

    def __str__(self):
        return f'{self.artist}의 앨범: {self.name}'


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    # nickname = models.CharField(
    #     max_length=30,
    #     unique=True,    # -> 해당 값은 중복이 안됨. 고유한 값을 가져야함.
    # )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        # 이한영 (PK: 1, 셔츠 사이즈: Medium) 되도록 출력
        return '{} (PK: {}, 셔츠 사이즈: {} {})'.format(
            self.name,
            self.pk,
            self.get_shirt_size_display(),
            self.shirt_size,
        )
