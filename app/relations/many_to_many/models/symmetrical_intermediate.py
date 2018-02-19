from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    """
    내가 A를 follow 함
        나는 A의 follower
        A는 나의 followee(팔로잉을 당하고 있는 사람)

    A와 내가 서로 follow함
        나와 A는 friend

    Block기능이 있어야 함
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        # relations는 Relation을 중개모델로 써서 자기 자신과 연결이 된 것.
        # 문제는 u1.relations.all()을 했을 때 타입을 모름.
        'self',
        symmetrical=False,
        through='Relation',
        # related_name='+',  # related_name에 +하면 역참조가 없어짐.
    )

    class Meta:
        verbose_name_plural = 'symmetrical_intermediate - TwitterUser'


    def __str__(self):
        return self.name

    @property
    def following(self):
        """
        내가 follow하고 있는 TwitterUser목록을 가져옴
        :return:
        """
        # 내가 from_user이며, type이 팔로잉인 Relation의 쿼리
        following_relations = self.from_user_set.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
            # type='f',
        )
        # 위와 같은 의미, from_user=u1를 써주고 안써줘도 되냐의 차이
        # following_relations = Relatioin.objects.filter(from_user=u1, type='f')

        # 팔로잉 'relation' 리스트지 아직 팔로잉 '유저 name' 리스트는 아님.

        # 위에서 정제한 쿼리셋에서 'to_user'값만 리스트로 가져옴 (내가 팔로잉하는 유저의 pk리스트)
        following_pk_list = following_relations.values_list('to_user', flat=True)
        # TwitterUser테이블에서 pk가
        # 바로 윗줄에서 만든 following_pk_list (내가 팔로잉하는 유저의 pk리스트)
        #   에 포함되는 User목록을 following_users변수로 할당

        # 수업시간 : pk__in 을 활용
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)

        # 내가 찾은 지저분한 방법 : list comprehesion을 이용
        # following_users = [TwitterUser.objects.get(pk=pk) for pk in following_pk_list]
        # -> 위 방법은 쿼리셋으로 반환, 아래 방법은 리스트로 반환. 큰 차이없으므로 깔끔한 위 방법을 쓰자.
        #########################################################################
        # 기존에 쿼리셋으로 반환하는 것에서 리스트로 바꾸니 아래 is_following에서 쿼리셋을 못써서 문제발생.
        #########################################################################

        return following_users


    @property
    def followers(self):
        pk_list = self.to_user_set.filter(type='f').values_list('from_user', flat=True)
        return TwitterUser.objects.filter(pk__in=pk_list)
        # 내가 to_user고 팔로잉목록인 relation 목록에서
        # from_user만 가져오면 나를 팔로우하고 있는 사람이 되죠.


    @property
    def blocking(self):
        """
        내가 block하고 있는 TwitterUser목록을 가져옴
        """
        block_relations = self.from_user_set.filter(
            type='b',
        )
        block_pk_list = block_relations.values_list('to_user', flat=True)
        blocking = TwitterUser.objects.filter(pk__in=block_pk_list)
        return blocking

    @property
    def block_users(self):
        """
        나를 block하고 있는 TwitterUser목록을 가져옴
        """
        block_relations = self.to_user_set.filter(
            type='b',
        )
        block_pk_list = block_relations.values_list('from_user', flat=True)
        block_users = TwitterUser.objects.filter(pk__in=block_pk_list)
        return block_users


    # @property -> 함수가 인자를 받기 때문에 안됨
    def is_following(self, to_user):
    # def is_followee(self, to_user): # -> 말이 너무 헷갈림.
        """
        내가 to_user를 follow하고 있는지 여부를 True/False로 반환
        :param to_user:
        :return:
        """
        # following_pk_list = self.from_user_set.filter(type='f').values_list('to_user', flat=True)
        # if to_user.pk in following_pk_list:
        #     return True
        # else:
        #     return False

        return self.following.filter(pk=to_user.pk).exists()
                # 1. 위에 있는 following 메소드를 property로 가져온것?
                # 2. 'following' 메소드와 다르게 to_user.pk를 한 것은
                #                .value()로 값을 가져오는게 아니기 때문

    # @property -> 함수가 인자를 받기 때문에 안됨
    def is_follower(self, from_user):
        """
        from_user가 나를 follow하고 있는지 여부를 True/False로 반환
        :param from_user:
        :return:
        """
        # follower_pk_list = to_user.from_user_set.filter(type='f').values_list('from_user', flat=True)
        # if from_user.pk in follower_pk_list:
        #     return True
        # else:
        #     return False
        return self.followers.filter(pk=from_user.pk).exists()



    def follow(self, to_user):
        """
        to_user에 주어진 TwitterUser를 follow함
        :param to_user:
        :return:
        """
        self.from_user_set.filter(to_user=to_user).delete()
        self.from_user_set.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        # Relation.objects.create(
        #     from_user=self,
        #     to_user=to_user,
        #     type=Relation.RELATION_TYPE_FOLLOWING,
        # )
        # 위와 같은 말

        # self.save() -> 필요없음

    def block(self, to_user):
        """
        to_user에 주어진 TwitterUser를 block함
        :param to_user:
        :return:
        """
        # 깊게 고민안하면 그냥 지워버리고 만들면 되요.
        # myopinion : 아마 지금 팔로잉중이면 물어보는 팝업창 띄워주어야하는데
        #             그럴려면 그냥 지워버리기보다 if 문으로 물어봐야할듯.
        self.from_user_set.filter(to_user=to_user).delete()
        # / 만약 기존 기록을 기억하고 싶으면 다른방법으로 해야함.
        # -> 밑에서 .DateTimeField(auto_now_add=True)를 auto_now=True로
        #    바꿔서 기존값을 수정하는 방법이 있음.

        self.from_user_set.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_BLOCK,
        )


class Relation(models.Model):
    """
    유저간의 관계를 정의하는 모델
    단순히 자신의 MTM이 아닌 중개모델의 역할을 함
    추가적으로 받는 정보는 관계의 타입(팔로잉 또는 차단)
    """
    RELATION_TYPE_FOLLOWING = 'f'  # -> 클래스변수로 선언하는게 편함?.
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 from_user인 경우에 Relation목록을 가져오고 싶을 경우
        related_name='from_user_set',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 to_user인 경우에 Relation목록을 가져오고 싶을 경우
        related_name='to_user_set',
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)

    # following / block 날짜를 저장하고 보여주고 싶다면,
    created_date = models.DateTimeField(auto_now_add=True) # 앞으로 생성할 것에 대해 무엇을 넣어주겠다는 표현.
    # 업데이트 (값이 수정) 될 때 마다 그 시간을 저장하고 싶다면.
    # modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"'{self.from_user.name}'가 '{self.to_user.name}'를 '{self.get_type_display()}'함"


    class Meta:
        verbose_name_plural = 'symmetrical_intermediate - Relation'

        unique_together = (
            # from_user와 to_user의 값이 이미 있을 경우
            # DB에 중복 데이터 저장을 막음
            # ex) from_user가 1, to_user가 3인 데이터가 이미 있다면
            #       두 항목의 값이 모두 같은 또 다른 데이터가 존재할 수 없음
            ('from_user', 'to_user'),
        )

        # -> 테이블 자체에 대한 설정