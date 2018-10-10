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

    # 억지로 related_name, related_query_name 만들어주려고 시도한 결과
    # friends = models.ManyToManyField('self', related_name='facebookuser', related_query_name='facebookuser')

    class Meta:
        verbose_name_plural = 'Self - FacebookUser'

    def __str__(self):
        # name이 '이한영'이며
        # 친구로 '박보영', '아이유'를 가지는 경우
        # -> 이한영 (친구: 박보영, 아이유)
        #  __str__의 결과가 위처럼 출력될 수 있도록 작성

        # 181009 재도전...
        # 결과 하루 걸림...

        # (3) values_list('', flat=True)
        # return '{} (친구: {})'.format(
        #     self.name,
        #     ', '.join(list(self.friends.values_list('name', flat=True)))
        # )

        # (1) 하루 종일 나를 헤매게한 정체 불명의 개념...
        f = FacebookUser.objects.get(id=self.pk)
        friends_object_list = FacebookUser.objects.filter(facebookuser__friends__pk=self.pk)
        friends_list = ', '.join([i.name for i in friends_object_list])

        # (1)
        # friends_list = []
        # for i in self.friends.all():
        #     friends_list.append(i.name)
        #
        # return '{} (친구: {})'.format(
        #     self.name,
        #     ', '.join(friends_list),
        # )

        # (2)
        return '{} (친구: {})'.format(
            self.name,
            ', '.join([i.name for i in self.friends.all()]),
        )

        # # 방법 1
        # # for loop를 사용 -> 제일 무식한 방법
        # friends_string = ''
        # for friend in self.friends.all():
        #     friends_string += friend.name
        #     friends_string += ', '
        # friends_string = friends_string[:-2]
        #
        # # 방법 2
        # # list comprehension 사용
        # friends_string = ', '.join([friend.name for friend in self.friends.all()])
        #
        # # 방법 3 - 쿼리차원에서 효율적으로 가져오는 방법 (네임만 필요할 때)
        # # Manager의 values_list를 사용
        # #   DB에서 모든 friends의 'name'필드 값만 가져옴
        # friends_string = ', '.join(self.friends.values_list('name', flat=True))
        #
        # return '{name} (친구: {friends})'.format(
        #     name=self.name,
        #     friends=friends_string,
        # )
