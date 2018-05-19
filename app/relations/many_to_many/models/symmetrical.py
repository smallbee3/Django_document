from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
    # -> 팔로잉만 있고 팔로워가 없는 이유 : 인스타그램에서 누군가를 팔로잉하는것밖에 없음.
        'self',
        # 대칭관계가 아님 -> 팔로잉만 하는 인스타그램 같은 서비스 / 페이스북과 다름
        symmetrical=False,
        # 역참조시 사용할 이름
        related_name='followers',
    )

    class Meta:
        verbose_name_plural = 'Symmetrical - InstagramUser'

    def __str__(self):
        return self.name

    # def followers(self):
    #     # 자신을 following하고 있는 사람들을 리턴
    #     # 문자열이 아닌 쿼리 자체
    #     return self.instagramuser_set.all()
    #       -> related_name 지정해서 instagramuser_set 못씀

    # -> 위에 related_name='followers' 역참조 이름 정의 한 줄로 해결.

