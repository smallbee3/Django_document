from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    """
    자기 자신을 MTM필드로 갖는 모델
    """
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    class Meta:
        verbose_name_plural = 'Self - FacebookUser'

    def __str__(self):
        # name이 '이한영'이며
        # 친구로 '박보영', '아이유'를 가지는 경우
        # -> 이한영 (친구: 박보영, 아이유)
        #  __str__의 결과가 위처럼 출력될 수 있도록 작성

        # 방법 1
        # for loop를 사용 -> 제일 무식한 방법
        friends_string = ''
        for friend in self.friends.all():
            friends_string += friend.name
            friends_string += ', '
        friends_string = friends_string[:-2]

        # 방법 2
        # list comprehension 사용
        friends_string = ', '.join([friend.name for friend in self.friends.all()])

        # 방법 3 - 쿼리차원에서  효율적으로 가져오는 방법 (네임만 필요할 때)
        # Manager의 values_list를 사용
        #   DB에서 모든 friends의 'name'필드 값만 가져옴
        friends_string = ', '.join(self.friends.values_list('name', flat=True))

        return '{name} (친구: {friends})'.format(
            name=self.name,
            friends=friends_string,
        )