from datetime import datetime

from django.db import models
from django.utils import timezone

__all__ = (
    'Post',
    'User',
    'PostLike',
)



# Extra fields on many-to-many relationships (Basic)
class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        # MTM으로 연결된 반대편에서
        # (지금의 경우 특정 User가 좋아요 누른
        #   Post목록을 가져오고 싶은 경우)
        # 자동 생성되는 역방향 매니저 이름인 post_set대신
        #   like_posts라는 이름을 사용하도록 한다
        # ex) user2.like_posts.all()
        related_name='like_posts',
    )

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    # related_post = models.ForeignKey( # -> 이렇게는 안됨. 어떤 모델에서 왔는지 판단이 안됨.
    #     Post,                         # 그래도 또 써야되면..
    #     on_delete=models.CASCADE,
    # )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    # recommender = models.ForeignKey(  # -> 누가 좋아요를 해달라고해서 좋아요를 눌렀다에서 '누가'
    #     User,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    # )
    # 굳이 필요허면 나중에 배우자


    created_date = models.DateTimeField(
        auto_now_add=True  ## 심지어 auto로 자동으로 들어가는데도 튜플로 언패킹 허용이 안됨.
    )                       # 중개모델이 있는 m-t-m에서 뭘 만든다하면 무조건 중개모델에서 create 해야함.

    def __str__(self):
        # 글 title이 "공지사항"이며
        # 유저 name이 "이한영"이고,
        # 좋아요 누른 시점이 2018.01.31일때
        # "공지사항"글의 좋아요(이한영, 2018.01.31)으로 출력
        return '"{title}"글의 좋아요({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            # created_date=self.created_date

            date=datetime.strftime(
                # timezone.make_naive(self.created_date),
                timezone.localtime(self.created_date), # ->  tzinfo값으로 Asia/Seoul을 가짐.
                '%Y.%m.%d'),
        )

